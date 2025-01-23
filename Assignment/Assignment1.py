# Here will be the code for Assignment 1
#

# %% User Input
user_input = input("Enter something: ")
print(f"You entered: {user_input}")

# %% String Formatting
name = "Alice"
age = 30
print(f"{name} is {age} years old")  # f-string
print("{} is {} years old".format(name, age))  # .format() method
print("%s is %d years old" % (name, age))  # % formatting

# %% String Assignment
greeting = "Hello, World!"
substring = greeting[0:5]  # Slicing
length = len(greeting)

# %% Lists
fruits = ["apple", "banana", "cherry"]
fruits.append("date")  # Add item
fruits.remove("banana")  # Remove item
sorted_fruits = sorted(fruits)  # Sort list

# %% Sets and Tuples
unique_set = {1, 2, 3, 4}
coordinates = (10, 20)  # Immutable

# %% Booleans and Operators
is_true = True
x, y = 5, 3
result = x > y and is_true

# %% Conditional Statements
if x > y:
   print("x is greater")
elif x < y:
   print("y is greater")
else:
   print("x and y are equal")

# %% Loops
for item in fruits:
   print(item)

i = 0
while i < 5:
   print(i)
   i += 1