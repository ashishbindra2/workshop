# Python 3.13

source: <https://testdriven.io/blog/python313/>
It was released on October 7th, 2024
It will make your Python development even better

1. Improved interactive interpreter - e.g., multiline editing with history preservation
2. No-GIL, free-threaded Python - utilize all available processing power by running threads in parallel on all available CPUs
3. Improved error messages - more helpful error messages for common mistakes
4. Improved typing - `typing.ReadOnly` to mark read-only attributes inside typed dicts
5. Improved warnings - new w`arnings.deprecated()` decorator to emit warnings at runtime and type checking if a deprecated object/function/overload is used
6. Improved argparse - a new `deprecated` argument was added to support deprecation of command-line options, positional arguments, and subcommands

---

## 1. Improved Interactive Interpreter

The new REPL now supports calling REPL-specific commands just by name -- no need to call them as functions anymore.

**Python < 3.13:**

```py
>>> exit()
```

**Python >= 3.13:**

```py
>>> exit
```

**Note:**
The old way of calling them as functions still works.

You can now edit multiline statements in the REPL without losing the history of the previous lines.

This is a great improvement for debugging and testing code snippets.

**Using history with Python < 3.13**

Defining function:

```py
>>> def foo():
...     print('Hello')
```

Going through history with up arrow:

```py
>>>     print('Hello')
>>> def foo():
```

Using history with Python >= 3.13
Going through history with up arrow:

```py
>>> def foo():
...     print('Hello')
```

Now you can go up using uparrow  and eit the functions

Prompts and tracebacks are now colored by default. That makes everything much more readable.

## No-GIL, Free-threaded Python

The Global Interpreter Lock (GIL) is a mutex (or lock) that protects access to Python objects, preventing multiple threads from executing Python bytecodes at once.

This lock is necessary mainly because CPython's memory management is not thread-safe.

The GIL is controversial because it prevents multithreaded CPython programs from taking full advantage of multiprocessor systems in certain situations.

CPython finally comes with an option for execution with the GIL disabled.

For now, this is only experimental

To make use of it, you'll need to install a special version of Python. Anyhow, with that, you can utilize all available processing power by running threads in parallel on all available CPUs.

## Improved Error Messages

hey've improved error messages for some of the common mistakes. Also, the interpreter now uses color when showing errors inside the terminal. This will make debugging easier and more efficient.

```py
# math.py

import math

print(math.sqrt(25))

```

Python < 3.13:

```js
$ python math.py

AttributeError: partially initialized module 'math' has no attribute 'sqrt'
(most likely due to a circular import)
```

Python >= 3.13:

```
$ python math.py

AttributeError: module 'math' has no attribute 'sqrt'
(consider renaming 'math.py' since it has the same name as the standard library
module named 'math' and the import system gives it precedence)
```

Another example is when you provide an incorrect keyword argument to a function -- the interpreter will now try to suggest the correct one:

```py
#  hello.py

def say_hello(*, full_name):
    return f"Hello, {full_name}!"

print(say_hello(fullname="Python"))
```

Python < 3.13:

```
$ python hello.py

TypeError: say_hello() got an unexpected keyword argument 'fullname'
```

Python >= 3.13:

```
$ python hello.py

TypeError: say_hello() got an unexpected keyword argument 'fullname'.
Did you mean 'full_name'?
```

## Improved Typing

The new typing.ReadOnly type. It can be used to mark read-only attributes inside typed dicts.

This is a great way to ensure that some key is not modified by mistake.

```py
# song.py

from typing import ReadOnly, TypedDict

class Song(TypedDict):
   name: ReadOnly[str]
   band: ReadOnly[str]
   number_of_plays: int

def count_plays(s: Song) -> None:
   s["number_of_plays"] += 1  # OK
   s["name"] = "New Name"  # Error
```

```
$ python -m mypy song.py

song.py:11: error: ReadOnly TypedDict key "name"
TypedDict is mutated  [typeddict-readonly-mutated]
```

## Improved Warnings

Python 3.13 comes with the new warnings.deprecated() decorator.

It can be used to emit warnings at runtime if a deprecated object/function/overload is used.

This is a great way to inform users that some part of the code is deprecated and should be replaced with a new one.

```py
# integration.py

from warnings import deprecated

@deprecated("Use NewIntegration instead")
class LegacyIntegration:
    pass

class NewIntegration:
    pass

LegacyIntegration()

```

```
$ python integration.py

integration.py:12: DeprecationWarning: Use NewIntegration instead
  LegacyIntegration()
```

Type checkers will also complain when an object is decorated with the warnings.deprecated() decorator

## Improved argparse

It can be used to support deprecation of command-line options, positional arguments, and subcommands.

This is a great way to inform users that some part of the CLI is deprecated and should be replaced with a new one.

```py
# cli.py

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--old", help="Old option", deprecated=True, required=False)
parser.add_argument("--new", help="New option", required=False)

args = parser.parse_args()
```

```
$ python cli.py --old foo

cli.py:  warning: option '--old' is deprecated
```
