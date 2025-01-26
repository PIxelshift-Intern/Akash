# here all the decorators are defined (that are to be used in the fastApi/main.py file)

# transactions will be looked upon tomorrow(jan 27, 2025 Monday)
def transaction(func):
    """
    This is a decorator function to handle the transaction
    """
    def wrapper(*args, **kwargs):
        """
        This is a wrapper function to handle the database transaction
        """
        print("Transaction started")
        func(*args, **kwargs)
        print("Transaction completed")
    return wrapper