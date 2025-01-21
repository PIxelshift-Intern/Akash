# Conditionals in pythons are
# if, elif, else

# if statement
if 5 > 2:
    print("5 is greater than 2")

# if else statement
if 5 < 2:
    print("5 is less than 2")
else:
    print("5 is not less than 2")

# if elif else statement
a= 5
b = 2
if a < b:
    print("5 is less than 2")
elif a > b:
    print("5 is greater than 2")
else:
    print("5 is equal to 2")

# we can also use the and, or, not operators in the conditionals
a = 5
b = 2
c = 3
if a > b and a > c: # will do what is said 
    print("a is the greatest number")
elif b > a and b > c:
    print("b is the greatest number")
else:
    print("c is the greatest number")

# we can also use the or operator
a = 5
b = 2
c = 3
if a > b or a > c: # will do what is said 
    print("a is the greatest number")
elif b > a or b > c:
    print("b is the greatest number")
else:
    print("c is the greatest number")

# we can also use the not operator
a = 5
b = 2
c = 3
if not a < b: 
    print("a is not less than b")
else:
    print("a is less than b")

# loops in python
# (we should leverage the power of list, tuple, set, dict to iterate over the elements)
# only if they are unavoidable we should use the loops

# for loop
# for loop is used to iterate over the elements of a sequence
# for example

a = [1, 2, 3, 4, 5]
for i in a:
    print(i)

# we can also use the range function to iterate over the elements
for i in range(5):
    print(i)

# we can also use the break statement to break out of the loop when `break` is encountered
for i in range(5):
    if i == 3:
        break
    print(i)

# we can also use the continue statement to skip the current iteration when `continue` is encountered
for i in range(5):
    if i == 3:
        continue
    print(i)


# while loop
# while loop is used to iterate over the elements until the condition is true
# for example
i = 0
while i < 5:
    print(i)
    i += 1

# we can also use the break statement to break (same as above)
# we can also use the continue statement to skip the current iteration (same as above)

# we can also use the else statement with the loops
# the else block will be executed when the loop is exhausted

for i in range(5):
    print(i)
else:
    print("Loop is exhausted")

# we can also use the else block with the while loop

