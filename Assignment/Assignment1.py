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
reversing = greeting[::-1]  # Reversing
length = len(greeting)
print("Substring:", substring)
print("Length:", length)
print("Reversed:", reversing)

# %% Lists
fruits = ["apple", "banana", "cherry"]
fruits.append("date")  # Add item
fruits.remove("banana")  # Remove item
sorted_fruits = sorted(fruits)  # Sort list
print("Sorted fruits: ", sorted_fruits)

# List Comprehension
numbers = [1, 2, 3, 4, 5]
squared = [x**2 for x in numbers]
evens = [x for x in numbers if x % 2 == 0]
print("Squared: ", squared)
print("Evens: ", evens)

def iterate_list():
   """
   This is for showing how to iterate over a list.
   There are multiple ways to do this.
   """

    # Using range
   for item in fruits:
      print(item)

   # Using enumerate
   for index, item in enumerate(fruits):
        print(index, item)
   
    # Using while loop
   i = 0
   while i < len(fruits):
        print(fruits[i])
        i += 1
    
    # Using list comprehension
   [print(item) for item in fruits]
   
   # Using Zip
   keys = ["a", "b", "c"]
   values = [1, 2, 3]

    # Iterate over two lists simultaneously
   for key, value in zip(keys, values):
        print(key, value)


# %% Sets and Tuples
unique_set = {1, 2, 3, 4}
coordinates = (10, 20)  # Immutable
x, y = coordinates
print(coordinates[0], coordinates[1])
print("x: ", x, "\ny: ", y)

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

# Assignments 2 and 3 are completed in learning basics 
# i realized that after completing this assignment(looked familiar and checked assignment 2 and 3)
# will be collecting the required code from there and pasting in each Assignment2.py and Assignment3.py