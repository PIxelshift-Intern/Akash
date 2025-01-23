##
# This script demonstrates variables and how they work in Python.
#

# %% Variable Examples
# Random example
name = "Akash"
age = 20

# Here, 'name' is a string and 'age' is an integer.
# Python automatically infers the type of variables at runtime.
# We can also change the type of a variable during runtime.
print(name)
name = 20  # Changes the type of 'name' from string to integer.
print(name)

# Explicitly specifying the type of a variable (optional in Python):
name_: str = "Akash"
age_: int = 20

# Assigning multiple variables in a single line:
name, age = "Akash", 20

# Assigning the same value to multiple variables:
name = age = "Akash"

# %% Standard Variable Types
# Standard types in Python:
# int, float, complex, str, bool, (list, tuple, set, dict - will be covered in Collections.py)

# Integer
example_int = 10

# Float
example_float = 10.5

# Complex
example_complex = 10 + 5j

# String
example_str = "Hello World"

# Boolean
example_bool = True

# Variables are mutable. Using PEP 8 naming conventions, we should use snake_case for variable names.
# Constant variable (by naming convention, not enforced):
EXAMPLE_INT = 10  # Still mutable, but considered a constant due to naming convention.

# Python is case-sensitive, so EXAMPLE_INT and example_int are different variables.

# %% Adding Numbers
# Adding two integers:
a = 10
b = 20
c = a + b

# Adding two complex numbers:
a = 10 + 5j
b = 20 + 5j
c = a + b  # Result is in the complex number format.

# %% Type Conversions
# Converting one type of variable to another:

# Integer to float:
a = 10
b = float(a)

# Float to integer:
a = 10.5
b = int(a)

# Integer to complex:
a = 10
b = complex(a)

# Float to complex:
a = 10.5
b = complex(a)

# Complex to integer or float:
# This will raise an error because complex numbers cannot be directly converted.

# String to integer:
a = "10"
b = int(a)  # Works if the string is numeric.
# Example:
# a = "a"  # Uncommenting this will raise ValueError: invalid literal for int() with base 10.

# String to float:
# Similar behavior as above for numeric strings.

# String conversions are further explored in 'strings.py'.

# %% Function Example for Execution

def demonstrate_variables():
    """Function to demonstrate variable operations."""
    # Integer addition
    a = 10
    b = 20
    c = a + b
    print("Sum of integers:", c)

    # Complex addition
    a = 10 + 5j
    b = 20 + 5j
    c = a + b
    print("Sum of complex numbers:", c)

    # Type conversion examples
    a = 10
    b = float(a)
    print("Integer to float:", b)

    a = "10"
    b = int(a)
    print("String to integer:", b)

# Execute the function
demonstrate_variables()

# %%
