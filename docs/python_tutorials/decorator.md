## What is a Decorator in Python?
A decorator in Python is a function that takes another function as input and extends or modifies its behavior without modifying its actual code. Decorators are often used to add functionalities like logging, authentication, or timing to functions.

## How Decorators Work
Decorators use the concept of higher-order functions, meaning they take a function as input, add extra behavior, and return a new function.

Basic Structure of a Decorator
```python
def my_decorator(func):
    def wrapper():
        print("Something before the function runs")
        func()
        print("Something after the function runs")
    return wrapper
```
Now, you can apply this decorator to a function:

```python
@my_decorator
def say_hello():
    print("Hello, World!")

say_hello()
Output
Something before the function runs
Hello, World!
Something after the function runs
```


Example 1: Logging with a Decorator
```python
def log_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Calling function: {func.__name__} with arguments {args} {kwargs}")
        result = func(*args, **kwargs)
        print(f"Function {func.__name__} returned {result}")
        return result
    return wrapper

@log_decorator
def add(a, b):
    return a + b

print(add(5, 3))
Output

Calling function: add with arguments (5, 3) {}
Function add returned 8
```

Example 2: Timing a Function Execution
```python
import time

def timer_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Function {func.__name__} took {end_time - start_time:.5f} seconds to execute")
        return result
    return wrapper

@timer_decorator
def slow_function():
    time.sleep(2)
    print("Finished execution")

slow_function()
Output
Finished execution
```
Function slow_function took 2.00045 seconds to execute

Example 3: Checking User Authentication
```python
def authenticate(func):
    def wrapper(user):
        if user != "admin":
            print("Access denied!")
            return
        return func(user)
    return wrapper

@authenticate
def dashboard(user):
    print(f"Welcome to the dashboard, {user}!")

dashboard("guest")  # Output: Access denied!
dashboard("admin")  # Output: Welcome to the dashboard, admin!
Chaining Multiple Decorators
```

You can apply multiple decorators to a function:

```python
@timer_decorator
@log_decorator
def multiply(a, b):
    return a * b

print(multiply(4, 5))
```
This will first log the function call, then measure its execution time.