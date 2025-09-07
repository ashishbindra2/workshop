# F-String

## String Formating techniques

1. `%` - formatting => 1.0v
2. `str.formate()` => 2.6 Best for Dictionary
3. `f-string` => 3.6 Higly recommened because of concise code, readabilty,speed

## timeit module

- python inbulit module
- By using timeit module, we can measure execution tiome of small coding snippets

t = timeit.timeit(code,numbeeer =1000)

- numbers =1000 => execute ccode with number 10000 of times PVM take hwo much time it will retuen in sec

## example

```py
import timeit
t= timeit.timeit('print("hello")',number=1000)
print(f'The time taken {t} sec')
```

### Handling quotes in f-sting

```py
subject ='math'
a = 'a'
print(f''' The class of {subject} by "{a}" too good''')
```

### Processing dictionary data by f-string

performance wise f-string is grater Higly recommended to use f-string

### How to define multi line f-string

```py
name = "ashish"
age = 26

message = f'''
    name: {name},
    age: {age}
    '''
print(message)
```

### Python f-string calling a function

we can call function directly from f-string

```py
print(f'Name: {name.upper()}')
def mymax(a,b):
    max = a if a>b else b
    return max

a = input("a ")
b = input("b ")

print(f'The max of {a} and {b} is {mymax(a,b)}')
help(__repr__)
```

`__repr__` => String to Object
`__str__`  => Object to string

### Python f-string for objects

- `str.format()` method will always call str() method only.
- but in f-string, we can call either str() or repr() based on our requirment

```py
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"Person(name={self.name}, age={self.age})"

    def __str__(self):
        return f"{self.name}, {self.age} years old"

# Creating an instance of the Person class

person = Person("John", 30)

# Using f-string with __repr__()

print(f"Representation of person: {person!r}")

# Using f-string with __str__()

print(f"String representation of person: {person}")
```

The __repr__() method returns a string representation suitable for debugging and development. It is often used with !r in f-strings to call __repr__() explicitly.

The __str__() method returns a more user-friendly string representation. When using f-strings, the default string conversion is the same as calling __str__()

#### python 3.8 version enhasment  related to f-string

- We can use = symbol f-string for self documentating expressions and it is useful for debugging purposes.

```py
x = 10
y = 10
print(f'{x = }')  # => print(f'x = {x}')
print(f'{y = }')  # => print(f'y = {y}')
```

- We can also use walrus operator (`:=`) inside f-string:

```py
import math
half_radious = 10

print(f'The Area of circle with radius {(r := 2 * half_radious)} is {math.pi ** r*r }')

# *__Note:__* `()` -> This is important in walrous operator in this example other wise we will get error.

print(f'The Area of circle with radius {r := 2 * half_radious} is {math.pi ** r*r }')
```

- f - string can in python 3.6 version but `=` and `:=` operator are allowed inside f-string in python 3.8 version
- `%` -> formating and `str.formate()` *__Not Recommanded__*.
f string

-------

- has performance
- concise
- less verbose
- more readable

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
print({8*8})

### How to use curly braces inside f-string

- { => replacement operator
- {{=> it is simple of '{'

```py
print(f'{{ is special symbol ')

print(f'{{{ is special symbol ')
n=1000000000
print(f'{n:_}')
n=1000000000
print(f'{n:,}')
n=1000000000
print(f'{n:-}')
n: int = 1_000_000_000
print(n)
n: float = 1e9
print(n)
var: str = 'var'

print(f'{var: > 20}:')
print(f'{var: < 20}:')
var: str = 'var'

print(f'{var:>20}:')
print(f'{var:<20}:')
print(f'{var:20}:')
print(f'{var:^20}:')

# fill element

var: str = 'var'

print(f'{var:_>20}:')
print(f'{var:#<20}:')
print(f'{var:|^20}:')
print(f'{var:*^20}:')
```

```py

from datetime import datetime

now: datetime = datetime.now()

print(f'{now:%d.%m.%y (%H:%M:%S)}')
print(f'{now:%c}') #local date and time
print(f'{now:%I%p}') #12 p.m
n: float = 1234.5678
print(round(n, 2))
n: float = 1234.5678

print(f'Result: {n:.2f}')
print(f'Result: {n:.0f}')

print(f'Result: {n:,.3f}')
print(f'Result: {n:_.3f}')

a: int = 5
b: int = 10

my_var: str = "ashish"

print(f'{a + b = }')
```

```py

import string

print(string.ascii_letters)
print(string.digits)
print(string.punctuation)
print(string.printable)

#### Sort below string

file_paths = [
    'static\\pdf\\01 Adsolut initiatie\\page_1.pdf',
    'static\\pdf\\01 Adsolut initiatie\\page_10.pdf',
    'static\\pdf\\01 Adsolut initiatie\\page_11.pdf',
    'static\\pdf\\01 Adsolut initiatie\\page_12.pdf',
    'static\\pdf\\01 Adsolut initiatie\\page_13.pdf',
    'static\\pdf\\01 Adsolut initiatie\\page_14.pdf',
    'static\\pdf\\01 Adsolut initiatie\\page_15.pdf',
    'static\\pdf\\01 Adsolut initiatie\\page_16.pdf',
    'static\\pdf\\01 Adsolut initiatie\\page_17.pdf',
    'static\\pdf\\01 Adsolut initiatie\\page_18.pdf',
    'static\\pdf\\01 Adsolut initiatie\\page_19.pdf',
    'static\\pdf\\01 Adsolut initiatie\\page_2.pdf',
    'static\\pdf\\01 Adsolut initiatie\\page_20.pdf',
    'static\\pdf\\01 Adsolut initiatie\\page_21.pdf',
    'static\\pdf\\01 Adsolut initiatie\\page_22.pdf',
    'static\\pdf\\01 Adsolut initiatie\\page_23.pdf',
    'static\\pdf\\01 Adsolut initiatie\\page_24.pdf',
    'static\\pdf\\01 Adsolut initiatie\\page_25.pdf',
    'static\\pdf\\01 Adsolut initiatie\\page_26.pdf',
    'static\\pdf\\01 Adsolut initiatie\\page_27.pdf',
    'static\\pdf\\01 Adsolut initiatie\\page_28.pdf',
    'static\\pdf\\01 Adsolut initiatie\\page_29.pdf',
    'static\\pdf\\01 Adsolut initiatie\\page_3.pdf',
    'static\\pdf\\01 Adsolut initiatie\\page_30.pdf',
    'static\\pdf\\01 Adsolut initiatie\\page_4.pdf',
    'static\\pdf\\01 Adsolut initiatie\\page_5.pdf',
    'static\\pdf\\01 Adsolut initiatie\\page_6.pdf',
    'static\\pdf\\01 Adsolut initiatie\\page_7.pdf',
    'static\\pdf\\01 Adsolut initiatie\\page_8.pdf',
    'static\\pdf\\01 Adsolut initiatie\\page_9.pdf'
]

from faker import Faker
fake = Faker()

help(fake.phone_number)
faker.providers.phone_number()
```
