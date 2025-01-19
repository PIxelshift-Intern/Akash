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

# Inorder for it to not change the type of the variable we can use the type hinting
strict_name: str = "Akash"
