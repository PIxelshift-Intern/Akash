# Conditionals in pythons are
# if, elif, else

a= 5
b = 2
# %% Conditional Statements
def conditional_examples():
   # Simple if statement
   if 5 > 2:
       print("5 is greater than 2")

   # If-else statement
   if 5 < 2:
       print("5 is less than 2")
   else:
       print("5 is not less than 2")

   # If-elif-else statement
   a, b, c = 5, 2, 3
   if a < b:
       print("5 is less than 2")
   elif a > b:
       print("5 is greater than 2")
   else:
       print("5 is equal to 2")

conditional_examples()

# %% Logical Operators
def logical_operator_examples():
   # AND operator
   if a > b and a > c:
       print("a is the greatest number")
   
   # OR operator
   if a > b or a > c:
       print("a is the greatest number")
   
   # NOT operator
   if not a < b:
       print("a is not less than b")

logical_operator_examples()

# %% Loops
def loop_examples():
   # For loop with list
   numbers = [1, 2, 3, 4, 5]
   for num in numbers:
       print(num)

   # Range-based for loop
   for i in range(5):
       print(i)

   # Break statement
   for i in range(5):
       if i == 3:
           break
       print(i)

   # Continue statement
   for i in range(5):
       if i == 3:
           continue
       print(i)

loop_examples()

# %% While Loop
def while_loop_example():
   # Basic while loop
   i = 0
   while i < 5:
       print(i)
       i += 1

while_loop_example()

# %% Loop with Else Clause
def loop_with_else():
   # For loop with else
   for i in range(5):
       print(i)
   else:
       print("Loop is exhausted")

loop_with_else()