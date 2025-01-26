##
# This is just for leaning basics of FastAPI
# this is a simple example of FastAPI
# A more standard use of FastAPI will be done through in another folder `Project`
# This folder `project` will contain a more complex example of FastAPI 
# and will have very deep usage as well as the use of database and other stuffs(like JWT, etc)
# 
# Here we are just learning the basics of FastAPI (like how to create a simple API {REST API=> GET, POST, PUT, DELETE}) 
# #


from fastapi import FastAPI, HTTPException

app = FastAPI()

# GET request
# This is basically used for getting the data from the server
# Get request has no body, it only has the path parameters and query parameters
# but creds can be passed through headers ( Quite important for authentication)
# we need to parse the standard headers for the authentication

# This is a simple example of FastAPI
@app.get("/")
async def root():
    """
    Standard Hello World with path `/`\n
    passing a message `Hello World` to the frontend with json response
    """

    return {"message": "Hello World"}

# This is a simple example of FastAPI
@app.get("/items/{item_id}")
async def read_item(
      item_id: int, q: str = None):
    """
    Parameters are for:
    item_id: int => this is used for item identification
    q: str = None => this is a query parameter(user search option)
    """
    return {"message": f'The {item_id} is selected', "q": q}

# This is a simple example of FastAPI
@app.get("/users/{user_id}")
async def read_user_me(
      user_id: str, q: str = None):
    """
    Parameters are for:
    user_id: str => this is used for user identification
    q: str = None => this is a query parameter(user search option)
    """


    return {"message": f"the current user has user id `{user_id}`", "q": q}

# this is to show different use of path parameters
@app.get("/users/{user_id}/items/{item_id}") 
async def read_user_item(
      user_id: int, item_id: int, 
      q: str = None):

    return {"message": f"the user {user_id} has selected item {item_id}", "q": q}

from functions import read_database, write_database, log
from datetime import datetime
import json
from typing import Optional, Dict



app = FastAPI()

@app.get("/api/{user}/{item_id}")
async def items_retrieve(
        item_id: int, 
        user: str,
        q: Optional[str] = None
):
    """
    Retrieve a specific item from the database
    - Finds item by item_id
    - Supports optional query parameter
    - Implements error handling
    """
    # same for the authentication check
    # AuthCheck(user) # this is to be replaced with the actual authentication check( i am using this as a example)
    # more advance authentication will be done further into the project

    try:
        # Read the entire database
        database = read_database()
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="Database not found")
    except json.JSONDecodeError:
        raise HTTPException(status_code=500, detail="Database is corrupted")

    # Find the specific item
    item = next((item for item in database if item['item_id'] == item_id), None)
    
    # Check if item exists
    if not item:
        raise HTTPException(status_code=404, detail=f"Item {item_id} not found")
    
    # Optional authorization check
    if 'user_id' in item and item['user_id'] != user:
        raise HTTPException(status_code=403, detail="Not authorized to view this item")

    return {
        "message": f"Item {item_id} retrieved successfully", 
        "item": item, 
        "query_param": q
    }

# POST request - Create a new item
@app.post("/api/{user_id}/{item_id}")
async def items_create(
        user_id: str, 
        item_id: int, 
        q: Optional[str] = None, 
        item_data: Optional[Dict] = None
):
    """
    Create a new item in the database
    - Checks if item already exists
    - Adds timestamp and user information
    - Supports optional additional item data
    """
    # Check if item_id and user_id are valid
    # AuthCheck(user_id) # this is to be replaced with the actual authentication check( i am using this as a example)
    # more advance authentication will be done further into the project

    # Read existing database
    database = read_database()
    
    # Check if item already exists
    if any(item['item_id'] == item_id for item in database):
        raise HTTPException(status_code=400, detail=f"Item {item_id} already exists")
    
    # Prepare item data
    new_item = {
        "item_id": item_id,
        "user_id": user_id,
        "message": f"New item {item_id} created",
        "timestamp": datetime.now(),
        "additional_data": item_data or {}
    }
    
    # Add to database
    database.append(new_item)

    # Keeping log of created items
    log("Created item", new_item)
    
    # Write updated database
    write_database(database)

    return {
        "message": f"Item {item_id} successfully created", 
        "item": new_item,
        "query_param": q
    }

# PUT request - Update an existing item
@app.put("/api/{user_id}/{item_id}")
async def items_update(
        user_id: str, 
        item_id: int, 
        q: Optional[str] = None, 
        update_data: Optional[Dict] = None
):
    """
    Update an existing item in the database
    - Finds the item by item_id
    - Merges new data with existing item
    - Adds update timestamp
    """
    # additional params can be added to this item_update function for creds and other stuffs(as per the requirement)
    # Check if item_id and user_id are valid
    # AuthCheck(user_id) # this is to be replaced with the actual authentication check( i am using this as a example)
    # more advance authentication will be done further into the project


    # Read existing database
    database = read_database()
    
    # Find the item to update
    item_to_update = None
    for index, item in enumerate(database):
        if item['item_id'] == item_id:
            item_to_update = index
            break
    
    # Raise error if item not found
    if item_to_update is None:
        raise HTTPException(status_code=404, detail=f"Item {item_id} not found")
    
    # Update the item
    existing_item = database[item_to_update]
    existing_item['message'] = f"Item {item_id} updated"
    existing_item['updated_at'] = datetime.now()
    
    # Merge additional update data
    if update_data:
        existing_item['additional_data'] = {
            **existing_item.get('additional_data', {}),
            **update_data
        }
    
    # Ensure the user has permission to update
    if existing_item['user_id'] != user_id:
        raise HTTPException(status_code=403, detail="Not authorized to update this item")
    
    # Keeping log of updated items
    log("Updated item", existing_item)

    # Write updated database
    write_database(database)

    return {
        "message": f"Item {item_id} successfully updated", 
        "item": existing_item,
        "query_param": q
    }

# DELETE request - Delete an existing item
@app.delete("/api/{user_id}/{item_id}")
async def items_delete(
        user_id: str, 
        item_id: int, 
        q: Optional[str] = None
):
    """
    Delete an existing item from the database
    - Finds the item by item_id
    - Removes the item from the database
    """

    # additional params can be added to this item_update function for creds and other stuffs(as per the requirement)
    # Check if item_id and user_id are valid
    # AuthCheck(user_id) # this is to be replaced with the actual authentication check( i am using this as a example)
    # more advance authentication will be done further into the project


    # Read existing database
    database = read_database()
    
    # Find the item to delete
    item_to_delete = None
    for index, item in enumerate(database):
        if item['item_id'] == item_id:
            item_to_delete = index
            break
    
    # Raise error if item not found
    if item_to_delete is None:
        raise HTTPException(status_code=404, detail=f"Item {item_id} not found")
    
    # Ensure the user has permission to delete
    if database[item_to_delete]['user_id'] != user_id:
        raise HTTPException(status_code=403, detail="Not authorized to delete this item")
    
    # Delete the item
    deleted_item = database.pop(item_to_delete)

    # Keeping log of deleted items
    log("Deleted item", deleted_item)
    
    # Write updated database
    write_database(database)

    return {
        "message": f"Item {item_id} successfully deleted", 
        "item": deleted_item,
        "query_param": q
    }

# with this it concludes the basic example of FastAPI
# although post request is not checking authentication but it can be done by adding a middleware for auth check