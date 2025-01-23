# %% Function Definitions with Parameters
def greet(name: str, greeting: str = "Hello") -> str:
   """Greet a person with optional custom greeting"""
   return f"{greeting}, {name}!"

# %% Multiple Return Values
def calculate(x: int, y: int) -> tuple[int, int, int]:
   """Perform multiple calculations on two numbers"""
   return x + y, x - y, x * y

# %% Variable Arguments (*args and **kwargs)
def flexible_function(*args, **kwargs):
   """Handle variable positional and keyword arguments"""
   print("Positional arguments:", args)
   print("Keyword arguments:", kwargs)

flexible_function(1, 2, 3, name="John", age=30)

# %% Lambda Functions
multiply_by_ten = lambda a: a + 10
print(multiply_by_ten(5))  # Output: 15

def multiplier(n: int):
   """Create specialized multiplier functions"""
   return lambda a: a * n

double = multiplier(2)
triple = multiplier(3)

print(double(11))   # Output: 22
print(triple(11))   # Output: 33

# %% Built-in Functions
from functools import reduce

numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, numbers))
evens = list(filter(lambda x: x % 2 == 0, numbers))
sum_all = reduce(lambda x, y: x + y, numbers)

