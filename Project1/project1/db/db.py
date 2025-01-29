# this is to be used for connection with postgres database
# I will be using sqlalchemy

from sqlalchemy import create_engine
import os
from dotenv import load_dotenv
load_dotenv()  # Load .env file

host = os.environ.get('DB_HOST', 'localhost')  # Defaults to localhost if not in Docker

engine = create_engine(
    f"postgresql://{os.environ['POSTGRES_USER']}:{os.environ['POSTGRES_PASSWORD']}"
    f"@{os.environ.get('DB_HOST', 'localhost')}:5432/{os.environ['POSTGRES_DB']}",
    pool_size=10,
    max_overflow=5,
    pool_timeout=30,
    pool_recycle=1800,
)

def Transactions():
    """
    A decorator to handle database transactions. 
    - Starts a transaction automatically.
    - Commits on success, rolls back on error.
    - Passes the active connection to the decorated function.
    """
    def decorator(func):
        def wrapper(*args, **kwargs):
            # Use a context manager to handle the connection and transaction
            with engine.begin() as conn:
                # Inject the connection into the decorated function's kwargs
                kwargs['connection'] = conn
                # Execute the function within the transaction
                result = func(*args, **kwargs)
                # Transaction auto-commits if no exceptions, otherwise rolls back
                return result
            # Connection is automatically closed and returned to the pool
        return wrapper
    return decorator

from sqlalchemy import text

def get_data(table_name, columns='*', where_clause=None, params=None):
    """
    Retrieve data from the specified table with optional columns, filters, and parameters.

    Args:
        table_name (str): Name of the table to query.
        columns (str/list, optional): Columns to select. Defaults to '*'.
        where_clause (str, optional): WHERE conditions (exclude 'WHERE'). Defaults to None.
        params (dict, optional): Parameters for the query. Defaults to None.

    Returns:
        list: Query results as a list of tuples.
    """
    # Convert columns list to comma-separated string
    if isinstance(columns, (list, tuple)):
        columns = ', '.join(columns)

    # Build base query
    query = f"SELECT {columns} FROM {table_name}"

    # Add WHERE clause if specified
    if where_clause:
        query += f" WHERE {where_clause}"

    # Execute query with parameters
    with engine.connect() as conn:
        result = conn.execute(text(query), params or {})
        return result.fetchall()