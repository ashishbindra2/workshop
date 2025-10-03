# Functions

- If a group of statments is repeatedly required then it not recommmended to write theses stements everytime serately.
- We have to define these statments as a single unit and we can call that unit any number of times  based on our requirment without rewriting.
- This unit is nothing but function

The main advantage of a function is code resablity.

Note: In other languages functions are know as methods, procdures, subroutins etc

Python supports two types of function

1. built in dunctions
2. User defined dunction

## 1. Build in functions

THe functions which are coming along with python software automatically, are called build in functions or predefined functions

eg:

```py
id()
type()
input()
eval()
```

etc..

## 2. User Defined functions

The functions which are developed by programmer explicity
to business requirments are called user defined functions:

Syntax to create user defined functions:

```py
def sunction_name(paramerters):
    """
    doc string
    """
    pass
    return value # optional
```

While creating function awe can use 2 keywords

1. def (mandatory)
2. return (optional)

### 1. Write a function to print Hello usinf dunction

```py
def wish():
    print("Helow Good Morning")

wish()
wish()
wish()
```

## Parameters / Arguments

Paramerters are inputs to the function.

- If a function contains paramerters thrn at the time of calling, compulsory we should provide values otherwise we will get error.

### Write a function to take name of student as input and print widsh msg by name

```py
def wish(name):
    print(f"Hello, {name} Good Morning")

widh("AShish")
widh("Bindra")
```

## Return statement

Function can take input values as paramters and executes busines logic and return output to caller with return statement.

```py
def add(x,y):
    return x + y

re = add(10 + 20)
print(f"The sum is {re}")
```

If we are not writing return statemetn then default return value is None

### Write a function to find factorial of given number?

```py
def fact(num):
    reult = 1
    while num >=1:
        result = result * num
        num = num - 1
    
    return result

fact(5)
```

## Returning multiple values from a function

Python, a function can return any number of values

```py
def sum_sub(a,b):
    sum = a + b
    sub = a - b

    return sum, sub

x, y = sum_sub(100,50)

print("The sum is:", x)
```

## Types of arguments

```def f1(a,b):
------
------
------
f1(10,20)
```

a,b are formal arguments where as 10,20 are actual arguments

There are 4 types are actual arguments are allowed in Python.

1. positional arguments
2. keyword arguments
3. default arguments
4. Variable length arguments

---

1. positional arguments:

These are the arguments passed to function in correct positnal order

```py

def sub(a, b):
    print(a-b)

sub(100,200)
sub(200,100)
```

The number of arguments and position of arguments must be matched. If we change the
order then result may be changed.

If we change the number of arguments then we will get error.

2. keyword arguments:
We can pass argument values by keyword i.e by parameter name.

```py
def wish(name,msg):
    print("Hello",name,msg)
wish(name="Ashish",msg="Good Morning")
wish(msg="Good Morning",name="ashish")
```

Here the order of arguments is not important but number of arguments must be matched

We can use both positional and keyword arguments simultaneously. But first we have to take positional arguments and then keyword arguments,otherwise we will get syntaxerror.

```py
def wish(name,msg):
print("Hello",name,msg)
wish("Durga","GoodMorning") ==>valid
wish("Durga",msg="GoodMorning") ==>valid
wish(name="Durga","GoodMorning") ==>invalid
```
