from fastapi import APIRouter, HTTPException
from pydantic import EmailStr
from project1.v1.Features.verification.func import handle_verification
from project1.v1.request.type import Email_Verification
from project1.db.db import update_data,get_data
from datetime import datetime
import os
from jose import jwt


router = APIRouter()

@router.post("/verify-email")
async def verify_email(
        email: Email_Verification):
    """
    Verify the email address and send a verification link.
    """

    # Placeholder for email verification logic
    return await handle_verification(email=email.email)

@router.get("/verify-email/{token}")
async def verify_email_link(token: str):
    """
    Verify the email address using the verification token from the link.
    """
    try:
        # Decode and verify the JWT token
        payload = jwt.decode(
            token, 
            os.getenv("SECRET_KEY"), 
            algorithms=["HS256"]
        )
        email = payload.get("email")
        
        if not email:
            raise HTTPException(
                status_code=400,
                detail="Invalid token format"
            )

        # Check if user exists and is unverified
        user = get_data(
            table_name="users",
            where_clause="email = :email",
            params={"email": email}
        )

        if not user:
            raise HTTPException(
                status_code=404,
                detail="Invalid verification link"
            )

        verified = get_data(
            table_name="users",
            columns="is_verified",
            where_clause="email = :email",
            params={"email": email}
        )

        if verified[0][0]:
            raise HTTPException(
                status_code=400,
                detail="Email is already verified"
            )
        # Update user's verification status
        updated = update_data(
            table_name="users",
            set_values={
                "is_verified": True,
                "verified_at": datetime.utcnow()
            },
            where_clause="email = :email",
            params={"email": email}
        )

        if not updated:
            raise HTTPException(
                status_code=400,
                detail="Failed to verify email"
            )

        return {
            "message": "Email verified successfully",
            "email": email
        }

    except jwt.ExpiredSignatureError:
        raise HTTPException(
            status_code=400,
            detail="Verification link has expired"
        )
    except jwt.JWTError:
        raise HTTPException(
            status_code=400,
            detail="Invalid verification token"
        )
    except Exception as e:
        # Log the error here
        print(f"Error in verify_email_link: {str(e)}")
        raise HTTPException(
            status_code=500,
            detail={
                "message": "Failed to verify email",
                "error": str(e)
            }
        )
    
@router.get("/verified/{email}")
async def verified(email: str):
    """
    Check if the email address is verified.
    """
    try:
        # Check if user exists and is verified
        user = get_data(
            table_name="users",
            columns="is_verified",
            where_clause="email = :email",
            params={"email": email}
        )

        if not user:
            raise HTTPException(
                status_code=404,
                detail="User not found"
            )

        return {
            "verified": user[0][0]
        }

    except Exception as e:
        # Log the error here
        print(f"Error in verified: {str(e)}")
        raise HTTPException(
            status_code=500,
            detail={
                "message": "Failed to check email verification status",
                "error": str(e)
            }
        )