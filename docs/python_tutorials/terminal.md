
### 62. Python Program to Print Colored Text to the Terminal

![alt text](img/colored_terminal.png)

```py
# Example 1: Using ANSI escape sequences
print('\x1b[38;2;5;86;243m' + 'Programiz' + '\x1b[0m')
```

#### Let's understand the escape code \x1b[38;2;5;86;243m

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
