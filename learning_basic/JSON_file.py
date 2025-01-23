# %% File Handling
def file_operations():
   """Demonstrate read and write operations"""
   # Writing to a file
   with open('example.txt', 'w') as file:
       file.write("Hello, File Handling!")
   
   # Reading from a file
   with open('example.txt', 'r') as file:
       content = file.read()
   
   return content

# %% JSON Handling
import json

def json_operations() -> dict:
   """Demonstrate JSON encoding and decoding"""
   data = {"name": "John", "age": 30}
   json_string = json.dumps(data)
   return json.loads(json_string)
