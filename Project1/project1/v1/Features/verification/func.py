from fastapi.responses import JSONResponse
from fastapi_mail import FastMail, MessageSchema, ConnectionConfig
from typing import Optional
import os
from datetime import datetime, timedelta
from jose import jwt
from email_validator import validate_email, EmailNotValidError
from project1.db.db import get_data, update_data

async def create_redirect_link(email: str) -> str:
    """Create a verification link with JWT token."""
    payload = {
        "email": email,
        "exp": datetime.utcnow() + timedelta(hours=24)  # Token expires in 24 hours
    }
    token = jwt.encode(payload, os.getenv("SECRET_KEY"), algorithm="HS256")
    base_url = os.getenv("BASE_URL", "http://localhost")
    return f"{base_url}/api/verify-email/{token}"

def is_email(email: str) -> bool:
    """Validate email format."""
    try:
        validate_email(email)
        return True
    except EmailNotValidError:
        return False

async def handle_verification(email: str) -> JSONResponse:
    """
    Handle email verification.

    Args:
        email (str): Email address to verify.

    Returns:
        Response: FastAPI response object.
    """
    try:
        # Validate email format
        if not is_email(email):
            return JSONResponse(
                content="Invalid email address format", 
                status_code=400
            )

        # Check if email already exists and is verified
        user = get_data(
            table_name="users",
            where_clause="email = :email",
            params={"email": email}
        )

        if user and user[0].is_verified:
            return JSONResponse(
                content="Email is already verified",
                status_code=400
            )

        # Create verification link with token
        redirect_link = await create_redirect_link(email)

        # Configure email settings
        connection_config = ConnectionConfig(
            MAIL_USERNAME=os.getenv("MAIL_USERNAME"),
            MAIL_PASSWORD=os.getenv("MAIL_PASSWORD"),
            MAIL_FROM=os.getenv("MAIL_FROM"),
            MAIL_PORT=int(os.getenv("MAIL_PORT", "587")),
            MAIL_SERVER="smtp.gmail.com",
            MAIL_STARTTLS=True,
            MAIL_SSL_TLS=False,
            USE_CREDENTIALS=True,
            MAIL_FROM_NAME="FastAPI"
        )

        # Create email message with HTML template
        html_content = f"""
        <html>
            <body>
                <h2>Email Verification</h2>
                <p>Please click the link below to verify your email address:</p>
                <p><a href="{redirect_link}">Verify Email</a></p>
                {redirect_link}
                <p>This link will expire in 24 hours.</p>
                <p>If you didn't request this verification, please ignore this email.</p>
            </body>
        </html>
        """

        message = MessageSchema(
            subject="Email Verification",
            recipients=[email],
            body=html_content,
            subtype="html"
        )

        # Send email
        fm = FastMail(connection_config)
        await fm.send_message(message)

        # Update user record to mark verification email as sent
        update_data(
            table_name="users",
            set_values={
                "verification_sent_at": datetime.utcnow()
            },
            where_clause="email = :email",
            params={"email": email}
        )

        return JSONResponse(
            content=f"Verification link sent to {email}",
            status_code=200
        )

    except Exception as e:
        # Log the error details here
        print(f"Error in handle_verification: {str(e)}")
        return JSONResponse(
            content={
                "message": "Failed to send verification email",
                "error": str(e)
            },
            status_code=500
        )
    
    