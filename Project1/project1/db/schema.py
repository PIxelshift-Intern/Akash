from sqlalchemy import MetaData, Table, Column, Integer, String, DateTime, ForeignKey, Boolean, JSON
from db.db import engine

metadata = MetaData()

users = Table(
    "users",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("username", String, unique=True),
    Column("password", String),
    Column("email", String, unique=True),
    Column("created_at", DateTime),
    Column("updated_at", DateTime),
    Column("Verified", Boolean, default=False),
    Column("is_Active", Boolean, default=False),
)

data = Table(
    "data",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("data", JSON),
)


User_data = Table(
    "User_data",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("user_id", Integer, ForeignKey("users.id")),
    Column("data_id", Integer, ForeignKey("data.id")),
    Column("created_at", DateTime),
    Column("updated_at", DateTime),
)

metadata.create_all(engine)

# will add other tables as needed(haven't thought of yet)
