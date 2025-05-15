# Introduction to Python

## About Python

- Python is a general-purpose, high-level programming language.
- It was developed by **Guido van Rossum** in 1989 at the National Research Institute in the Netherlands.
- Python was officially released to the public on **February 20, 1991**.
- Python is highly recommended as a first programming language for beginners due to its simplicity.

---

## Examples

### Example 1: Print "Hello World"

**Java:**
```java
public class HelloWorld {
    public static void main(String[] args) {
        System.out.println("Hello World");
    }
}
```

**C:**

```c
#include<stdio.h>
void main() {
    printf("Hello World");
}
```

**Python:**

```python
print("Hello World")
```

---

### Example 2: Sum of Two Numbers

**Java:**

```java
public class Add {
    public static void main(String[] args) {
        int a, b;
        a = 10;
        b = 20;
        System.out.println("The Sum: " + (a + b));
    }
}
```

**C:**

```c
#include <stdio.h>

void main() {
    int a, b;
    a = 10;
    b = 20;
    printf("The Sum: %d", (a + b));
}
```

**Python:**

```python
a = 10
b = 20
print("The Sum:", (a + b))
```

---

## Origin of the Name "Python"

The name **Python** was inspired by the British comedy TV show *"Monty Python’s Flying Circus"* broadcasted by the BBC from 1969 to 1974.

---

## Language Influences

Guido van Rossum designed Python by borrowing features from various programming languages:

* **Functional programming**: C
* **Object-oriented programming**: C++
* **Scripting features**: Perl, Shell Script
* **Modular programming**: Modula-3
* Syntax is mostly derived from **C** and **ABC languages**.

---

## Applications of Python

Python can be used in a wide variety of areas:

1. Desktop Applications
2. Web Applications
3. Database Applications
4. Network Programming
5. Game Development
6. Data Analysis
7. Machine Learning
8. Artificial Intelligence
9. Internet of Things (IoT)

> **Note:**
> Python is used by companies like **Google**, **Microsoft**, **IBM**, **Yahoo**.
> It's also used in **YouTube**, **NASA**, and **New York Stock Exchange**.

---

## Features of Python

1. **Simple and Easy to Learn**

   * Python code reads like English.
   * Minimal syntax, around 30+ keywords.
   * Fewer lines of code for the same logic compared to other languages.

2. **Free and Open Source**

   * No license needed to use Python.
   * Source code is open for modification (e.g., Jython for Java integration).

3. **High-Level Language**

   * Programmer-friendly; no need to manage memory or security manually.

4. **Platform Independent**

   * Write once, run anywhere (PVM handles platform translation).

5. **Portable**

   * Code produces the same result across platforms.

6. **Dynamically Typed**

   * No need to declare variable types explicitly.
   * Type is inferred at runtime.

7. **Supports Both Procedural and Object-Oriented Programming**

8. **Interpreted Language**

   * Compilation handled by Python Interpreter.
   * Errors raised at runtime if any.

9. **Extensible**

   * Can integrate code from other languages for performance or legacy reuse.

10. **Embeddable**

* Python code can be embedded within other languages.

11. **Extensive Library Support**

* Large standard library with built-in functions and modules.

---

## Limitations of Python

1. **Performance**

   * Slower than compiled languages due to interpretation.

2. **Not Commonly Used for Mobile Development**

---

## Flavors of Python

| Flavor         | Description                                 |
| -------------- | ------------------------------------------- |
| CPython        | Standard implementation using C             |
| Jython/JPython | For Java applications (runs on JVM)         |
| IronPython     | For C#/.NET applications                    |
| PyPy           | JIT compiler support for faster performance |
| RubyPython     | Integrates Python with Ruby                 |
| AnacondaPython | Optimized for data processing and analytics |

---

## Python Versions

| Version    | Release Date  |
| ---------- | ------------- |
| Python 1.0 | January 1994  |
| Python 2.0 | October 2000  |
| Python 3.0 | December 2008 |

> **Note:**
> Python 3 does **not** provide backward compatibility with Python 2.
> Python 2 programs may not run on Python 3 without modifications.

**Current Common Versions:**

* Python 3.6.1
* Python 2.7.13

---

#### 56. Python Program to Catch Multiple Exceptions in One Line
```py title="Multiple exceptions as a parenthesized tuple" linenums="1"
string = input()

try:
    num = int(input())
    print(string+num)
except (TypeError, ValueError) as e:
    print(e)
```
#### 62. Python Program to Print Colored Text to the Terminal
### ![colored_terminal.png](attachment:colored_terminal.png)
```py
# Example 1: Using ANSI escape sequences
print('\x1b[38;2;5;86;243m' + 'Programiz' + '\x1b[0m')
```

##### Let's understand the escape code \x1b[38;2;5;86;243m.

- \x1b calls a function. You can also use \033 for the same purpose.
- 38;2;r;g;b helps to set RGB color. 5;86;243 are the rgb color for blue (the color of the logo of Programiz).
- m is the function name. Here, m means SGR (Select Graphics Rendition) function.
```py
# Example 2: Using python module termcolor
from termcolor import colored

print(colored('ashish', 'blue'))
```
```py
# Example 2: Using python module termcolor
from termcolor import colored

print(colored('bindra', 'green'))
```

#### 74. Python Program to Get the Class Name of an Instance
```py title ="Example 1: Using __class__.__name__"
class Vehicle:
    def name(self, name):
        return name

v = Vehicle()
print(v.__class__.__name__)
```
#### 76. Python Program to Differentiate Between type() and isinstance()
#### 79. Python Program to Represent enum
#### 80. Python Program to Return Multiple Values From a Function
#### 88. Python Program to Compute the Power of a Number
#### 89.  Python Program to Count the Number of Digits Present In a Number
