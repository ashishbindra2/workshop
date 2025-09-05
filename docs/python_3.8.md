# python 3.8 version enhasment

## The 3.8 version new features

1. Warlous Operator
2. Postional only Parameters
3. Fstring Support
4. iSqrt function
5. continue with finally
6. reversed dictionary
7. syntax warning

## python 3.8 version enhasment  related to f-string

* We can use `=` symbol f-string for self documentating expressions and it is useful for debugging purposes.

    ```py
    x = 10
    y = 10
    print(f'{x = }')  # => print(f'x = {x}')
    print(f'{y = }')  # => print(f'y = {y}')
    ```

* We can also use walrus operator (`:=`) inside f-string:

    ```py
    import math

    half_radious = 10

    print(f'The Area of circle with radius {(r := 2 * half_radious)} is {math.pi ** r*r }')
    ```

    ***Note:*** `()` -> This is important in walrous operator in this example other wise we will get error.

    ```py
    print(f'The Area of circle with radius {r := 2 * half_radious} is {math.pi ** r*r }')
    ```

* f - string can in python 3.6 version but `=` and `:=` operator are allowed inside f-string in python 3.8 version

* `%` -> formating and `str.formate()` ***Not Recommanded***.

f string
-------

* has performance

* concise
* less verbose
* more readable

```py
class Student:
    def __init__(self, name, rollno, marks):
        self.name = name
        self.rollno = rollno
        self.marks = marks
    def __str__(self):
        return f'Name: {self.name}, RollNo: {self.rollno}, Marks: {self.marks}'
    
    def __repr__(self):
        return f'Student Name: {self.name}, Student RollNo: {self.rollno}, Student Marks: {self.marks}'

s = Student('ashish',101,80)
print('Information-------> {}'.format(s))
print(f'Information-------> {s}')
print(f'Information-------> {s!r}')
```

### Expression inside f-string

We can pass expression inside f-string and those expressions will be evaluated at runtime
{8*8}

```py
print({8*8})
```

### How to use curly braces inside f-string

* { => replacement operator

* {{=> it is simple of '{'

```py
print(f'{{ is special symbol ')
print(f'{{{ is special symbol ')

```

### New Syntax Warning in python 3.8 version

* In python warning are Exception

* Python has a syntaxWarning that can warn about doubtful syntax,that is typically not syntaxerror

---

```
BaseException
    └── Exception
        └── Warning
            └── SyntaxWarning
```

1. `is` and `is not` operators are used for numbers and strings.
2. While creating larger collections, we may miss some elements.

---

### is and is not operators for numbers and strings

is operator vs == operator

* is operator meant for reference comparsion
* == operator meant for content comparsion
<br>

 `l1 = [10,20,30,40]`<br>
 `l2 = [10,20,30,40]`<br>
 `print(l1 is l2)`<br>
 `print(l1 == l2)`<br>

* A new SyntaxWarning added extraa in 3.8 version which will be raised if we use is and is not operator for number and string literals.
* It is highly recommended to use == operator instead of is for literal comparsion.
* While creating large collections, we may miss ',' to alert this, a new syntax warning was added to Python 3.8.

 ```
 print(6 is 6)
 print('a' is ' a')
 ```

* python 3.8  = > oct 14 2019
* python 3.9  = > oct 5 2020

More flexibility to programmer with new features

## 1. The Warlus operator:(sea hourse)

Syntax `:=`

* This operator released as the part of PEP 577
* PEP => Python Enhancement Proposals

* To assign values to the variable as the oasrt of expression itself

```py
# Assignment Expression
num = [10,20,30,40,50,60]
length = len(num)

if length > 3:
    print('List conatins more than 3 element')
    print('The length of the list is', length)

```

```py
num = [10,20,30,40,50,60]

if (n:=len(num)) > 3:
    print('List conatins more than 3 element')
    print('The length of the list is', length)
        
```

```py
# Example 2
heriones = []

herion = input('Enter your Favourit Herione ')

while herion != 'done':
    heriones.append(herion)
    herion = input('Enter your Favourit Herione ')

print(heriones)
```

```py
heriones = []

while (herion := input('Enter your Favourit Herione '))!= 'done':
    heriones.append(herion)

print(heriones)
```

```py
# Read data line by line from abc.txt file and print to the console.
# FileNotFoundError

f = open('abc.txt')
line = f.readline()

while line != '':
    print(line, end='')
    line = f.readline()

f.close()

```

The Walrus Operator is a new addition to Python 3.8 and higher. In this article, weâ€™re going to discuss the Walrus operator and explain it with an example.

### Introduction

Walrus Operator allows you to assign a value to a variable within an expression. This can be useful when you need to use a value multiple times in a loop, but donâ€™t want to repeat the...

```py
numbers = [1, 2, 3, 4, 5]
while (n := len(numbers)) > 0:
    print(numbers.pop())
```

```py

f = open('abc.txt')

while (line := f.readline()) != '':
    print(line, end='')

f.close()
```

### The main advantage of warlous Operator

* It won't do any new thing
* It just reduce length of code and readablity will be imporoved

## 2. Postional-only parameter

python 3.8 version
PEP 570

1. Postional argument
    * order and number both are implemented
2. keyword argument
    * By keyword (parameter name) (a=10, b=20), (b=20, a=10)
    * The number of argument must be match order is notimportant
3. default arguments:
    * `def sum(a=0,b=0)` argument with default value
    * `def sum(a=0,b) -- x after a arument, we cannot take non-default argument
4. varable length argument and all value will be converted into touple
    * def f(*args)
        -print(args)
    * *args and **kwargs

```py
def calc(a,b): # a,b parameter
    print(a+b)
    print(a-b)
    print(a*b)
 
calc(10,20) # arguments
# Interchangable we can use
```

### Function types

1. Postional arguments
2. Keyword arguments
3. default arguments
4. varable legth argument

```py
calc(20,30) # Postional argument
```

#### 1. The number of argument must be match and order

### Keyword only parameters (3.0 -Version)

* After *, all parameter will become keyword only paramter

* At the time of calling we should pass values by keyword only

```py
def f1(*,a,b):
    print(a,b)

f1(a=10, b=20) # valid
f1(10, 20) # TypeError: f1() takes 0 postional arguments but 2 were given
f1(10, b=20)  # TypeError: f1() takes 0 positional arguments but 1 positional argument (and 1 keyword-only argument) were given

```

```py
def f(a,*,b,c):
    """
    # For a we can pass value either by postional or keyword But
      for b,c compulosry we should use keyword
    """
    print(a,b,c)
```

```py
def f2(*,a=10,b,c): # correct
    ...
def f3(a=10,b,c,*): # error SyntaxError: non-default argument follows default argument
    ...
```

#### Positional only arguments: (3.8)

* We should pass values by postional only arguments

* / => Forword slash
* All paramters vefore /, will bwcome postional only paramters

```py
def f3(a,b,/):
    print(a,b)

f3(10,20)
f3(a=10,b=20)
```

#### Python 3.8 version as the past PEP 570

* a and b are postional only parameteers
* c and d are postional or keyword paramters
* e and f are keyword only paramters

```py
def f4(a,b,/,c,d,*,e,f):
    print(a,b,c,d,e,f)

f4(10,20,30,d=40,e=50,f=60)
f4(10,b=20,c=30,d=40,e=50,f=60)
f4(10,20,30,40,50,f=60)
```

#### f4(postional args,postional or keyword,keyword only args)

#### Problem without postional only argument

case - 1:

* Without effecting client, we cannont change parameter name based on our requirment

```py
def display(name, arg, roll):
    print(name, arg, roll)

display('Ravi',14,101)
display(name = 'Ravi', age = 14, roll = 101)
display('Ravi', 14, roll = 101)

```

#### If arguments are postional only, then we can change variable names

```py
def display(name, arg, roll,/):
    print(name, arg, roll)
```
