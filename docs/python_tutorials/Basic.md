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
