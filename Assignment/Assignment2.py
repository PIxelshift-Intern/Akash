# %% Default Dictionaries
from collections import defaultdict

def default_dict_example():
    """
    Default dictionaries in Python.
    These dictionaries have a default value for keys that have not been set.
    """
    default_dict = defaultdict(int)
    default_dict["apple"] += 1  # Automatically initializes the value to 0 and adds 1
    print(default_dict)

default_dict_example()

# %% Ordered Dictionaries
from collections import OrderedDict

def ordered_dict_example():
    """
    Ordered dictionaries in Python.
    These dictionaries maintain the order of insertion of keys.\n
    That is, the order of keys is the same as the order in which they were inserted.
    """
    ordered = OrderedDict()
    ordered["first"] = 1
    ordered["second"] = 2
    print(ordered)

ordered_dict_example()

# %% Dictionary Comprehension
def dict_comprehension_example():
    """
    Dictionary comprehension in Python.
    This is similar to list comprehension but for dictionaries.
    """
    squares = {x: x**2 for x in range(5)}
    print(squares)

dict_comprehension_example()

# %% Merging Dictionaries
def merge_dicts_example():
    """
    Merge two dictionaries in Python.
    """
    dict1 = {"a": 1, "b": 2}
    dict2 = {"b": 3, "c": 4}

    # Using `update`
    dict1.update(dict2)
    print("Using update:", dict1)

    # Using `|` operator (Python 3.9+)
    merged = dict1 | dict2
    print("Using | operator:", merged)

merge_dicts_example()

# %% View Objects
def view_objects_example():
    """
    View objects provide a dynamic view on the dictionary's keys, values, or items.
    """
    d = {"a": 1, "b": 2}
    keys_view = d.keys()

    d["c"] = 3  # Modifying dictionary
    print("Keys View:", list(keys_view))  # Reflects change

view_objects_example()

# %% Sorting Dictionaries
def sort_dict_example():
    """
    Sorting dictionaries in Python.
    This can be done by sorting by keys or values.
    """

    d = {"c": 3, "a": 1, "b": 2}

    # Sort by keys
    sorted_by_keys = dict(sorted(d.items()))
    print("Sorted by keys:", sorted_by_keys)

    # Sort by values
    sorted_by_values = dict(sorted(d.items(), key=lambda item: item[1]))
    print("Sorted by values:", sorted_by_values)

sort_dict_example()

# %% Nested Dictionaries
def nested_dict_example():
    """
    Nested dictionaries in Python.
    These are dictionaries within a dictionary.
    """
    nested = {"user": {"name": "Akash", "age": 20}}
    print(nested["user"]["name"])  # Accessing nested values

nested_dict_example()

# %% Advanced Iteration
from itertools import islice

def advanced_iteration_example():
    """
    Advanced iteration techniques in Python.
    Here, we use `islice` to iterate over the first N items of a dictionary.
    """
    d = {"a": 1, "b": 2, "c": 3}

    # Iterate first N items
    for key, value in islice(d.items(), 2):
        print(key, value)
    


advanced_iteration_example()