# %% Collection Types
# List, Tuple, Set, and Dictionary Operations

# %% List
example_list = [1, 2, 3, 4, 5]

# List Operations
def list_operations():
   # Accessing Elements
   first = example_list[0]
   last = example_list[-1]

   # Modifying List
   example_list.append(6)  # Add to end
   example_list.insert(2, 99)  # Insert at specific index
   example_list.remove(3)  # Remove first occurrence
   
   # Advanced List Comprehension
   items = [item for item in example_list]
   elements = list(set(example_list))  # Remove duplicates

   print("First: ", first, "\nLast: ", last)
   print("Items: ", items, "\nElements: ", elements)
   
   # Checking and Iterating
   is_present = 4 in example_list
   print("Is Present: ", is_present)
   for item in example_list:
       print(item)

# List comprehension with print
print(*[item for item in example_list])
# Output: 1 2 3 4 5

list_operations()

# %% Tuple
example_tuple = (1, 2, 3, 4, 5)

def tuple_operations():
   # Accessing Elements
   first = example_tuple[0]
   last = example_tuple[-1]
   print("First: ", first, "\nLast: ", last)

   # Tuple-Specific Methods
   count = example_tuple.count(2)
   index = example_tuple.index(3)
   print("Count: ", count, "\nIndex: ", index)

   # Checking and Iterating
   is_present = 3 in example_tuple
   print("Is Present: ", is_present)
   for item in example_tuple:
       print(item)

tuple_operations()

# %% Set
example_set = {1, 2, 3, 4, 5}

def set_operations():
   # Modifying Set
   example_set.add(6)
   example_set.discard(4)  # Safe removal

   # Set Combinations
   another_set = {3, 4, 5, 6}
   union_set = example_set.union(another_set)
   intersection_set = example_set.intersection(another_set)
   difference_set = example_set.difference(another_set)

   # Unique Element Extraction
   elements = {item for item in example_set}
   unique_elements = set(example_set)

   print("union: ",union_set,"\nIntersection_set: ", intersection_set,"\nDifference_Set: ", difference_set)
   print("Elements: ", elements)
   print("Unique Elements: ", unique_elements)

set_operations()

# %% Dictionary
example_dict = {"name": "Akash", "age": 20}

def dict_operations():
   # Accessing and Modifying
   name = example_dict["name"]
   age = example_dict.get("age")  # Safe access
   example_dict["city"] = "Kathmandu"  # Add/Update

   # Removal
   removed_value = example_dict.pop("age", None)
   print("Name: ", name, "\nAge: ", age, "\nRemoved Value: ", removed_value)

   # Iteration Techniques
   for key in example_dict.keys():
       print(key)
   
   for value in example_dict.values():
       print(value)
   
   for key, value in example_dict.items():
       print(key, value)

dict_operations()