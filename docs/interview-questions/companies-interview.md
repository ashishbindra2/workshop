# Companies Interviews experences

## infosis interview

1. implement model api
2. implement aoth and login api
3. pandas pdf manupulation
4. pandas data cleaing
5. pandas pdf view
6. show libreary
7. open source libray fetch and display

## L1 Interview|| Neosoft|| Python || 30 Oct 2025 3:30 Pm

- What are the set() and pop() functions in Python?
- What is Django ORM?
- What is FastAPI, and how does it compare to Flask? (Which is better and why?)
What is Django's architecture? (MVT pattern)
What are Docker Volumes?
What are Docker layers, and how do they work with Django?
What is the difference between deep copy and shallow copy in Python?
How do try and except work in Python? (Exception handling)
What is an ORM QuerySet in Django?
How does NumPy matrix multiplication work?
What is the difference between Pandas DataFrame and Series?
How to open and work with files in Python? (open() function)
What are Django Serializers?

## Exubers

1. Memory mangment in python
2. GIL
3. LLM use
4. project working
5. Threads in python, how its impemented
6. async in python
7. why fastapi is asyncronus how explain.
8. orm mapping
9. Garbage vs iterator

## Recro.io

0. logging module
1. message quese
2. event driven
3. distrubuted
4. metrix
5. monitoring
6. how radis is so fast
7. docker isolate from host
8. asynio usecase
9. async io
10. radis

11. ✅ Task:

    Build an endpoint:

    GET /config

    The system should load configuration settings from three levels, in this order (higher wins over lower):

    - Default settings (hardcoded in app).--3
    - Environment variables (read from os.environ).--2
    - Query parameters on the /config endpoint. --1

    For example, if the setting is DEBUG, the query param overrides the env var, which overrides the default.

    Return the final merged configuration as JSON.

12. How to write testcase in python

## Varaisys

### Q1. Flatten Nested List

**Task:**  
Write a Python function to flatten a nested list of arbitrary depth.

 Example

```python
Input:  [1, [2, [3, 4], 5], [6, 7]]
Output: [1, 2, 3, 4, 5, 6, 7]
def flatten_list(data):
    pass

```

### Q2. Numeric Kite Pattern

Task:
Write a program to print a numeric kite pattern based on a given integer n.

Example

If n = 3, the output should be:

```
  1
 121
12321
 121
  1
```

### Q3. Find Pairs with Target Sum

Task:
Given a list of integers and a target value, return all unique pairs whose sum equals the target

```py
nums = [2, 4, 3, 7, 5, 8, 1]
target = 9
Output: [(2, 7), (4, 5), (8, 1)]
def find_pairs(nums, target):
    pass

```

## Q4. Attempt Any One

🅐 Top-K Frequent Words (Single Loop Constraint)

Task:
You are given a string s consisting of words separated by spaces.
Return the top-n most frequent words using only one pass through the words
(you cannot re-iterate over the frequency dictionary or sort after counting).

Example

```py
Input:
s = "python is great and python is dynamic and great"
n = 3

Output:
[('python', 2), ('great', 2), ('is', 2)]
```

## 5. 🅑 Data Structures — Longest Substring with K Distinct Characters

Task:
Given a string s and an integer k, find the length of the longest substring that contains exactly k distinct characters.

Example

| Input             | Output | Explanation                          |
| :---------------- | :----- | :----------------------------------- |
| `"aabbcc"`, k = 2 | `4`    | `"aabb"` or `"bbcc"`                 |
| `"aaabbb"`, k = 3 | `0`    | No substring has 3 unique characters |
| `"eceba"`, k = 2  | `3`    | `"ece"`                              |

## Jasper Colin

### Round 1

1. Task:  user age api using FastAPI
2. websoket
3. middleware
4. fastapi background task - and also celery
5. sort the string # 01010101110111001

### round 2

Please find the task below for your reference. Request you to submit the response at the earliest.

Create a FastAPI-based application to manage a "Task Management System" with the following features:

API Endpoints:
Create a Task: Accept title, description, and status fields (status can be pending, in-progress, or completed).
Get All Tasks: Return a list of tasks with pagination (default: 10 tasks per page).
Update a Task: Allow updating the title and status of a task by its ID.
Delete a Task: Remove a task by its ID.
Database:
Use PostgreSQL to store tasks.
Create a table tasks with columns:
id (Primary Key, UUID)
title (String, Required)
description (String, Optional)
status (Enum: pending, in-progress, completed)
created_at (Timestamp, Default: Current Time)
updated_at (Timestamp, Auto-Update on Modify)
Requirements:

Write a FastAPI application that includes the above endpoints.
Use SQLAlchemy or any ORM for database interactions.
Write the database schema and migration script for PostgreSQL using Alembic.
Add proper exception handling and validation using Pydantic models.
Implement a health-check endpoint for database connectivity.
2. Application Architecture Design

Scenario:
You are tasked with designing the architecture for a FastAPI-based application that serves high traffic. The application must:

Use PostgreSQL as the primary database.
Handle millions of tasks and concurrent users.
Ensure high availability and scalability.
Include role-based access control (RBAC) for the API endpoints using Keycloak.
Enable logging and monitoring for troubleshooting and performance metrics.
Questions:

Describe how you would design the application architecture, including database design, API scalability, and authentication setup.
Provide a diagram of the architecture (describe in text form if unable to draw).
Explain how you would implement caching (e.g., for frequently accessed tasks) and message queuing (e.g., for background task processing).
s

## ZOHO -BY abynone else

1. You have a list nums = [1,2,3,[4,5],6] How to access the number 5?

    ```py
    nums = [1,2,3,[4,5],6]
    print(nums[3][1])
    ```

2. How do you merge two dictionaies without using update()?
    1. Using the | (Pipe) Operator — Python 3.9+

    ```py
    merged = dict1 | dict2
    print(merged)
    ```

    - The | operator (introduced in Python 3.9) merges two dictionaries.
    - If both dictionaries have the same key, the right-hand dictionary (dict2) takes precedence.

    2. Using Dictionary Unpacking (**) — Works in Python 3.5+

    ```py
    merged = {**dict1, **dict2}
    print(merged)
    ```

    - **dict1 and**dict2 unpack the key-value pairs into a new dictionary.
    - If duplicate keys exist, values from dict2 overwrite those from dict1.

    3. Using a For Loop

    ```py
    merged = {key: value for d in (dict1, dict2) for key, value in d.items()}
    print(merged)
    ```

3. WAP statement to unpack a into seprate vables

    ```py
    
    a,b,c,d,e = (1,2,3,4,5)
    print(a,b,c,d,e)    

    *a, = (1,2,3,4,5)
    print(a)
    ```

4. What's the use of *args and **kwargs in python?Given a short example.

    In Python,*args and**kwargs are used in function definitions to handle a variable number of arguments.
    1. *args (Non-keyword arguments)
    - *args allows a function to accept any number of positional arguments.

    ```py
    def add_numbers(*args):
    return sum(args)

    print(add_numbers(2, 4, 6))
    ```

    2. **kwargs (Keyword arguments)

    **kwargs allows a function to accept any number of keyword arguments.

    Inside the function, kwargs behaves like a dictionary.
    Inside the function, args behaves like a tuple.

    ```py
    def show_details(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

    show_details(name="Ashish", age=25, city="Delhi")
    ```

    - *args is used to pass a variable number of positional arguments.
    - **kwargs is used to pass a variable number of keyword arguments.
    - They make your functions more flexible and reusable.

### 5. What happens if you write a try bloack without an except block?

In Python, the `else` clause can be used both with **loops** and **try–except** blocks, but its purpose is slightly different in each case.

---

### 🔹  `else` with Loops

The `else` block in a loop executes **only if the loop completes normally**, meaning it **did not encounter a `break` statement`.**

So, it’s typically used when we’re **searching for something** and want to take an action **only if the item wasn’t found.**

**Example:**

```python
for i in range(5):
    if i == 3:
        print("Found 3")
        break
else:
    print("3 not found")
```

- If the loop finds `3`, it breaks, and the `else` block is skipped.
- If it doesn’t find `3`, the loop completes normally and the `else` block runs.

So in short:

> `else` with a loop runs only when the loop finishes **without a break**.

---

### 🔹 **2️⃣ `else` with `try–except`**

In a `try–except` block, the `else` part runs **only when no exception is raised** inside the `try` block.

This is useful when you want to keep your "normal" code separate from your "error-handling" code.

**Example:**

```python
try:
    x = int(input("Enter a number: "))
except ValueError:
    print("Invalid input!")
else:
    print("You entered:", x)
```

- If converting input to an integer succeeds, the `else` block runs.
- If a `ValueError` occurs, control goes to `except`, and `else` is skipped.

So, in summary:

> `else` in `try–except` executes **only when no exception occurs**.

---

### 🔹 **3️⃣ Optional `finally`**

You can also combine `else` with a `finally` block:

```python
try:
    x = 10 / 2
except ZeroDivisionError:
    print("Division error")
else:
    print("Division successful")
finally:
    print("Execution complete")
```

Here:

- `else` runs only if no exception occurs.
- `finally` runs **always**, whether there’s an error or not.

---

### 🧠 **Summary for Interview**

    | Construct      | When `else` runs                         | Skipped when              |
    | -------------- | ---------------------------------------- | ------------------------- |
    | **Loop**       | When loop finishes normally (no `break`) | If loop exits via `break` |
    | **Try–Except** | When no exception occurs                 | If an exception is raised |

    ---

    **In short:**

    > * With loops → `else` means *"no break happened."*
    > * With try–except → `else` means *"no error happened."*

### 6. Write a recursive function to find the sum of digits of a number

```py
def f(n):
if n==0:
    return 0
return n%10+f(n//10)
print(f(l))
```

### 7. How can you find the key with maximum value in a dictionay?

```py
data = {'a': 10, 'b': 25, 'c': 7, 'd': 30}
## Using max() with key parameter (Most Pythonic)

max_key = max(data, key=data.get)
print(max_key)
max_value = data[max_key]
print(max_key, max_value)

```

### 8. Write a one line code remove duplicates from list while keeping order

dict.fromkeys() is a class method that creates a new dictionary with the specified keys and an optional default value for all of them.

Syntax:
dict.fromkeys(iterable, value)

iterable → any iterable (like a list, tuple, or string) whose elements will become the dictionary’s keys.

value → (optional) the value assigned to each key. Default is None.

```py
keys = ['a', 'b', 'c']
d = dict.fromkeys(keys)
print(d) # {'a': None, 'b': None, 'c': None}

```

How it helps remove duplicates:
When you pass a list with duplicates to dict.fromkeys(), only unique keys remain, because dictionary keys are unique by design.

```py
l = [1, 2, 2, 3, 1, 4]
unique_dict = dict.fromkeys(l)
print(unique_dict)
```

dict.fromkeys() is a neat trick to remove duplicates while preserving order — because each key in a dictionary must be unique (and since Python 3.7+, dicts preserve insertion order).

## impetus

1. Explain the difference between tuple and list
2. Explain the functionality of get method in python
    The get() method is used with dictionaries to safely access the value of a key without causing an error if the key does not exist.

    Syntax

    ```
    dictionary.get(key, default_value)
    ```

    Parameters

    - key → The key you want to look up.
    - default_value (optional) → The value returned if the key is not found.
    - If not provided, it returns None.

   ### Without using get()

    ```py
    data = {"name": "Ashish", "age": 25}
    print(data["city"])   # ❌ KeyError: 'city'
    ```

    Using get()

    ```py
    data = {"name": "Ashish", "age": 25}
    print(data.get("city"))          # ✔ None (no error)
    print(data.get("city", "N/A"))   # ✔ N/A (custom default)
    print(data.get("name"))          # ✔ Ashish
    ```

    Why get() is useful
    - Prevents KeyError if the key is missing.
    - Allows providing a default value.
    - Makes code cleaner and safer.

    Question:
    Why is the get() method preferred over direct access dict[key] in API responses?

    Answer:
    Because API responses may not contain all fields.
    Using get() avoids crashes:

    response = {"status": "ok"}
    print(response.get("data"))      # No error → None

    Example 4: Counting Occurrences Using get()

    Question:
    Use the get() method to count occurrences of characters in a string.

    Answer:

    text = "banana"
    count = {}

    for ch in text:
        count[ch] = count.get(ch, 0) + 1

    print(count)

    Output:

    {'b': 1, 'a': 3, 'n': 2}

    Example 5: Nested Dictionary Access

    Question:
    How do you safely access a nested value using get()?

    Answer:

    user = {
        "profile": {
            "name": "Ashish"
        }
    }

    name = user.get("profile", {}).get("name")
    print(name)

    Output:

    Ashish

    Example 6: Handling Missing Keys in Loops

    Question:
    What does the following code output?

    d = {"a": 1, "b": None}
    print(d.get("b", 10))
    print(d.get("c", 10))

    Answer:

    None   # key exists but value is None → default NOT used
    10     # key doesn't exist → default used

    Example 7: Using get() in JSON Parsing

    Question:
    Given:

    import json
    data = '{"name":"Ashish"}'
    obj = json.loads(data)

    Why is this safer?

    city = obj.get("city", "Unknown")

    Answer:
    Because JSON may not contain the key. get() avoids exceptions and provides fallback values.

## 3. What are struct in python and implement struct in python

    In Python, there is no built-in struct keyword like in C/C++.

    Python provides multiple ways to create structure-like objects for grouping related data.
    1. User classes

        ```py
        class Person:
        def __init__(self, name, age, height):
            self.name = name
            self.age = age
            self.height = height

        p = Person("Alice", 25, 5.5)
        print(p.name, p.age, p.height)
        ```

        This behaves like a struct by grouping fields together.

    2. Using dataclasses

        ```py
        from dataclasses import dataclass

        @dataclass
        class Person:
            name: str
            age: int
            height: float

        p = Person("Charlie", 22, 5.8)
        print(p)
        ```

        - Auto-generated **init**, **repr**, **eq**
        - Cleaner syntax
        - Optional immutability (frozen=True)
    3. Using the struct module
        If by “struct” you mean binary packing/unpacking, Python has a struct module:

        ```py
        import struct

        # pack integers into bytes (C-style struct)
        data = struct.pack('i f', 10, 3.14)
        print(data)

        # unpack back to Python values
        unpacked = struct.unpack('i f', data)
        print(unpacked)
        ```

        Use cases:
        - Binary files
        - Network communication
        - C-compatible data formats
4. How to store the dictionary to the Database table. With three columns data

    ```
    data = {
        "name": "Ashish",
        "age": 25,
        "city": "Delhi"
    }
    ```

    Store Each Dict Key Into Separate Columns

    🏗 Ste: Create the DB Table Model

    ```py
    from sqlalchemy import Column, Integer, String
    from database import Base

    class User(Base):
        __tablename__ = "users"

        id = Column(Integer, primary_key=True, index=True)
        name = Column(String)
        age = Column(Integer)
        city = Column(String)
    ```

    Step 2: Pydantic Model

    ```py
    from pydantic import BaseModel

    class UserCreate(BaseModel):
        name: str
        age: int
        city: str
    ```

    Step 3: FastAPI Endpoint to Store the Dictionary

    ```py
    from fastapi import FastAPI, Depends
    from sqlalchemy.orm import Session

    app = FastAPI()

    @app.post("/save")
    def save_user(user: UserCreate, db: Session = Depends(get_db)):
        db_user = User(
            name=user.name,
            age=user.age,
            city=user.city
        )
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return db_user
    ```

    o/p

    ```
        {
    "name": "Ashish",
    "age": 25,
    "city": "Delhi"
    }
    ```

    If Your Dictionary Keys Are Dynamic

    ```py
    from sqlalchemy.dialects.postgresql import JSON

    class Data(Base):
        __tablename__ = "data"

        id = Column(Integer, primary_key=True)
        name = Column(String)
        payload = Column(JSON)    # store full dictionary
    @app.post("/save-dict")
    def save_dict(name: str, data: dict, db: Session = Depends(get_db)):
        db_row = Data(name=name, payload=data)
        db.add(db_row)
        db.commit()
        db.refresh(db_row)
        return db_row
    ```

5. What are middlewares in fast api. Give some example.
    Middleware in FastAPI is a function that runs before and after each request.

    It allows you to:

    - Modify the incoming request
    - Modify or inspect the outgoing response
    - Add cross-cutting features (logging, authentication, CORS, caching, etc.)

    ✅ How Middleware Works in FastAPI

    ```
    Client → Middleware → FastAPI Endpoint → Middleware → Client
    ```

    So it wraps the entire request/response lifecycle.

    🧩 Syntax of Middleware

    ```py
    @app.middleware("http")
    async def my_middleware(request: Request, call_next):
        # Code before request reaches the endpoint
        response = await call_next(request)
        # Code after endpoint returns response
        return response
    ```

    🔷 Middleware Flow Diagram

    ```
          ┌──────────────────────────┐
          │        Client            │
          └─────────────┬────────────┘
                        │ HTTP Request
                        ▼
              ┌───────────────────────┐
              │      MIDDLEWARE       │
              │  (Before Endpoint)    │
              └─────────────┬─────────┘
                            │
                            ▼
                ┌────────────────────┐
                │  FastAPI Endpoint  │
                └────────────┬───────┘
                            │ Response
                            ▼
              ┌───────────────────────┐
              │      MIDDLEWARE       │
              │   (After Endpoint)    │
              └─────────────┬─────────┘
                            │
                            ▼
          ┌──────────────────────────┐
          │        Client            │
          └──────────────────────────┘
    ```

    🚀 Example 1: Logging Request Time Middleware

    ```py
    import time
    from fastapi import FastAPI, Request

    app = FastAPI()

    @app.middleware("http")
    async def add_process_time_header(request: Request, call_next):
        start = time.time()
        response = await call_next(request)
        process_time = time.time() - start
        response.headers["X-Process-Time"] = str(process_time)
        return response
    ```

    Calculates how long each request takes

    Adds time in response header: X-Process-Time: 0.0023

    🚀 Example 2: Custom Authentication Middleware

    ```py
    from fastapi import FastAPI, Request, HTTPException

    app = FastAPI()

    @app.middleware("http")
    async def verify_token(request: Request, call_next):
        token = request.headers.get("X-API-Key")
        if token != "12345":
            raise HTTPException(status_code=401, detail="Invalid token")

        return await call_next(request)
    ```

    Checks API key in header

    Blocks request if token is wrong

    Add Custom Header to Every Response

    ```py
    @app.middleware("http")
    async def add_header(request: Request, call_next):
        response = await call_next(request)
        response.headers["X-App-Version"] = "1.0.0"
        return response
    ```

    logging Requests (Path + Method)

    ```py
    import logging

    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger("fastapi")

    @app.middleware("http")
    async def log_requests(request: Request, call_next):
        print(f"Incoming request: {request.method} {request.url}")
        response = await call_next(request)
        print(f"Response status: {response.status_code}")
        return response
    ```

    ```py
    from fastapi import FastAPI, Request
    import time
    from logging_config import logger   # import the logger

    app = FastAPI()

    @app.middleware("http")
    async def log_requests(request: Request, call_next):
        start_time = time.time()

        # Log the incoming request
        logger.info(
            f"Incoming request: {request.method} {request.url} from {request.client.host}"
        )

        # Process the request
        response = await call_next(request)

        # Calculate execution time
        duration = round(time.time() - start_time, 4)

        # Log completed request
        logger.info(
            f"Completed: {request.method} {request.url.path} "
            f"Status: {response.status_code} "
            f"Duration: {duration}s"
        )

        # Add duration to response header (optional)
        response.headers["X-Process-Time"] = str(duration)

        return response

    ```

    Q1. Why do we use middleware in FastAPI?

    To run code before and after each request — useful for logging, authentication, transformations, etc.

    Q2. Can middleware modify requests and responses?

    Yes. Middleware can change headers, body, or even block the request.

    | Middleware                       | Dependency                       |
    | -------------------------------- | -------------------------------- |
    | Runs for **every request**       | Runs only when endpoint uses it  |
    | Works at **global level**        | Works at **path/endpoint level** |
    | Has access to request + response | Mainly request                   |
    | Good for cross-cutting concerns  | Good for endpoint-specific logic |

    Q3. What parameters does a middleware receive?

    request: incoming request object
    call_next: function to call the next handler (endpoint)
### 6. How the Oauth2 works in Fast api. And how to implement the same.



OAuth2 is an authentication method where:

1️⃣ **User sends username + password**
2️⃣ Server **verifies** them
3️⃣ Server returns an **access token (JWT)**
4️⃣ User sends the token with every request
5️⃣ Server **validates token** → provides access

FastAPI has built-in tools to implement OAuth2, especially:

- `OAuth2PasswordBearer`
- `OAuth2PasswordRequestForm`

These handle:

➡ Extracting token from headers
➡ Validating authentication form
➡ Providing token to dependencies

---

# ⭐ Flow of OAuth2 With JWT in FastAPI

### ✔ Step 1: Client sends credentials

POST `/token`

```
username=ashish
password=1234
```

### ✔ Step 2: Server verifies and returns JWT

Response:

```json
{
  "access_token": "xyz.abc.123",
  "token_type": "bearer"
}
```

### ✔ Step 3: User sends token for secured endpoints

Header:

```
Authorization: Bearer <token>
```

### ✔ Step 4: FastAPI extracts token → validates → grants access

---

# ⭐ OAuth2 Implementation in FastAPI (JWT Based)

## 📌 Step 1 — Install requirements

```bash
pip install fastapi uvicorn python-jose passlib[bcrypt]
```

---

## 📌 Step 2 — Setup OAuth2 Scheme

```python
from fastapi.security import OAuth2PasswordBearer

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
```

This tells FastAPI:

> “Clients will send token in Authorization header as Bearer Token.”

---

## 📌 Step 3 — JWT Utility Functions

```python
from jose import JWTError, jwt
from datetime import datetime, timedelta

SECRET_KEY = "mysecretkey123"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

def create_access_token(data: dict, expires_delta=None):
    to_encode = data.copy()
    expire = datetime.utcnow() + (expires_delta or timedelta(minutes=15))
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
```

---

## 📌 Step 4 — Generate Token Endpoint `/token`

```python
from fastapi import Depends, FastAPI, HTTPException
from fastapi.security import OAuth2PasswordRequestForm

app = FastAPI()

fake_users = {
    "ashish": {
        "username": "ashish",
        "password": "1234"    # plain password for demo
    }
}

@app.post("/token")
def login(form: OAuth2PasswordRequestForm = Depends()):
    user = fake_users.get(form.username)
    if not user or form.password != user["password"]:
        raise HTTPException(status_code=400, detail="Invalid login")

    access_token = create_access_token({"sub": user["username"]})
    return {"access_token": access_token, "token_type": "bearer"}
```

---

## 📌 Step 5 — Dependency to Get Current User from Token

```python
async def get_current_user(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username = payload.get("sub")
        return {"username": username}
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")
```

---

## 📌 Step 6 — Protect Any Route

```python
@app.get("/profile")
def profile(user = Depends(get_current_user)):
    return {"message": "Welcome!", "user": user}
```

Now, this endpoint requires a valid OAuth2 token.

---

# ⭐ Example Workflow

### 1️⃣ User logs in

```
POST /token
username=ashish
password=1234
```

Response:

```json
{
  "access_token": "<JWT_TOKEN>",
  "token_type": "bearer"
}
```

### 2️⃣ User accesses protected API

```
GET /profile
Authorization: Bearer <JWT_TOKEN>
```

---

# 🧠 Interview-Ready Explanation

> OAuth2 in FastAPI provides a secure way to authenticate users using access tokens.
>
> The client first sends username and password to `/token`. FastAPI verifies the credentials and returns a JWT token. The client includes the JWT in the `Authorization: Bearer <token>` header for all protected endpoints.
>
> FastAPI’s `OAuth2PasswordBearer` extracts the token, and a dependency (`get_current_user`) validates it using the secret key. If valid, the user is authenticated and the request continues.
>
> This approach is secure, stateless, and widely used for API authentication.

---

If you want, I can also provide:

🔹 Refresh Tokens
🔹 Role-Based Access Control (RBAC)
🔹 Integrating OAuth2 with FastAPI + SQLAlchemy
🔹 Login form support for frontend

Just tell me!

7. How do you perform a heath check in fast API.
    A health check is a simple endpoint used to verify that your API is running and responsive. It is commonly used by load balancers, Kubernetes, Docker, and monitoring systems.

    ✅ Basic Health Check Endpoint

    ```py
    from fastapi import FastAPI

    app = FastAPI()

    @app.get("/health")
    async def health_check():
        return {"status": "ok"}
    ```

    Health Check With Database Check
    Often, you want to check database connectivity as well.

    ```py
    from fastapi import FastAPI, Depends
    from sqlalchemy.orm import Session
    from db import get_db_session  # your DB dependency

    app = FastAPI()

    @app.get("/health")
    async def health_check(db: Session = Depends(get_db_session)):
        try:
            db.execute("SELECT 1")   # simple DB ping
            return {"status": "healthy", "database": "connected"}
        except Exception:
            return {"status": "unhealthy", "database": "disconnected"}
    ```

8. How a fast API application is started. Write code for basic fast API application and starting the same.
Here is a clean and interview-ready answer for:

---

# **10. How a FastAPI application is started. Write code for a basic FastAPI application and how to run it.**

FastAPI applications are started using **Uvicorn**, an ASGI server.
FastAPI itself is just the framework — it needs an ASGI server to actually run.

---

# ✅ **How a FastAPI Application Starts (Concept)**

1. **Create a FastAPI instance**

   ```python
   app = FastAPI()
   ```

2. **Define routes (endpoints)**

   ```python
   @app.get("/")
   def home():
       return {"message": "Hello FastAPI"}
   ```

3. **Start the application using Uvicorn (ASGI server)**
   Example command:

   ```bash
   uvicorn main:app --reload
   ```

   - `main` → the Python filename (main.py)
   - `app` → FastAPI instance name
   - `--reload` → auto-restart on code changes (useful in development)

---

# ✅ **Basic FastAPI Application (main.py)**

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Hello FastAPI!"}

@app.get("/items/{item_id}")
def get_item(item_id: int):
    return {"item_id": item_id}
```

---

# ✅ **How to Run This Application**

### **Step 1: Install FastAPI + Uvicorn**

```bash
pip install fastapi uvicorn
```

### **Step 2: Run the app**

```bash
uvicorn main:app --reload
```

---

# ✅ **What Happens Internally When the App Starts?**

1. Uvicorn loads the module (`main.py`)
2. It finds the FastAPI instance (`app`)
3. It starts an ASGI server
4. FastAPI generates:

   - Routing table
   - OpenAPI schema
   - Docs (Swagger UI, ReDoc)
5. Server listens on:

   ```
   http://127.0.0.1:8000
   ```

---

# ⭐ Bonus (Often Asked in Interviews)

### **How to start FastAPI without the command line (programmatically)?**

```python
# run.py
import uvicorn

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
```

Run:

```bash
python run.py
```

---


9. How the different end points are managed in fast api using routers.
Here’s a clear and **interview-ready explanation** of **how FastAPI manages different endpoints using Routers**, along with practical examples.

---

# ⭐ **How FastAPI Manages Endpoints Using Routers**

When your application grows, placing all endpoints inside a single `main.py` file becomes messy.

To solve this, FastAPI provides **APIRouter**, which allows you to:

✅ Organize endpoints into separate files
✅ Group related routes (users, tasks, auth, etc.)
✅ Apply prefixes (e.g., `/users`)
✅ Apply tags (for Swagger UI)
✅ Apply middlewares or dependencies at router-level
✅ Keep clean & scalable project structure

---

# ⭐ **Simple Example Without Router (Not scalable)**

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/users")
def get_users():
    return ["A", "B"]

@app.get("/tasks")
def get_tasks():
    return ["Task1", "Task2"]
```

This becomes unmanageable as the project grows.

---

# ⭐ **Using APIRouter (Recommended)**

## 📁 **Project Structure**

```
app/
 ├── main.py
 ├── routers/
 │     ├── users.py
 │     ├── tasks.py
 │     └── auth.py
```

---

# 📌 **Step 1 — Create router for users**

➡ **app/routers/users.py**

```python
from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def get_users():
    return ["Ashish", "Rohit"]

@router.post("/")
def create_user():
    return {"message": "User created"}
```

---

# 📌 **Step 2 — Create router for tasks**

➡ **app/routers/tasks.py**

```python
from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def get_tasks():
    return ["Task1", "Task2"]
```

---

# 📌 **Step 3 — Include Routers into main app**

➡ **app/main.py**

```python
from fastapi import FastAPI
from routers import users, tasks

app = FastAPI()

app.include_router(users.router, prefix="/users", tags=["Users"])
app.include_router(tasks.router, prefix="/tasks", tags=["Tasks"])
```

---

# ⭐ Resulting Endpoints

| Router File | Endpoint Prefix | Final Endpoint |
| ----------- | --------------- | -------------- |
| users.py    | `/users`        | `/users/`      |
| tasks.py    | `/tasks`        | `/tasks/`      |

FastAPI automatically groups them in Swagger UI under tags.

---

# ⭐ Additional Router Features

## 🔹 1. **Apply prefix**

```python
prefix="/users"
```

All routes inside router will become:

```
/users/
/users/{id}
```

---

## 🔹 2. **Apply tags**

Tags organize endpoints on Swagger UI.

```python
tags=["Users"]
```

---

## 🔹 3. **Add dependencies to all routes in router**

```python
app.include_router(
    users.router,
    prefix="/users",
    dependencies=[Depends(authenticate)]
)
```

Every endpoint inside the router will require authentication.

---

## 🔹 4. **Versioning using Routers**

```python
app.include_router(v1.router, prefix="/api/v1")
app.include_router(v2.router, prefix="/api/v2")
```

---

# ⭐ **Interview-Ready Answer**

> FastAPI uses **APIRouter** to organize endpoints into separate modules.
> Each resource or feature—such as users, tasks, authentication—is placed in its own router file.
>
> The `main.py` imports these routers using `include_router()`, where we can apply route prefixes, tags, and shared dependencies.
>
> This helps scale applications cleanly by keeping the code modular, readable, and maintainable. FastAPI’s router system works similar to Express.js routes or Flask blueprints.

---

If you want, I can also explain:

🔹 How to organize large FastAPI projects (best directory structure)
🔹 Router-level middleware
🔹 Router-level OAuth2 protection
🔹 Versioning your API with routers

Just tell me!

10. Why Dataclasses?

A dataclass in Python is a decorator (@dataclass) that automatically generates special methods for a class—such as
`__init__,` `__repr__`, `__eq__`, and more—based on the class attributes.

They were introduced in Python 3.7 to make it easier to create classes that mainly store data (similar to structs).

Without dataclasses, you must manually implement boilerplate code:

```py
class Person:
    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city

    def __repr__(self):
        return f"Person(name={self.name}, age={self.age}, city={self.city})"

```

Dataclasses eliminate this with a single decorator:

```py
from dataclasses import dataclass

@dataclass
class Person:
    name: str
    age: int
    city: str

```

Python auto-generates:

```
__init__
__repr__
__eq__
__hash__ (optional)
__post_init__ hook
```

A dataclass is a Python feature that reduces boilerplate when creating classes that primarily hold data.
It automatically generates methods like **init**, **repr**, and **eq** based on class fields.
Dataclasses support default values, type hints, immutability, comparisons, and post-initialization validation

### Adding Default Values

```py
@dataclass
class Car:
    make: str
    model: str
    year: int = 2024
```

Making Dataclasses Immutable (like a C struct)

```py
@dataclass(frozen=True)
class Point:
    x: int
    y: int
```

```
p = Point(1, 2)
p.x = 10   # ❌ Error: Frozen dataclass cannot be modified

```

`__post_init__` — Validation Logic After Initialization

```py
@dataclass
class Product:
    name: str
    price: float

    def __post_init__(self):
        if self.price < 0:
            raise ValueError("Price cannot be negative")

```

### Comparison of Objects

```py
@dataclass(order=True)
class Score:
    points: int

print(Score(10) < Score(20))  # True
```

### Default Factories for Lists / Dicts

```py
from dataclasses import dataclass, field

@dataclass
class Classroom:
    students: list = field(default_factory=list)
```

How is a dataclass different from a regular class?

It automatically generates methods like **init**, which reduces boilerplate and improves readability.

2. How do you make a dataclass immutable?

Use @dataclass(frozen=True).

3. What is default_factory used for?

To safely create default mutable values like lists or dicts.

4. What is **post_init**?

A method that runs right after **init**, often used for validation.

5. How do you enable ordering comparisons?

Use @dataclass(order=True).

### Default `__eq__` in a Dataclass

When you use @dataclass, Python automatically generates the `__eq__` method for you.

```py
from dataclasses import dataclass

@dataclass
class Person:
    name: str
    age: int
p1 = Person("Alice", 30)
p2 = Person("Alice", 30)
p3 = Person("Bob", 25)

print(p1 == p2)  # True
print(p1 == p3)  # False

```

If You Want to Disable Auto **eq**

```py
@dataclass(eq=False)
class Person:
    name: str
    age: int
```

📌 If You Want to Override **eq** Manually

```py
@dataclass
class Person:
    name: str
    age: int

    def __eq__(self, other):
        return self.name.lower() == other.name.lower()
```

Here is a **clear and simple explanation** of **Serialization and Deserialization** with examples — great for interviews.

---

# 🔹 **Serialization and Deserialization in Python**

## **1. What is Serialization?**

**Serialization** is the process of converting a Python object into a format that can be:

- Stored (in file, database)
- Transmitted (over network)
- Reconstructed later

Common serialization formats:

- **JSON**
- **Pickle**
- **YAML**
- **MessagePack**

### **Example (Serialization using JSON)**

```python
import json

data = {"name": "Ashish", "age": 25}
json_string = json.dumps(data)

print(json_string)
```

**Output:**

```
{"name": "Ashish", "age": 25}
```

---

## **2. What is Deserialization?**

**Deserialization** is the reverse process — converting serialized data (JSON, binary, etc.) back into a Python object.

### **Example (Deserialization using JSON)**

```python
import json

json_string = '{"name": "Ashish", "age": 25}'
data = json.loads(json_string)

print(data)
```

**Output:**

```
{'name': 'Ashish', 'age': 25}
```

---

# 🔹 **Why Serialization Is Used?**

- Save program state to disk.
- Transfer data between services or microservices.
- Store objects in cache (Redis, Memcached).
- Convert Python objects to JSON for APIs.

---

# 🔹 Serialization vs Deserialization (Table)**

| Operation           | Meaning                            | Example Function                |
| ------------------- | ---------------------------------- | ------------------------------- |
| **Serialization**   | Convert object → JSON/string/bytes | `json.dumps()`, `pickle.dump()` |
| **Deserialization** | Convert JSON/string/bytes → object | `json.loads()`, `pickle.load()` |

---

# 🔹 **Interview-Style Examples**

### **Example 1: Serialize Python Dictionary to JSON**

**Question:**
Convert the following dict to JSON format:

```python
user = {"id": 1, "name": "Ashish"}
```

**Answer:**

```python
json_str = json.dumps(user)
```

---

### **Example 2: Deserialize JSON into Python Object**

**Question:**
Convert this JSON string into a Python dictionary:

```python
'{"id": 1, "active": true}'
```

**Answer:**

```python
data = json.loads('{"id": 1, "active": true}')
```

---

### **Example 3: Serialization in API Context**

**Question:**
Why is serialization required in REST APIs?

**Answer:**
APIs send data in **JSON** format.
Python objects must be serialized to JSON before sending to clients.

---

### **Example 4: Using Pickle for Python-Specific Serialization**

```python
import pickle

data = [1, 2, 3]
serialized = pickle.dumps(data)
original = pickle.loads(serialized)

print(original)
```

---

### **Example 5: JSON Serialization with Non-Serializable Types**

**Question:**
What happens if you try to serialize a `datetime` object using `json.dumps()`?

**Answer:**
It raises an error because JSON doesn't support datetime objects directly.
You must convert them manually:

```python
json.dumps({"date": str(datetime.now())})
```

---

🎤 5. Interview Questions (FastAPI Serialization/Deserialization)
Q1. How does FastAPI validate incoming request data?

FastAPI uses Pydantic models to:

Deserialize JSON

Validate fields and types

Convert types (e.g., "25" → int)

Q2. What is the role of response_model in FastAPI?

It controls:

Output serialization

What fields are included/excluded

Data shape consistency

Security (hide sensitive fields)

Q3. What is from_attributes in Pydantic v2?

Used to convert ORM models → Pydantic models during serialization.

class Config:
    from_attributes = True

Q4. How is JSON serialization handled in FastAPI?

FastAPI uses:

Pydantic for model → dict

JSONResponse / Standard JSON encoder for dict → JSON

Q5. Can FastAPI serialize complex types like datetime?

Yes, Pydantic automatically converts:

datetime → ISO format

UUID → string

Decimal → float (optional)

3. Serialization & Deserialization Flow in FastAPI
Request Flow

Client JSON → FastAPI → Pydantic model → Python object
✔ Type validation
✔ Field conversion (str → int, etc.)

Response Flow

Python object → Pydantic model → JSON → Client
✔ Only allowed fields returned
✔ Extra fields filtered
✔ Sensitive data can be hidden

| Stage               | Action                | Example       |
| ------------------- | --------------------- | ------------- |
| **Deserialization** | JSON → Pydantic model | Request body  |
| **Serialization**   | Pydantic model → JSON | Response body |

Here is a **clean, interview-ready explanation** of **CORS** and the **difference between CORS middleware and custom middleware** in FastAPI.

---

# ⭐ **Q5. Difference Between CORS Middleware and Custom Middleware?**

| Feature      | **CORS Middleware**                     | **Custom Middleware**                                   |
| ------------ | --------------------------------------- | ------------------------------------------------------- |
| Purpose      | Handle browser security rules (CORS)    | Any custom logic (logging, auth, headers, timing, etc.) |
| Provided by  | FastAPI / Starlette (built-in)          | Developer creates it                                    |
| Runs         | Before/after requests                   | Before/after requests                                   |
| Focus        | Allow or block cross-origin requests    | Implement business or infra logic                       |
| Configurable | Yes (allowed origins, methods, headers) | Totally custom                                          |
| Use cases    | Frontend → Backend communication        | Logging, token checks, rate limiting, etc.              |
| Complexity   | Simple configuration                    | You write the logic                                     |

### **In short:**

✔ CORS middleware solves a **browser-level security problem**
✔ Custom middleware solves **your application-level needs**

---

# 🔵 **What is CORS (Cross-Origin Resource Sharing)?**

**CORS** is a browser security feature that controls whether a web page from one origin (domain) can make requests to a backend on another origin.

### **Origin = protocol + domain + port**

Example:

- Frontend → `http://localhost:3000`
- Backend → `http://localhost:8000`

Different → Browser blocks request unless **CORS is enabled**.

---

# 🔵 Why CORS Exists?

Browsers block cross-site requests by default to prevent:

❌ CSRF attacks
❌ Malicious scripts
❌ Unauthorized API usage

CORS specifies **who** is allowed to talk to your backend.

---

# 🔵 **Preflight Request (OPTIONS)**

For some requests, the browser sends:

```
OPTIONS /api/users
```

This is called a **preflight** request, asking:

> "Server, is it okay if I send this request?"

CORS middleware responds with headers like:

```
Access-Control-Allow-Origin: http://localhost:3000
Access-Control-Allow-Methods: GET, POST
Access-Control-Allow-Headers: Content-Type
```

Only then the actual request is sent.

---

# 🟢 **CORS in FastAPI (Built-in Middleware)**

You add it like this:

```python
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

---

# 🔵 **What CORS Middleware Does Automatically**

✔ Handles preflight (`OPTIONS`) requests
✔ Adds necessary CORS headers
✔ Allows/blocks specific domains
✔ Allows/blocks methods (`GET`, `POST`, etc.)
✔ Allows/blocks headers

---

# 🔴 **Custom Middleware — What You Write Yourself**

Example:

```python
@app.middleware("http")
async def log_requests(request: Request, call_next):
    print(f"{request.method} {request.url}")
    response = await call_next(request)
    return response
```

Used for:

- Logging
- Authentication
- Rate limiting
- Modifying responses
- Adding custom headers
- Performance monitoring

---

# 🟣 **Key Interview Answer (Short & Perfect)**

**CORS Middleware** is a **built-in** middleware in FastAPI that resolves **cross-origin browser restrictions** by adding proper CORS headers and handling preflight requests.

**Custom Middleware** is **user-defined** logic that runs before and after each request for tasks like logging, authentication, timing, or modifying responses.

---

If you want, I can also prepare:
✔ MCQ questions on CORS
✔ Real examples of CORS errors
✔ CORS vs CSRF explanation
✔ Diagram explaining CORS flow

Here’s a clear and interview-friendly explanation:

---

# **Dependency Injection in FastAPI — What & Why?**

## **What is Dependency Injection (DI)?**

**Dependency Injection** is a design pattern where required components (dependencies) are *provided* to a function, class, or path operation instead of creating them manually inside the function.

In FastAPI, dependency injection is done using:

```python
from fastapi import Depends
```

---

# **Why do we need Dependency Injection in FastAPI? (Simple Explanation)**

FastAPI uses DI to help you **reuse logic**, **avoid code duplication**, and **keep your code clean and testable**.

Here are the main benefits:

---

## ✅ 1. **Clean & Modular Code**

Without DI:

```python
def get_user():
    db = create_db_session()  # creating DB session again
    ...
```

This repeats the same logic everywhere.

With DI:

```python
def get_user(db: Session = Depends(get_db)):
    ...
```

The DB session is provided automatically.
**No boilerplate. No repetition.**

---

## ✅ 2. **Centralized Control**

You can define things *once* (like DB connection, authentication logic, API key validation) and use them anywhere by injecting them.

---

## ✅ 3. **Better Testability**

DI makes it easy to mock dependencies during testing.

```python
app.dependency_overrides[get_db] = fake_db  # used in tests
```

So you can test your API **without hitting the real database**.

---

## ✅ 4. **Automatic Execution & Cleanup**

FastAPI automatically:

- Creates the dependency
- Passes it to the function
- Cleans it up after the request

Example:

```python
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
```

You don’t need to manually close the DB.
FastAPI handles it.

---

## ✅ 5. **Security & Authorization**

FastAPI has built-in security dependencies like OAuth2, JWT, API-key validation.

Example:

```python
def get_current_user(token: str = Depends(oauth2_scheme)):
    return decode_token(token)
```

Any route with this dependency automatically gets authentication.

---

## ✔ Example of Dependency Injection

```python
from fastapi import FastAPI, Depends

app = FastAPI()

def get_message():
    return "Hello from DI!"

@app.get("/demo")
def demo(msg: str = Depends(get_message)):
    return {"msg": msg}
```

FastAPI calls `get_message()` automatically and provides the result.

---

# **In short — Why we need DI in FastAPI?**

✔ Reduce repetition
✔ Increase maintainability
✔ Centralize important logic
✔ Easy testing
✔ Auto-handling of lifecycle & cleanup
✔ Security/authentication becomes reusable

---

Great! Here is a complete, interview-oriented explanation of **types of dependencies in FastAPI**, **sub-dependencies**, **class-based dependencies**, and **background tasks**, with examples.

---

# ✅ **1. Types of Dependencies in FastAPI**

FastAPI supports **three main types** of dependencies:

---

## **1️⃣ Function-based Dependencies (Most Common)**

These are simple Python functions used as dependencies.

### **Example**

```python
from fastapi import Depends, FastAPI

app = FastAPI()

def get_message():
    return "Hello"

@app.get("/one")
def one(msg: str = Depends(get_message)):
    return {"message": msg}
```

---

## **2️⃣ Class-based Dependencies (Good for shared state or complex logic)**

FastAPI calls the class like a function (it uses `__call__()`).

### **Example**

```python
class AuthChecker:
    def __init__(self, token_required: bool = True):
        self.token_required = token_required

    def __call__(self):
        if self.token_required:
            return "Token validated"
        return "No token required"

auth = AuthChecker()

@app.get("/check")
def check(auth_result: str = Depends(auth)):
    return {"auth": auth_result}
```

Useful when:

- You have multiple steps inside a dependency
- You want to maintain state
- You need configuration

---

## **3️⃣ Sub-Dependencies (Dependency inside another dependency)**

Example:
To validate user → you need a token → which requires extracting headers.

### **Example**

```python
from fastapi import Header

def get_token(authorization: str = Header(...)):
    return authorization

def get_current_user(token: str = Depends(get_token)):
    return {"user": "ashish", "token": token}

@app.get("/me")
def me(user = Depends(get_current_user)):
    return user
```

This keeps your logic clean and layered.

---

# ✅ **2. Dependency Parameters (Request-based, shared, optional)**

---

## **Optional Dependency**

```python
from typing import Optional

def optional_token(token: Optional[str] = Header(None)):
    return token
```

---

## **Shared Dependency (`use_cache=True`)**

FastAPI caches dependencies by default per request.
If two endpoints use the same dependency, it's executed once.

```python
@app.get("/a")
@app.get("/b")
def both(db = Depends(get_db)):
    return {"ok": True}
```

---

# ✅ **3. Dependencies with `yield` (Setup + Cleanup)**

Useful for:

- DB connections
- Opening files
- Network resources

### Example (Database session)

```python
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
```

FastAPI:

1. Executes code before `yield`
2. Passes value to route
3. Executes code after `yield` automatically

---

# ✅ **4. Background Tasks as Dependencies**

Sometimes you want an operation **after the response is sent**, like:

- Sending email
- Logging
- Updating analytics

### Example

```python
from fastapi import BackgroundTasks

def send_email(email: str):
    print("Sending email to", email)

@app.post("/register")
def register(email: str, bg: BackgroundTasks):
    bg.add_task(send_email, email)
    return {"msg": "User registered"}
```

FastAPI sends the response instantly and continues the task in the background.

---

# ✔ Summary (Interview Answer)

**FastAPI Dependency Injection Types:**

1. **Function-based** – simple reusable logic.
2. **Class-based** – good for complex or stateful dependencies.
3. **Sub-dependencies** – when dependencies depend on other dependencies.

**Why use DI?**

- Avoid duplication
- Clean, modular code
- Automatic resource cleanup
- Improve security & authentication
- Easy to test
- Better separation of concerns

---

Here’s a simple and interview-friendly explanation of **decoupling** — especially in the context of FastAPI and Dependency Injection.

---

# ✅ **What is Decoupling? (Simple Definition)**

**Decoupling means separating components so they do not depend directly on each other.**
Each part works independently, can be modified independently, and can be tested independently.

More decoupling → cleaner, flexible, maintainable system.

---

# 🧠 **Why do we need Decoupling?**

Because tightly-coupled code:

❌ Hard to test
❌ Hard to reuse
❌ Hard to change
❌ Breaks easily if one thing changes

Decoupled code:

✔ Flexible
✔ Easy to modify
✔ Replaceable
✔ Testable
✔ Cleaner architecture

---

# 🎯 **Decoupling in FastAPI (Through Dependency Injection)**

FastAPI’s dependency injection system helps achieve decoupling.

### Example (Tightly Coupled Code)

```python
@app.get("/users")
def get_users():
    db = SessionLocal()  # direct DB dependency
    return db.query(User).all()
```

Problems:

- If DB changes → this function breaks
- Hard to test (always hits real DB)
- You can't mock the database

---

### ✅ **Decoupled Version Using DI**

```python
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/users")
def get_users(db: Session = Depends(get_db)):
    return db.query(User).all()
```

Now:

- DB logic is separated
- Can replace DB with a fake one
- Cleaner architecture
- Reusable DB logic

---

# 🧪 **Decoupling Helps in Testing**

FastAPI allows overriding dependencies:

```python
from fastapi.testclient import TestClient

def fake_db():
    yield FakeDB()

app.dependency_overrides[get_db] = fake_db
```

Now the API uses a **mock database** → no real DB needed.

This is *only possible* because of decoupling.

---

# 🛠 **More Examples of Decoupling in FastAPI**

### ✔ Authentication

You don’t put auth logic in every route.
You create a dependency:

```python
def get_current_user(token = Depends(oauth2_scheme)):
    return decode_token(token)
```

Routes become independent of auth implementation:

```python
@app.get("/profile")
def profile(user = Depends(get_current_user)):
    return user
```

If tomorrow you switch JWT → OAuth → API key,
**routes don’t change** → that's decoupling.

---

### ✔ Logging

Middleware handles logging separately.
Routes don't care about logging logic.

---

### ✔ Configuration

You can inject settings instead of hardcoding.

---

# 🧩 **Interview-Style Answer**

> **Decoupling** means separating code components so they are independent and do not directly rely on each other.
>
> In FastAPI, decoupling is achieved through **dependency injection**, where shared logic like database sessions, authentication, configuration, or services are injected into routes instead of being created inside them.
>
> This makes the code cleaner, reusable, testable, and easier to maintain because you can change or replace a dependency without modifying the route logic.

---

If you want, I can also explain:

🔹 Inversion of Control (IoC)
🔹 Coupling vs Cohesion
🔹 High-level clean architecture for FastAPI

Here’s a clear and interview-friendly explanation of **Inversion of Control (IoC)** vs **Dependency Injection (DI)** — one of the most common backend interview questions.

---

# ⭐ **Inversion of Control (IoC) vs Dependency Injection (DI)**

## 🚀 **Short Answer (For Interviews)**

- **Inversion of Control (IoC)** is a *principle* that says:

  > *Don’t let your code control everything — let a framework or external system control the flow.*

- **Dependency Injection (DI)** is a *design pattern* (a technique) that implements IoC by:

  > *Providing required components (dependencies) from outside instead of creating them inside.*

**DI is one way to achieve IoC.**

---

# 🔍 **Detailed but Simple Explanation**

## 1️⃣ **What is Inversion of Control (IoC)?**

Normally in traditional programming:

- Your code controls the flow
- Your code decides when to create objects
- Your code decides how logic executes

With IoC:

- The **control is inverted**
- A **framework** (like FastAPI, Spring, Django) controls when your functions run
- You provide functions/classes — the framework calls them at the right time

### ✔ Example (IoC in FastAPI)

```python
@app.get("/users")
def get_users():
    return {"ok": True}
```

Who calls `get_users()`?

Not you.
**FastAPI calls it** when a request comes in.

That’s **IoC**.

---

## 2️⃣ **What is Dependency Injection (DI)?**

DI is a *method* to supply dependent objects from outside.

Instead of:

```python
def get_users():
    db = DBConnection()  # creating dependency inside
```

We inject it:

```python
def get_users(db = Depends(get_db)):
    return db.query(User).all()
```

**DI makes code decoupled, testable, clean.**

---

# 🎯 **Relationship Between IoC and DI**

Think of IoC as “big concept”
and DI as “one tool to implement it”.

```
Inversion of Control
    |
    -> Dependency Injection (one implementation)
    -> Event listeners
    -> Middleware
    -> Framework lifecycle hooks
```

DI ≠ IoC
DI ⊂ IoC

---

# 🧠 **FastAPI Example to Show IoC + DI Together**

### Example: Database Dependency

```python
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
```

DI:

```python
@app.get("/items")
def items(db = Depends(get_db)):
    return db.query(Item).all()
```

IoC:

FastAPI decides:

- when to create the DB connection
- when to call the route function
- when to execute the dependency
- when to close the DB connection

Your code is not in control — the framework is.

---

# 🧑‍🏫 **Interview-Ready Explanation**

> **Inversion of Control (IoC)** is a broad principle where the control of program flow is shifted from developer-written code to an external system like a framework.
> **Dependency Injection (DI)** is a specific design pattern used to achieve IoC by supplying required dependencies from outside instead of creating them internally.
>
> In FastAPI, IoC is seen when the framework controls the request handling and calls your functions automatically. DI is seen when dependencies like database sessions or authentication are injected using `Depends`.

---

Here is a clear, simple, and interview-ready explanation of **Coupling vs Cohesion**, with examples related to FastAPI.

---

# ⭐ **Coupling vs Cohesion (Interview Answer)**

## 🔹 **Cohesion = How focused a module/class/function is.**

High cohesion → a module does *one clear thing*.

## 🔹 **Coupling = How dependent one module is on another.**

Low coupling → modules depend on each other *as little as possible*.

---

# 🧠 **Simple Meaning**

| Concept      | Meaning                                                  | Good/Bad                   |
| ------------ | -------------------------------------------------------- | -------------------------- |
| **Cohesion** | How strongly things inside a module relate to each other | **Higher cohesion = GOOD** |
| **Coupling** | How strongly modules depend on other modules             | **Lower coupling = GOOD**  |

---

# 🎯 Example to Understand Quickly

### 📦 **High Cohesion Example**

A file `auth.py` contains only authentication-related functions:

```python
def hash_password(pwd): ...
def verify_user(token): ...
def create_jwt(user): ...
```

Everything inside it is related to *auth* → HIGH cohesion.

### 📦 **Low Cohesion Example**

A single file contains:

- DB logic
- Auth logic
- Email logic
- Validation logic

Not related → LOW cohesion → BAD.

---

# 🔗 Coupling in FastAPI

### ❌ **High Coupling Example (Bad)**

Route directly creates DB connection:

```python
@app.get("/users")
def get_users():
    db = DBConnection()   # tightly coupled
    return db.query(User).all()
```

If DB changes → route breaks.
If you want to test → hard.

### ✔ **Low Coupling Example Using Dependency Injection (Good)**

```python
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/users")
def get_users(db = Depends(get_db)):
    return db.query(User).all()
```

- Route does NOT depend on actual DB creation
- DB can be replaced in tests
- Code is modular

→ This is **LOW coupling**.

---

# 🔥 Cohesion in FastAPI

### ✔ High Cohesion

**Router file for tasks:**

```
routers/
   tasks.py   → contains only task logic
   users.py   → contains only user logic
   auth.py    → contains only auth logic
```

Each module has a *single responsibility*.

### ❌ Low Cohesion

```
api.py → contains all routes mixed together
```

Hard to maintain, unclear responsibility.

---

# 🎯 Why Low Coupling & High Cohesion Are Good

| Benefit                  | Why it matters                         |
| ------------------------ | -------------------------------------- |
| **Easier testing**       | Mock dependencies easily               |
| **More maintainable**    | Small focused modules                  |
| **More reusable**        | Modules can be used elsewhere          |
| **Less breakage**        | Changing one part doesn’t break others |
| **Cleaner architecture** | Easier to understand                   |

---

# 🧑‍🏫 **Interview-Ready Summary**

> **Cohesion** describes how related the responsibilities within a module are. Higher cohesion means a module focuses on one purpose — which is desirable.
>
> **Coupling** describes how much modules depend on each other. Lower coupling means modules interact through well-defined interfaces and do not break each other — also desirable.
>
> In FastAPI, using Dependency Injection increases cohesion by keeping responsibilities separate (DB logic, auth logic, routing logic stay isolated) and reduces coupling by injecting dependencies instead of creating them directly.

---

If you want, I can also explain:

🔹 High cohesion + low coupling in **clean architecture**
🔹 Example folder structure for FastAPI
🔹 Real-world scenarios based on microservices

Just say **yes**.

Here is a **clean, interview-ready, production-ready** explanation of:

# ✅ **1. Running FastAPI with Gunicorn + Uvicorn Workers (Production Setup)**

# ✅ **2. Running FastAPI in Docker (with full Dockerfile example)**

---

# #️⃣ **1. Running FastAPI with Gunicorn + Uvicorn Workers**

FastAPI uses **Uvicorn** (ASGI server).
For production, we combine:

### **Gunicorn (Process Manager)**

✔ Manages multiple worker processes
✔ Restarts workers automatically
✔ Handles load balancing between workers

### **Uvicorn Workers**

✔ Async support
✔ High-performance server for FastAPI

---

## ✔ **Installation**

```bash
pip install gunicorn uvicorn
```

---

## ✔ **Command to Run FastAPI with Gunicorn + Uvicorn Workers**

```bash
gunicorn main:app -k uvicorn.workers.UvicornWorker --workers 4 --bind 0.0.0.0:8000
```

### **Explanation:**

| Argument                           | Meaning                                         |
| ---------------------------------- | ----------------------------------------------- |
| `main:app`                         | main.py → app instance                          |
| `-k uvicorn.workers.UvicornWorker` | worker class for async FastAPI                  |
| `--workers 4`                      | number of processes (CPU cores × 2 recommended) |
| `--bind 0.0.0.0:8000`              | host + port                                     |

---

## ✔ **Auto-detect recommended worker count**

```bash
gunicorn main:app -k uvicorn.workers.UvicornWorker --workers $(nproc --all) --bind 0.0.0.0:8000
```

---

# #️⃣ **2. Running FastAPI in Docker**

### **📌 Folder Structure**

```
/fastapi-app
    ├── main.py
    ├── requirements.txt
    └── Dockerfile
```

---

# ✔ **Dockerfile (Production-Ready)**

```dockerfile
# Use official Python base image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application files
COPY . .

# Expose the port
EXPOSE 8000

# Start using Gunicorn + Uvicorn worker
CMD ["gunicorn", "main:app", "-k", "uvicorn.workers.UvicornWorker", "--workers", "4", "--bind", "0.0.0.0:8000"]
```

---

# ✔ **requirements.txt Example**

```
fastapi
uvicorn
gunicorn
```

---

# ✔ **Build Docker Image**

```bash
docker build -t fastapi-app .
```

---

# ✔ **Run Docker Container**

```bash
docker run -p 8000:8000 fastapi-app
```

Now the app is available at:

```
http://localhost:8000
```

---

# #️⃣ **Docker + Uvicorn (Dev Mode)**

If you want **reload** for development:

### **Dockerfile.dev**

```dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
```

Run:

```bash
docker build -t fastapi-dev -f Dockerfile.dev .
docker run -p 8000:8000 fastapi-dev
```

---

# #️⃣ **Bonus: docker-compose.yml Example**

```yaml
version: "3"

services:
  fastapi:
    build: .
    ports:
      - "8000:8000"
    environment:
      - ENV=production
    restart: always
```

Run:

```bash
docker compose up --build
```

---

# 🎉 Want more?

I can also give you:

✅ **Nginx + FastAPI Reverse Proxy Setup**
✅ **Docker + PostgreSQL + FastAPI complete project**
✅ **CI/CD pipeline for FastAPI (GitHub Actions / Docker Hub)**

Just tell me!
Here is a **clear and interview-ready explanation** of **Iterable vs Generator** with **examples + code**:

---

# 🔍 Iterable vs Generator (Python)

## ✅ **1. Iterable**

An **iterable** is any Python object you can loop over using a `for` loop.

### ✔ Examples of iterables

- list
- tuple
- string
- dict
- set
- file object
- any class that implements `__iter__()` or `__getitem__()`

### ✔ Characteristics of Iterables

- Stores **all values in memory**.
- Slower when handling large datasets.
- Can iterate **multiple times**.
- Returns an **iterator** when passed to `iter()`.

### ✔ Example

```python
nums = [1, 2, 3]    # list is iterable

for n in nums:
    print(n)
```

---

# ✅ **2. Generator**

A **generator** is a special type of iterator that **generates values on the fly**, one at a time, and does NOT store them in memory.

### ✔ Characteristics of Generators

- Uses **lazy evaluation** → produces values only when needed.
- **Memory-efficient** (doesn’t store entire sequence).
- **Faster** for large data.
- You can iterate **only once**.
- Created using:

  - `yield` inside a function
  - Generator expression: `(x for x in range(10))`

---

# ▶ Example: Generator using `yield`

```python
def my_generator():
    for i in range(3):
        yield i

gen = my_generator()
print(next(gen))   # 0
print(next(gen))   # 1
print(next(gen))   # 2
```

---

# ▶ Example: Generator Expression

```python
gen = (x*x for x in range(5))
for i in gen:
    print(i)
```

---

# 🔥 Memory Difference Example

```python
import sys

lst = [x for x in range(1000000)]
gen = (x for x in range(1000000))

print(sys.getsizeof(lst))  # large memory usage
print(sys.getsizeof(gen))  # very small memory usage
```

---

# 📝 Summary Table: Iterable vs Generator

| Feature                     | Iterable                  | Generator                          |
| --------------------------- | ------------------------- | ---------------------------------- |
| Stores Data                 | Yes (all items in memory) | No (generates one value at a time) |
| Memory Usage                | High                      | Very low                           |
| Speed                       | Slower for large datasets | Faster due to lazy evaluation      |
| Can iterate multiple times? | Yes                       | No (exhausts after one use)        |
| Examples                    | list, tuple, dict, string | `yield`, generator expressions     |
| Use Case                    | Small/medium data         | Large data, streaming, pipelines   |

---

# 🎯 Interview Short Answer

**Iterable:** An object that returns an iterator when `iter()` is called. It holds all items in memory.
**Generator:** A type of iterator that yields items lazily using `yield`. More memory-efficient and faster for large data.

---

If you want, I can give you:

✔ Iterable vs iterator vs generator (3-way comparison)
✔ When to use generators in real projects
✔ Generator use case in FastAPI (streaming large responses)

Just tell me!
Here's the **clearest and interview-ready explanation** of **Iterator vs Generator** with examples and code.

---

# 🔍 **Iterator vs Generator (Python)**

## ✅ 1. **Iterator**

An **iterator** is an object used to iterate over an iterable, **one element at a time**.

### ✔ How do you know something is an iterator?

It must implement:

- `__iter__()`
- `__next__()`

### ✔ How an iterator works

```python
nums = [1, 2, 3]
it = iter(nums)

print(next(it))   # 1
print(next(it))   # 2
print(next(it))   # 3
```

When there are no more elements, it raises **StopIteration**.

### ✔ Characteristics

| Feature     | Iterator                         |
| ----------- | -------------------------------- |
| Memory      | Depends on underlying iterable   |
| Usage       | Used to fetch next element       |
| Reusability | **Not reusable** (exhausts once) |
| Creation    | Using `iter()` or custom class   |

---

# ✅ 2. **Generator**

A **generator is a special type of iterator**, created using:

- `yield` inside a function
- OR a generator expression

### ✔ Example using `yield`

```python
def my_gen():
    yield 1
    yield 2
    yield 3

gen = my_gen()
print(next(gen))  # 1
print(next(gen))  # 2
print(next(gen))  # 3
```

### ✔ Generator expression

```python
gen = (x*x for x in range(3))
```

### ✔ Characteristics

| Feature     | Generator                                   |
| ----------- | ------------------------------------------- |
| Memory      | **Very low** (produces one value at a time) |
| Creation    | Using `yield` or generator expression       |
| Speed       | Faster for large data                       |
| Reusability | **Not reusable** (exhausts once)            |

---

# 🎯 **Key Difference (Simple)**

| Feature                   | Iterator                 | Generator                       |
| ------------------------- | ------------------------ | ------------------------------- |
| What is it?               | Object used to iterate   | **A type of iterator**          |
| How created?              | `iter()` or custom class | `yield` or generator expression |
| Memory usage              | Varies                   | **Minimal (lazy)**              |
| Syntax complexity         | More code                | Very concise                    |
| **next**() implementation | Must write manually      | Auto-handled by Python          |

---

# 📌 **Custom Iterator Example** (manual)

```python
class Counter:
    def __init__(self, limit):
        self.limit = limit
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < self.limit:
            self.current += 1
            return self.current
        raise StopIteration

it = Counter(3)
print(list(it))  # [1, 2, 3]
```

---

# 📌 **Equivalent Generator Example** (simpler)

```python
def counter(limit):
    for i in range(1, limit + 1):
        yield i

gen = counter(3)
print(list(gen))  # [1, 2, 3]
```

---

# ⭐ Interview One-Liner Answer

> **An iterator is an object that implements `__iter__()` and `__next__()`.
> A generator is a simpler way to create an iterator using `yield`, and is more memory-efficient because it produces values lazily.**

---

If you want, I can also give you:

✔ Iterable vs Iterator vs Generator (3-in-1 table)
✔ Real-world generator use case in FastAPI (stream streaming responses)
✔ Code examples for advanced generators (send, throw, close)

Just tell me!

Monitoring Tools for FastAPI
✅ 1. Prometheus + Grafana (Most popular)
🔵 2. Loguru (Most recommended for FastAPI)

GIL (Global Interpreter Lock) ensures only one thread executes Python bytecode at a time. It simplifies memory management but prevents true multi-threading for CPU-bound tasks. I/O-bound tasks are not affected because they release the GIL.

➡ GIL kills multi-threading performance for CPU-intensive tasks.

| Feature     | **Event Loop (asyncio)**                  | **Thread**                                          |
| ----------- | ----------------------------------------- | --------------------------------------------------- |
| Model       | Single-threaded, cooperative multitasking | Multi-threaded, OS-level scheduling                 |
| Best for    | I/O-bound tasks                           | CPU-bound tasks / parallelism                       |
| Switching   | Manual switching using `await`            | Automatic OS context switching                      |
| Overhead    | Very low; no thread creation              | High; thread creation & context switch cost         |
| Safety      | No shared-memory issues                   | Race conditions, need locks                         |
| Used in     | FastAPI, Node.js, async apps              | Django, Flask, CPU-heavy tasks                      |
| Concurrency | Yes                                       | Yes                                                 |
| Parallelism | No (GIL stops parallel Python code)       | Yes (but GIL still limits CPU-bound Python threads) |

The event loop is the core of asyncio. It schedules and runs asynchronous tasks. When a task is waiting (like for I/O), the event loop switches to another task so nothing blocks. FastAPI uses the event loop to handle many requests concurrently using async/await.
