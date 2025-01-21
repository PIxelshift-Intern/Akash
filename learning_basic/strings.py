# strings
# strings are immutable in python
# we can't change the values of the string once it is assigned
# but we can change the reference of the string
# for example
name = "Akash"
name = "Kafle" # this will change the reference of the string to "Kafle" from "Akash"
# but we can't change the value of the string
# for example
name = "Akash"
name[0] = "B" # this will throw an error

# operations in strings
# we can concatenate two strings using the + operator
first_name = "Akash"
last_name = "Kafle"
full_name = first_name + " " + last_name

# we can also multiply the string
name = "Akash"
name = name * 3 # this will multiply the string name 3 times eg. "AkashAkashAkash"

# we can also use the format method to format the string
name = "Akash"
age = 20
formatted_string = "My name is {} and I am {} years old".format(name, age)
# we can also use the f string to format the string
formatted_string = f"My name is {name} and I am {age} years old"

# we can also use the in operator to check if a substring is present in the string
name = "Akash"
if "Ak" in name:
    print("Ak is present in the name")
else:
    print("Ak is not present in the name")

# we can also use the not in operator to check if a substring is not present in the string
name = "Akash"
if "Ak" not in name:
    print("Ak is not present in the name")
else:
    print("Ak is present in the name")

# we can also use the len function to get the length of the string
name = "Akash"
length = len(name) # this will return 5 as `Akash` has 5 characters

# we can also use the indexing to get the character at a specific index
name = "Akash"
first_character = name[0] # this will return `A`
last_character = name[-1] # this will return `h`

# we can also use the slicing to get the substring
name = "Akash"
first_three_characters = name[:3] # this will return `Aka`
last_three_characters = name[-3:] # this will return `ash`

# we can also use the step in the slicing
name = "Akash"
alternate_characters = name[::2] # this will return `Aah`
reverse_name = name[::-1] # this will return `hsakA`
