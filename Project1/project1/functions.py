from datetime import datetime
from uuid import uuid4
from fastapi import HTTPException
from passlib.hash import bcrypt
from sqlalchemy import text
import re
from project1.db.db import engine
from project1.v1.Features.verification.func import handle_verification

async def login(
        username: str, password: str):
    """
    Authenticate a user and return their profile information.
    
    Args:
        username (str): Username or email for login
        password (str): User's password
    
    Returns:
        dict: User profile information if authentication successful
        
    Raises:
        HTTPException: If authentication fails or user is not verified
    """
    try:
        # Check if username input is email format
        is_email = bool(re.match(r"[^@]+@[^@]+\.[^@]+", username))
        where_clause = "email = :username" if is_email else "username = :username"
        
        # Get user from database
        with engine.connect() as conn:
            query = text(f"SELECT * FROM users WHERE {where_clause}")
            result = conn.execute(query, {"username": username})
            user = result.fetchone()
            
            if not user:
                raise HTTPException(
                    status_code=401,
                    detail="Invalid credentials"
                )
            
            # Verify password
            if not await bcrypt.verify(password, user.password):
                raise HTTPException(
                    status_code=401,
                    detail="Invalid credentials"
                )
            
            # Check if user is verified
            if not user.is_verified:
                raise HTTPException(
                    status_code=403,
                    detail="Email not verified. Please verify your email first."
                )
            
            # Check if user is active
            if not user.is_active:
                raise HTTPException(
                    status_code=403,
                    detail="Account is deactivated. Please contact support."
                )
            
            # Update last login time
            update_query = text("""
                UPDATE users 
                SET last_login = :login_time 
                WHERE id = :user_id
            """)
            conn.execute(update_query, {
                "login_time": datetime.utcnow(),
                "user_id": user.id
            })
            conn.commit()
            
            # Return user data (excluding password)
            return {
                "id": user.id,
                "username": user.username,
                "email": user.email,
                "is_verified": user.is_verified,
                "is_active": user.is_active,
                "created_at": user.created_at,
                "last_login": user.last_login
            }
            
    except HTTPException as he:
        raise he
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Login failed: {str(e)}"
        )
    

async def register(username: str, password: str, email: str):
    """
    Register a new user and initiate email verification.
    If email verification fails, the user registration is rolled back.
    
    Args:
        username (str): Desired username
        password (str): User's password
        email (str): User's email address
    
    Returns:
        dict: Registration status and verification email details
        
    Raises:
        HTTPException: If registration fails due to validation or duplicate entries
    """
    # Store user_id for potential rollback
    user_id = None
    
    try:
        # Validate input lengths
        if len(username) < 3:
            raise HTTPException(
                status_code=400,
                detail="Username must be at least 3 characters long"
            )
            
        if len(password) < 8:
            raise HTTPException(
                status_code=400,
                detail="Password must be at least 8 characters long"
            )
            
        # Validate email format
        if not bool(re.match(r"[^@]+@[^@]+\.[^@]+", email)):
            raise HTTPException(
                status_code=400,
                detail="Invalid email format"
            )
            
        # Check for existing username or email
        with engine.connect() as conn:
            query = text("""
                SELECT username, email 
                FROM users 
                WHERE username = :username OR email = :email
            """)
            result = conn.execute(query, {
                "username": username,
                "email": email
            })
            existing_user = result.fetchone()
            
            if existing_user:
                if existing_user.username == username:
                    raise HTTPException(
                        status_code=400,
                        detail="Username already taken"
                    )
                else:
                    raise HTTPException(
                        status_code=400,
                        detail="Email already registered"
                    )
            
            # Generate user ID
            user_id = str(uuid4())
        try:
            # Create new user
            insert_query = text("""
                INSERT INTO users (
                    id, username, password, email, 
                    is_verified, is_active
                ) VALUES (
                    :id, :username, :password, :email, 
                    false, true
                )
            """)
            
            # Hash password
            hashed_password = bcrypt.hash(password)
            
            conn.execute(insert_query, {
                "id": user_id,
                "username": username,
                "password": hashed_password,
                "email": email
            })
            conn.commit()
            
            # Send verification email
            await handle_verification(email)
            
        except Exception as email_error:
            # If email sending fails, delete the user and raise the error
            with engine.connect() as conn:
                delete_query = text("DELETE FROM users WHERE id = :user_id")
                conn.execute(delete_query, {"user_id": user_id})
                conn.commit()
            
            raise HTTPException(
                status_code=500,
                detail=f"Failed to send verification email: {str(email_error)}"
            )
            
        return {
            "message": "Registration successful",
            "detail": f"Verification email sent to {email}"
        }
            
    except HTTPException as he:
        raise he
    except Exception as e:
        # If we have a user_id but encountered a different error, try to clean up
        if user_id:
            try:
                with engine.connect() as conn:
                    delete_query = text("DELETE FROM users WHERE id = :user_id")
                    conn.execute(delete_query, {"user_id": user_id})
                    conn.commit()
            except Exception as cleanup_error:
                # Log cleanup error but raise the original error to the user
                print(f"Failed to clean up user during registration rollback: {cleanup_error}")
        
        raise HTTPException(
            status_code=500,
            detail=f"Registration failed: {str(e)}"
        )