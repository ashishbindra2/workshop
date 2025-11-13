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

What are the set() and pop() functions in Python?
What is Django ORM?
What is FastAPI, and how does it compare to Flask? (Which is better and why?)
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
5. Threads in python
6. async in python
7. why fastapi is asyncronus how explain.
8. orm mapping

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

5. What happens if you write a try bloack without an except block?

    In Python, the `else` clause can be used both with **loops** and **try–except** blocks, but its purpose is slightly different in each case.

    ---

### 🔹 **1️⃣ `else` with Loops**

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

    * If the loop finds `3`, it breaks, and the `else` block is skipped.
    * If it doesn’t find `3`, the loop completes normally and the `else` block runs.

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

    * If converting input to an integer succeeds, the `else` block runs.
    * If a `ValueError` occurs, control goes to `except`, and `else` is skipped.

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

    * `else` runs only if no exception occurs.
    * `finally` runs **always**, whether there’s an error or not.

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

6. Write a recursive function to find the sum of digits of a number.

    ```py
    def f(n):
    if n==0:
        return 0
    return n%10+f(n//10)
    print(f(l))
    ```

7. How can you find the key with maximum value in a dictionay?

    ```py
    data = {'a': 10, 'b': 25, 'c': 7, 'd': 30}
    ## Using max() with key parameter (Most Pythonic)
    
    max_key = max(data, key=data.get)
    print(max_key)
    max_value = data[max_key]
    print(max_key, max_value)

    ```

8. Write a one line code remove duplicates from list while keeping order.

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
