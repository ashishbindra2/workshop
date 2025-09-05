# Python 3.10

Python 3.10 was released on October 4th, 2021.

Python language that will help to make your Python code even cleaner:

1. Structural pattern matching
2. Parenthesized context managers
3. Clearer error messages
4. Improved type annotations
5. Strict argument for zipping

## Structural Pattern Matching

It introduces a match/case statement to the Python language, which looks very much like a switch/case statement in other programming languages. With structural pattern matching, you can test an object against one or more patterns to determine if the structure of the comparison object matches one of the given patterns.

```py
code = 404

match code:
    case 200:
        print("OK")
    case 404:
        print("Not found")
    case 500:
        print("Server error")
    case _:
        print("Code not found")
```

Patterns can be:

1. literals
2. captures
3. wildcards
4. values
5. groups
6. sequences
7. mappings
8. classes

```py
from http import HTTPStatus

code = 404

match code:
    case HTTPStatus.OK:
        print("OK")
    case HTTPStatus.NOT_FOUND:
        print("Not found")
    case HTTPStatus.INTERNAL_SERVER_ERROR:
        print("Server error")
    case _:
        print("Code not found")


# => "Not found"
```

You can also combine multiple patterns using the OR pattern:

```py
from http import HTTPStatus

code = 400

match code:
    case HTTPStatus.OK:
        print("OK")
    case HTTPStatus.NOT_FOUND | HTTPStatus.BAD_REQUEST:
        print("You messed up")
    case HTTPStatus.INTERNAL_SERVER_ERROR | HTTPStatus.BAD_GATEWAY:
        print("Our bad")
    case _:
        print("Code not found")


# => "You messed up"
```

What makes structural pattern matching different from the switch/case syntax in other languages is that you can unpack complex data types and perform actions based on the resulting data:

```py
point = (0, 10)

match point:
    case (0, 0):
        print("Origin")
    case (0, y):
        print(f"Y={y}")
    case (x, 0):
        print(f"X={x}")
    case (x, y):
        print(f"X={x}, Y={y}")
    case _:
        raise ValueError("Not a point")


# => Y=10
```

Here, the value (10) is bound from the subject ((0, 10)) to a variable inside the case. This is the capture pattern.

You can achieve nearly the same thing with the class pattern:

```py
from dataclasses import dataclass
@dataclass
class Point:
    x: int
    y: int

point = Point(10, 10)

match point:
    case Point(x=0, y=0):
        print("Origin")
    case Point(x=0, y=y):
        print(f"On Y axis with Y={y}")
    case Point(x=x, y=0):
        print(f"On X axis with X={x}")
    case Point(x=x, y=y):
        print(f"Somewhere in a X, Y plane with X={x}, Y={y}")
    case _:
        print("Not a point")


# => Somewhere in a X, Y plane with X=10, Y=10
```

## Parenthesized Context Managers

Python now supports continuation across multiple lines when using context managers:

```py
with (
    CtxManager1() as ctx1,
    CtxManager2() as ctx2
):
```

## Clearer Error Messages

As you can tell, it's much easier to spot the actual issue with the new error message

## Improved Type Annotations

### Union Operator

First, you'll also be able to use a new type union operator, `|`, so you can express either type X or Y rather than having to import `Union` from the `typing`module:

```py
# before
from typing import Union

def sum_xy(x: Union[int, float], y: Union[int, float]) -> Union[int, float]:
    return x + y


# after
def sum_xy(x: int | float, y: int | float) -> int | float:
    return x + y
```

## Type Aliases

Another bit of sugar is the ability to explicitly define type aliases. Static type checkers, as well as other developers, sometimes have problems distinguishing between variable assignments and type aliases.

Take, for example, the following two flavors of is_employee:

```py
# without type guards
def is_employee(user: User) -> bool:
    return isinstance(user, Employee)


# with type guards
from typing import TypeGuard

def is_employee(user: User) -> TypeGuard[Employee]:
    return isinstance(user, Employee)

```

So, with the second flavor of is_employee, when it returns True, the type checker will be able to narrow user down from User to Employee.

## Strict Argument for Zipping

What happens when you try to zip two iterables that don't have the same length?

```py
names = ["Jan", "Mike", "Marry", "Daisy"]
grades = ["B+", "A", "A+"]

for name, grade in zip(names, grades):
    print(name, grade)

"""
Jan B+
Mike A
Marry A+
"""
```

Iteration stops when the end of the shorter iterable is reached.

Python 3.10 introduces a new strict keyword parameter to ensure at runtime all iterables have the same length:

```py
names = ["Jan", "Mike", "Marry", "Daisy"]
grades = ["B+", "A", "A+"]

for name, grade in zip(names, grades, strict=True):
    print(name, grade)

# ValueError: zip() argument 2 is shorter than argument 1
```
