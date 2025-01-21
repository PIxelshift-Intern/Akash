##
# 
# This is for learning about the variables and how they work in python
#  
# 
# #

# random example
name = "Akash"
age = 20

# Here name is a string and age is an integer
# We don't need to specify the type of the variable in python, it will be automatically inferred in the runtime by the python interpreter
# We can also change the type of the variable during the runtime
print(name)
name = 20 # this will change the type of the variable name from string to integer
print(name)

# We can also specify the type of the variable explicitly
name_: str = "Akash"
age_: int = 20

# We can also assign multiple variables in a single line
name, age = "Akash", 20

# We can also assign the same value to multiple variables
name = age = "Akash"

# there are standard types for the variables in python
# int, float, complex, str, bool, (list, tuple, set, dict)=> will be in the next file `Collections.py`

# int 
example_int = 10

# float
example_float = 10.5

# complex
example_complex = 10 + 5j

# str
example_str = "Hello World"

# bool
example_bool = True


# all the above variables are mutable variables, using pep8 naming convention we should use snake_case for the variable names
# int
EXAMPLE_INT = 10 # this is a constant variable(sort of can still be changed but due to the naming convention it is considered as a constant)

# also python is case sensitive so EXAMPLE_INT and example_int are different variables

# adding two numbers
a = 10
b = 20
c = a + b

# same for complex numbers
a = 10 + 5j
b = 20 + 5j
c = a + b     # will be in the same format as complex numbers


