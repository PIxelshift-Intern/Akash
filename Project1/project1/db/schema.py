from sqlalchemy import (
    MetaData, Table, Column, Integer, String, 
    DateTime, ForeignKey, Boolean, JSON, Text,
    UniqueConstraint, CheckConstraint
)
from sqlalchemy.sql import func
from db.db import engine
import uuid

def generate_uuid():
    return str(uuid.uuid4())

metadata = MetaData()

users = Table(
    "users",
    metadata,
    Column("id", String(36), primary_key=True, default=generate_uuid),
    Column("username", String(50), unique=True, nullable=False),
    Column("password", String(255), nullable=False),
    Column("email", String(255), unique=True, nullable=False),
    Column("created_at", DateTime, server_default=func.now(), nullable=False),
    Column("updated_at", DateTime, server_default=func.now(), onupdate=func.now()),
    Column("is_verified", Boolean, server_default="false", nullable=False),
    Column("is_active", Boolean, server_default="true", nullable=False),
    Column("verification_sent_at", DateTime),
    Column("verified_at", DateTime),
    Column("last_login", DateTime),
    
    # Add constraints
    CheckConstraint('length(username) >= 3', name='username_length_check'),
    CheckConstraint('length(password) >= 8', name='password_length_check')
)

data = Table(
    "data",
    metadata,
    Column("id", String(36), primary_key=True, default=generate_uuid),
    Column("data", JSON, nullable=False),
    Column("created_at", DateTime, server_default=func.now(), nullable=False),
    Column("updated_at", DateTime, server_default=func.now(), onupdate=func.now()),
    Column("data_type", String(50), nullable=False),  # To categorize different types of data
    Column("version", Integer, server_default="1", nullable=False)
)

user_data = Table(
    "user_data",
    metadata,
    Column("id", String(36), primary_key=True, default=generate_uuid),
    Column("user_id", String(36), ForeignKey("users.id", ondelete="CASCADE"), nullable=False),
    Column("data_id", String(36), ForeignKey("data.id", ondelete="CASCADE"), nullable=False),
    Column("created_at", DateTime, server_default=func.now(), nullable=False),
    Column("updated_at", DateTime, server_default=func.now(), onupdate=func.now()),
    Column("access_level", String(20), server_default="read", nullable=False),
    
    # Add unique constraint to prevent duplicate user-data relationships
    UniqueConstraint('user_id', 'data_id', name='uq_user_data')
)

user_files = Table(
    "user_files",
    metadata,
    Column("id", String(36), primary_key=True, default=generate_uuid),
    Column("user_id", String(36), ForeignKey("users.id", ondelete="CASCADE"), nullable=False),
    Column("file_id", String(36), ForeignKey("data.id", ondelete="CASCADE"), nullable=False),
    Column("file_name", String(255), nullable=False),
    Column("file_path", String(512), nullable=False),
    Column("file_size", Integer, nullable=False),
    Column("mime_type", String(128), nullable=False),
    Column("created_at", DateTime, server_default=func.now(), nullable=False),
    Column("updated_at", DateTime, server_default=func.now(), onupdate=func.now()),
    Column("last_accessed", DateTime),
    Column("is_being_used", Boolean, server_default="false", nullable=False),
    Column("checksum", String(64)),  # For file integrity verification
    
    # Add constraints
    CheckConstraint('file_size > 0', name='file_size_check'),
    UniqueConstraint('user_id', 'file_path', name='uq_user_filepath')
)

metadata.create_all(engine)