# list
example_list = [1, 2, 3, 4, 5]

# tuple
example_tuple = (1, 2, 3, 4, 5)

# set
example_set = {1, 2, 3, 4, 5}


# Operations in collections

# List
# Access elements
first_element = example_list[0]
last_element = example_list[-1]

# Add elements
example_list.append(6)  # Adds 6 at the end
example_list.insert(2, 99)  # Inserts 99 at index 2

# Remove elements
example_list.remove(3)  # Removes the first occurrence of 3
removed_element = example_list.pop(2)  # Removes and returns the element at index 2
example_list.clear()  # Clears the list

# Check if an element exists
is_present = 4 in example_list

# Iterate over elements
for item in example_list:
    print(item)

# Better way for iterating
items = [item for item in example_list] # this is rather faster than the above one
elements = list(example_set)  # this is rather faster than the above one

# Length of list
length = len(example_list)


# Tuple
# Access elements
first_element = example_tuple[0]
last_element = example_tuple[-1]

# Check if an element exists
is_present = 3 in example_tuple

# Iterate over elements
for item in example_tuple:
    print(item)

# Length of tuple
length = len(example_tuple)

# Count occurrences of an element
count = example_tuple.count(2)

# Find index of an element
index = example_tuple.index(3)


# Set
# Add elements
example_set.add(6)

# Remove elements
example_set.remove(4)  # Raises KeyError if element is not found
example_set.discard(4)  # Does not raise an error if element is not found
example_set.clear()  # Clears the set

# Check if an element exists
is_present = 3 in example_set

# Set operations
another_set = {3, 4, 5, 6}
union_set = example_set.union(another_set)  # Union of sets
intersection_set = example_set.intersection(another_set)  # Intersection of sets
difference_set = example_set.difference(another_set)  # Difference of sets

# Iterate over elements
for item in example_set:
    print(item)

elements = {item for item in example_set} 
Set_elemts = set(example_set)  # this will sort the duplicate elements and remove them only unique elements will be there

# Length of set
length = len(example_set)


# %% [markdown]
# Dict

# %%
# Access elements
# dict
example_dict = {
    "name": "Akash",
    "age": 20
}


name = example_dict["name"]
age = example_dict.get("age")  # Safe access, returns None if key is not found

# Add or update elements
example_dict["city"] = "Kathmandu"  # Adds a new key-value pair
example_dict["age"] = 21  # Updates the value of an existing key

# Remove elements
removed_value = example_dict.pop("age", None)  # Removes and returns value of "age", None if not found

# Check if a key exists
is_present = "name" in example_dict

# Iterate over keys, values, or items
for key in example_dict.keys():
    print(key)

for value in example_dict.values():
    print(value)

for key, value in example_dict.items():
    print(key, value)

example_dict.clear()  # Clears the dictionary

# Length of dictionary
length = len(example_dict)
print(length)


# %% [markdown]
