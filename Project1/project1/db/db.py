# this is to be used for connection with postgres database
# I will be using sqlalchemy

from sqlalchemy import create_engine
import os

engine = create_engine(f'postgresql://{os.environ.get("POSTGRES_USER")}:{os.environ.get("POSTGRES_PASSWORD")}@postgres_db_Project1:5432/{os.environ.get("POSTGRES_DB")}')

def get_engine():
    try:
        engine.connect()
    except Exception as e:
        return (None, e)
    
    return (engine, None)