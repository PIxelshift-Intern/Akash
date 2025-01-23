# import libraries
# import `file_name`(must be in the same directory)
# import `module_name`(must be in the same directory)
# import `module_name` as `alias`
# from `module_name` import `function_name`
# from `module_name` import `function_name` as `alias`
# from `module_name` import *
# import `main_module`.`sub_module`.`module_name` (nested module {we need to specify the path})


# %% OOP Concepts

# Base Class: Modeling a Person with Comprehensive OOP Features
class Person:
   # Class Attribute: Shared across all instances
   # Represents a common characteristic of the entire class
   species = "Homo Sapiens"

   # Constructor: Initialize object with essential attributes
   def __init__(self, name: str, age: int):
       # Instance Attributes: Unique to each object
       # Protected attributes (convention: single underscore)
       # Indicates these should not be directly accessed outside the class
       self._name = name  # Encapsulation of name
       self._age = age    # Encapsulation of age
       self._health = 100  # Additional private attribute

   # Instance Method: Basic behavior of a person
   def introduce(self):
       """
       Generate a personal introduction
       Demonstrates method behavior specific to each instance
       """
       return f"I'm {self._name}, {self._age} years old"

   # Property Decorator: Controlled attribute access
   # Provides getter with additional logic
   @property
   def age(self):
       """
       Getter for age
       Allows read-only or controlled access to private attribute
       """
       return self._age

   # Property Setter: Validate before setting attribute
   @age.setter
   def age(self, value: int):
       """
       Setter for age with validation
       Prevents invalid age assignments
       """
       if 0 < value < 120:
           self._age = value
       else:
           raise ValueError("Invalid age")

   # Class Method: Alternative constructor
   # Creates an object without requiring all parameters
   @classmethod
   def create_anonymous(cls):
       """
       Alternative constructor for creating a default/anonymous person
       Demonstrates flexible object creation
       """
       return cls("Anonymous", 0)

   # Static Method: Utility function not dependent on instance state
   @staticmethod
   def is_adult(age: int) -> bool:
       """
       Determine if a person is an adult based on age
       Independent of any specific instance
       """
       return age >= 18

# Inheritance: Extending base class with specialized behavior
class Employee(Person):
   def __init__(self, name: str, age: int, job: str, salary: float):
       # Call parent constructor using super()
       super().__init__(name, age)
       
       # Additional attributes specific to Employee
       self.job = job
       self._salary = salary

   # Method Overriding: Customize parent class method
   def introduce(self):
       """
       Override parent's introduce method
       Adds job information to the introduction
       Demonstrates polymorphic behavior
       """
       return f"{super().introduce()}, works as {self.job}"

   # Unique method for Employee
   def calculate_annual_income(self):
       """
       Calculate total annual income
       Demonstrates class-specific method
       """
       return self._salary * 12

# Abstract Base Class: Define interface for shape calculations
from abc import ABC, abstractmethod

class Shape(ABC):
   @abstractmethod
   def area(self):
       """
       Abstract method to enforce implementation in child classes
       Ensures all shapes must define their area calculation
       """
       pass

class Rectangle(Shape):
   def __init__(self, width: float, height: float):
       self.width = width
       self.height = height

   def area(self):
       """
       Concrete implementation of area for rectangles
       Demonstrates implementation of abstract method
       """
       return self.width * self.height

# Polymorphism Demonstration
def print_introduction(person):
   """
   Function showing polymorphic behavior
   Can work with different types of person-like objects
   """
   print(person.introduce())

# Practical Usage Examples
def main():
   # Create different types of objects
   generic_person = Person("Alice", 30)
   tech_worker = Employee("Bob", 35, "Software Developer", 5000)
   anonymous_person = Person.create_anonymous()

   # Demonstrate various OOP concepts
   print(generic_person.introduce())  # Basic introduction
   print(tech_worker.introduce())     # Overridden introduction
   print(f"Bob's annual income: ${tech_worker.calculate_annual_income()}")
   
   # Polymorphism in action
   print_introduction(generic_person)
   print_introduction(tech_worker)

   # Demonstrate property and validation
   try:
       tech_worker.age = 150  # This will raise a ValueError
   except ValueError as e:
       print(f"Age validation error: {e}")

# Run the demonstration
if __name__ == "__main__":
   main()
# %%
