# FastAPI Guide

## Prerequisites
Before beginning, it is essential to have knowledge of:
1. **Standard HTTP headers format and contents**
2. **How an HTTP (REST API) request works**
3. **OAuth2**
4. **JWT (JSON Web Tokens)**
5. **FastAPI**
6. **Pydantic**
7. **SQLAlchemy**

---

## Introduction
FastAPI is a modern, fast (high-performance) web framework for building APIs with Python 3.6+ based on standard Python type hints. It is built on top of Starlette for the web parts and Pydantic for the data parts. FastAPI is designed to be easy to use and learn while offering robust performance and features.

### Key Features
- **Fast**: Very high performance, comparable to Node.js and Go, leveraging Starlette and Pydantic. It is one of the fastest Python frameworks available.
- **Fast to Code**: Development speed increases by 200% to 300%.*
- **Fewer Bugs**: Reduces approximately 40% of human (developer) induced errors.*
- **Intuitive**: Excellent editor support with features like autocompletion and type hints.
- **Standards-based**: Fully compatible with OpenAPI (formerly Swagger) and JSON Schema.

---

## Installation
To start using FastAPI, install it using `pip`:

```bash
pip install fastapi
pip install uvicorn
```

`uvicorn` is an ASGI server implementation, used to run the FastAPI application.

---

## Creating a FastAPI App
Below is an example of a simple FastAPI app:

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}
```

Save this file as `main.py`.

---

## Running the FastAPI App
Run the app using `uvicorn`:

```bash
uvicorn main:app --reload
```

The `--reload` flag enables auto-reloading for development, so the server restarts when you make changes to the code.

Once the server starts, you can access the API at `http://127.0.0.1:8000/`.

---

## Standard HTTP Headers
HTTP headers let the client and the server pass additional information with an HTTP request or response. Each header consists of a case-insensitive name followed by a colon (`:`) and its value. Whitespace before the value is ignored.

### Common HTTP Headers
- **`Accept`**: The MIME types that the client can understand.
- **`Accept-Language`**: The natural languages that the client can understand.
- **`Accept-Charset`**: The character sets that the client can understand.
- **`Accept-Encoding`**: The encoding that the client can understand.
- **`Authorization`**: Contains the credentials to authenticate a user agent with a server.
- **`Content-Type`**: The MIME type of the body of the request (used with POST and PUT requests).
- **`User-Agent`**: Contains information about the user agent making the request.
- **`Cache-Control`**: Specifies directives for caching mechanisms.
- **`Connection`**: Controls whether the network connection stays open after the transaction.
- **`Cookie`**: Contains stored HTTP cookies sent by the server.
- **`Host`**: Specifies the domain name of the server.
- **`Referer`**: Contains the address of the previous web page from which a link was followed.
- **`Server`**: Contains information about the software used by the server.
- **`Set-Cookie`**: Sends cookies from the server to the client.
- **`X-Forwarded-For`**: Contains the originating IP address of a client connecting through a proxy.

---

## How an HTTP Request Works
An HTTP request is a message sent from the client to the server. It consists of the following parts:

1. **Request Line**: Contains the HTTP method (e.g., GET, POST), URL, and protocol version.
2. **Headers**: Provide metadata about the request (e.g., content type, authorization).
3. **Body (Optional)**: Contains data sent to the server (e.g., form data, JSON).

### Example
A sample HTTP GET request:

```
GET /api/resource HTTP/1.1
Host: example.com
Authorization: Bearer <token>
Accept: application/json
```

---

## OAuth2
OAuth 2.0 is the industry-standard protocol for authorization. It focuses on simplicity for client developers while providing specific authorization flows for various application types, including web apps, desktop apps, and mobile apps.

### Key Components
1. **Authorization Server**: Issues tokens after authentication.
2. **Resource Server**: Hosts the protected resources and validates access tokens.
3. **Client**: The application requesting access on behalf of the user.
4. **Resource Owner**: The user granting permissions.

---

## JWT (JSON Web Tokens)
JWT is an open standard (RFC 7519) that defines a compact and self-contained way of securely transmitting information as a JSON object. JWTs are used for:

1. **Authentication**: Validating user identity.
2. **Authorization**: Granting access to resources.

### Structure of a JWT
1. **Header**: Contains metadata about the token (e.g., algorithm, token type).
2. **Payload**: Contains the claims (e.g., user data, permissions).
3. **Signature**: Ensures the token's integrity and authenticity.

### Example JWT
```
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9
.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ
.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c
```

---

## Pydantic
Pydantic is a Python library for data validation and settings management using Python type annotations. It:

- Validates data at runtime.
- Converts input data into expected formats.

### Example
```python
from pydantic import BaseModel

class User(BaseModel):
    id: int
    name: str
    email: str

user = User(id=1, name="John Doe", email="john@example.com")
print(user.dict())
```

---

## SQLAlchemy
SQLAlchemy is a Python SQL toolkit and Object-Relational Mapper (ORM) that provides powerful database management capabilities.

### Key Features
- Comprehensive ORM for working with database tables as Python objects.
- Support for raw SQL queries.

### Example
```python
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)

engine = create_engine('sqlite:///example.db')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

new_user = User(name="Jane Doe", email="jane@example.com")
session.add(new_user)
session.commit()
```

---

## Conclusion
FastAPI, combined with supporting libraries like Pydantic and SQLAlchemy, provides a powerful and efficient framework for building robust APIs. By understanding key concepts such as HTTP headers, OAuth2, and JWT, you can leverage FastAPI to create secure, high-performance applications.
