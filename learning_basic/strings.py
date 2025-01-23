# %% Strings in Python
# Strings are immutable in Python
# Once assigned, the values of a string cannot be changed, but the reference can be updated.

# Example of changing reference:
name = "Akash"
name = "Kafle"  # Updates the reference from "Akash" to "Kafle"

# Attempting to change the value will throw an error:
# name[0] = "B"  # Uncommenting this line will cause an error.

# %% String Operations

def string_operations():
    # Concatenation
    first_name = "Akash"
    last_name = "Kafle"
    full_name = first_name + " " + last_name
    print("Full Name:", full_name)
    
    # Multiplication
    name = "Akash"
    name_repeated = name * 3
    print("Repeated Name:", name_repeated)
    
    # Formatting
    age = 20
    formatted_string = "My name is {} and I am {} years old".format(first_name, age)
    print("Formatted String (using format):", formatted_string)
    
    formatted_string_f = f"My name is {first_name} and I am {age} years old"
    print("Formatted String (using f-string):", formatted_string_f)

string_operations()

# %% Membership Operators
def membership_operations():
    name = "Akash"
    
    # Checking substring presence
    if "Ak" in name:
        print("'Ak' is present in the name")
    else:
        print("'Ak' is not present in the name")
    
    # Checking substring absence
    if "Zy" not in name:
        print("'Zy' is not present in the name")
    else:
        print("'Zy' is present in the name")

membership_operations()

# %% String Properties
def string_properties():
    name = "Akash"
    
    # Length of the string
    length = len(name)
    print("Length of name:", length)
    
    # Indexing
    first_character = name[0]
    last_character = name[-1]
    print("First Character:", first_character)
    print("Last Character:", last_character)
    
    # Slicing
    first_three_characters = name[:3]
    last_three_characters = name[-3:]
    print("First Three Characters:", first_three_characters)
    print("Last Three Characters:", last_three_characters)
    
    # Step in slicing
    alternate_characters = name[::2]
    reverse_name = name[::-1]
    print("Alternate Characters:", alternate_characters)
    print("Reversed Name:", reverse_name)

string_properties()


# %% String Conversion
def string_conversion():
    # Convert integer to string
    a = 10
    b = str(a)
    print("Converted Integer to String:", b)
    
    # Convert float to string
    a = 10.5
    b = str(a)
    print("Converted Float to String:", b)
    
    # Convert list to string using join()
    example = [1, 2, 3, 4, 5]
    joined_string = ' '.join(map(str, example))
    print("Joined List as String:", joined_string)

string_conversion()
