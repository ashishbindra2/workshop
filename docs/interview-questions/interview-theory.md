# Python Interview

Why Should You Hire Me?
Why Did You Leave Your Last Job?
Why Should We Hire You?

## Why Python?

- Python is a general purpose high level programming language.
- Python was developed by Guido Van Rossam
- Python is an interpreted language
- Dynamic: Type of the variable is determined only during runtime

General purpose = Python is versatile and can be applied to almost any kind of software development, not tied to just one field.

### Interpreded?

- An interpreter allows the code to run line by line rather than being compiled into machine language

High level: python is easy to read mange meomery for you, works on any system
Theory Questions:

### 1. Difference between List, Tuple and Array

|sno| LIST | Tuple |
|---|------|-------|
|1|List is mutable|Tuple is immutable|
|2|List is a container to contain different types of objects and is used to iterate objects.|Tuple is also similar to list but contains immutable objects.|
|3|Syntax li = ['a', 'b', 'c', '123'] | tuples = ('a','b','c',123)|
|4| List iteration is slower|Tuple processing is faster than list|
|5|Lists consume more memory|Tuple consume less memory|
|6|Operations like insertion and detection are better performed|Elementscan accessed better|

|sno| LIST | Array |
|---|------|-------|
|1|The list can store the value of different types|It can only consist of value of same type.|
|2|The list cannot handle the direct arithmetic operations| It can directly handle arithmetic operation|
|3|The list are build in data structure so we don't need to import it.|We need to import the array before work with the array|
|4|The lists are less compatible then the array to store the data|An array are much compatible than thelist.|
|5|It consumes a large memory.|It is more compact in memory size comparatively list|
|6| It is suitable for storing the longer sequence of the data item| It is suitable for storing shorter sequence of data items|
|7| We can print the entire list using explicit looping|We can print the entire list without using explicit looping|

### 2. Lambda function with example

Lambda Function:

- A Lambda Function in Python programming is an anonymous function or a function having no name.
- It is a small and restricted function having no more than one line.
- Just like a normal function, a Lambda function can have multiple arguments with one expression.

Syntax:

`lambda arguments : expression`

```py
# Add 5 to argument a, and return the result:

x = lambda a : a + 5
print(x(5))

# Output: 
# 10
```

Example 2:

Find Cubes Of All Elements In A List.

```py


list1 = [1, 2, 3, 4, 5, 6, 7]
res = list(map(lambda x: x ** 3, list1))
print(res)

Output:
[1, 8, 27, 64, 125, 216, 343]
```

### 3. Difference between append() and expand() in list

Append():.

- append() adds an element to a list
- append() adds its argument as a single element to the end of a list.
- The length of the list itself will increase by one.

Extend():

extend() concatenates the first list with another list/iterable.
extend() iterates over its argument adding each element to the list, extending the list.
The length of the list will increase by however many elements were in the iterable argument.

In Case Of String Value

```py
list1 = [1,2,3]
list2 = [5,6,7]
# Append():.

list1.append('AB')
print(list1)

Output:
[1, 2, 3, 'AB’]

# Extend():.

list1.extend(‘AB’)
print(list1)

Output:
[1, 2, 3, ‘A’, ‘B’]

```

In Case Of List Value

```py
list1 = [1,2,3]
list2 = [5,6,7]
# Append():.

list1.append(list2)
print(list1)

Output:
[1, 2, 3, [5, 6, 7]]
# Extend():.

list1.extend(list2)
print(list1)

Output:
[1, 2, 3, 5, 6, 7]
```

In Case Of Integer Value

```py
list1 = [1,2,3]
list2 = [5,6,7]
# Append():.

list1.append(4)
print(list1)

Output:
[1, 2, 3, 4]
Extend():.


list1.extend(4)
print(list1)

Output:
Traceback (most recent call last):
  File "main.py", line 5, in <module>
    list1.extend(4)
TypeError: 'int' object is not iterable
```

### 2. What is Decorator? Explain With Example

A Decorator is just a function that takes another function as an argument, add some kind of functionality and then returns another function.
All of this without altering the source code of the original function that you passed in.

Decorator Coding Example

```py
def decorator_func(func):
 def wrapper_func():
  print("wrapper_func Worked")
  return func()
 print("decorator_func worked")
 return wrapper_func

def show():
 print("Show Worked")
decorator_show = decorator_func(show)
decorator_show()


#Alternative
@decorator_func
def display():
 print('display 
worked')
display()

```

Output:
decorator_func worked
wrapper_func Worked
Show Worked
decorator_func worked
wrapper_func Worked
display worked

## 9. What Does Python Support? -  Call By Reference OR Call By Value

Python utilizes a system, which is known as “Call by Object Reference” or “Call by assignment”.

In the event that you pass arguments like whole numbers, strings or tuples to a function, the passing is like call-by-value because you can not change the value of the immutable objects being passed to the function.

Whereas passing mutable objects can be considered as call by reference because when their values are changed inside the function, then it will also be reflected outside the function.

```py
Example 1: 

s1 = "Geeks"
def test(s1):
 s1 = "GeeksforGeeks"
 print("Inside Function:", s1)
 
test(s1)
print("Outside Function:", s1)

Output:
Inside Function: GeeksforGeeks
Outside Function: Geeks
```

Example 2:

```py

def add_more(list):
 list.append(50)
 print("Inside Function", list)

mylist = [10,20,30,40]
add_more(mylist)
print("Outside Function:", mylist)

Output:
Inside Function [10, 20, 30, 40, 50]
Outside Function: [10, 20, 30, 40, 50]
```

Binding Names to Objects: In python, each variable to which we assign a value/container is treated as an object. When we are assigning a value to a variable, we are actually binding a name to an object.

```py
Example 3: 

a = "first"
b = "first"

print(id(a))
print(id(b))
print(a is b)

Output:
110001234557894
110001234557894
True
```

```py
Example 2: 

a = [10, 20, 30]
b = [10, 20, 30]

print(id(a))
print(id(b))
print(a is b)

Output:
541190289536222
541190288737777
False
```

The output of the above two examples are different because the list is mutable and the string is immutable.
An immutable variable cannot be changed once created. If we wish to change an immutable variable, such as a string, we must create a new instance and bind the variable to the new instance.
Whereas, mutable variable can be changed in place.

### 4. Exception handling in Python

 ```py
try:
  # Some code...!
except:
  # Optional Block
  # Handling of exception (if required)
else:
  # Some code
  # Execute if no exception
finally:
  # Some code....always executed
 ```

try: This block will test the exceptional error to occur.

Except: Here you can handle the error

Else: If there is no exception then this block will be executed.

finally: Finally block always get executed either except is generated or not

### 5. Decoration in detail with an example(customazied decoration, parameterized decorator). Add two numbers using the decorator

A Decorator is just a function that takes another function as an argument, add some kind of functionality and then returns another function.
All of this without altering the source code of the original function that you passed in.

Decorator Coding Example

```py
def decorator_func(func):
 def wrapper_func():
  print("wrapper_func Worked")
  return func()
 print("decorator_func worked")
 return wrapper_func

def show():
 print("Show Worked")
decorator_show = decorator_func(show)
decorator_show()


#Alternative
@decorator_func
def display():
 print('display 
worked')
display()
```

Output:
decorator_func worked
wrapper_func Worked
Show Worked
decorator_func worked
wrapper_func Worked
display worked

A Decorator is just a function that takes another function

```py
def addTwoNumbers(a, b):
    c=a+b
    return c

c=addTwoNumber(4, 5)
 
print("Addition of two numbers=", c)

#Addition of two numbers=9
```

Now our aim is to modify the behavior of addTwoNumbers() without changing function definition and function call.

### What function behavior do we want to change?

We want addTwoNumbers function should calculate the sum of the square of two numbers instead of the sum of two numbers.  Here is a simple decorator to change the behavior of the existing function.a

```py
def decorateFun(func): 
    def sumOfSquare(x, y): 
        return func(x**2, y**2) 
    return sumOfSquare 

@decorateFun
def addTwoNumbers(a, b): 
    c = a+b 
    return c 

c = addTwoNumbers(4,5) 
print("Addition of two numbers=", c)

#Addition of two numbers=41
```

The below simple program is equivalent to the above decorator example. Here we are changing the function call.

```py
def decorateFun(func): 
    def sumOfSquare(x, y): 
        return func(x**2, y**2) 
    return sumOfSquare 

def addTwoNumbers(a, b): 
    c = a+b 
    return c 

obj=decorateFun(addTwoNumbers) 
c=obj(4,5) 
print("Addition of square of two numbers=", c)


# Addition of square of two numbers=41
```

Source: <https://www.csestack.org/python-decorators/>

### 6. Abstraction. How to define abstract class/function?

Abstraction in Python:

Abstraction is used to hide the internal functionality of the function from the users. The users only interact with the basic implementation of the function, but inner working is hidden. User is familiar with that "what function does" but they don't know "how it does."
In simple words, we all use the smartphone and very much familiar with its functions such as camera, voice-recorder, call-dialing, etc., but we don't know how these operations are happening in the background. Let's take another example - When we use the TV remote to increase the volume. We don't know how pressing a key increases the volume of the TV. We only know to press the "+" button to increase the volume.

That is exactly the abstraction that works in the object-oriented concept.

Why Abstraction is Important?
In Python, an abstraction is used to hide the irrelevant data/class in order to reduce the complexity. It also enhances the application efficiency. Next, we will learn how we can achieve abstraction using the Python program.

Abstraction classes in Python
In Python, abstraction can be achieved by using abstract classes and interfaces.
A class that consists of one or more abstract method is called the abstract class. Abstract methods do not contain their implementation. Abstract class can be inherited by the subclass and abstract method gets its definition in the subclass. Abstraction classes are meant to be the blueprint of the other class. An abstract class can be useful when we are designing large functions. An abstract class is also helpful to provide the standard interface for different implementations of components. Python provides the abc module to use the abstraction in the Python program. Let's see the following syntax.
Syntax
from abc import ABC  
class ClassName(ABC):  
We import the ABC class from the abc module.

Abstract Base Classes
An abstract base class is the common application program of the interface for a set of subclasses. It can be used by the third-party, which will provide the implementations such as with plugins. It is also beneficial when we work with the large code-base hard to remember all the classes.

Working of the Abstract Classes:
Unlike the other high-level language, Python doesn't provide the abstract class itself. We need to import the abc module, which provides the base for defining Abstract Base classes (ABC). The ABC works by decorating methods of the base class as abstract. It registers concrete classes as the implementation of the abstract base. We use the @abstractmethod decorator to define an abstract method or if we don't provide the definition to the method, it automatically becomes the abstract method. Let's understand the following example.

```py
Example -
from abc import ABC, abstractmethod   
class Car(ABC):   
    def mileage(self):   
        pass  
  
class Tesla(Car):   
    def mileage(self):   
        print("The mileage is 30kmph")   
class Suzuki(Car):   
    def mileage(self):   
        print("The mileage is 25kmph ")   
class Duster(Car):   
     def mileage(self):   
          print("The mileage is 24kmph ")   
  
class Renault(Car):   
    def mileage(self):   
            print("The mileage is 27kmph ")  
# Driver code   
t= Tesla ()   
t.mileage()   
  
r = Renault()   
r.mileage()   
  
s = Suzuki()   
s.mileage()   
d = Duster()   
d.mileage()  



Output:
The mileage is 30kmph
The mileage is 27kmph 
The mileage is 25kmph 
The mileage is 24kmph

```

Explanation -
In the above code, we have imported the abc module to create the abstract base class.
We created the Car class that inherited the ABC class and defined an abstract method named mileage().
We have then inherited the base class from the three different subclasses and implemented the abstract method differently.
We created the objects to call the abstract method.

Source: <https://www.javatpoint.com/abstraction-in-python>

### 7. What do you mean by MRO? **

- MRO stands for Method Resolution Order
- MRO is a concept used in inheritance.
- It is the order in which a method is searched for in a classes hierarchy and is especially useful in Python because Python supports multiple inheritance.
- In Python, the MRO is from bottom to top and left to right.
This means that, first, the method is searched in the class of the object. If it’s not found, it is searched in the immediate super class.
- In the case of multiple super classes, it is searched left to right, in the order by which was declared by the developer.

For example:
 def class C(B,A):

In this case, the MRO would be C -> B -> A.

Since B was mentioned first in class declaration, it will be searched first while resolving a method.

```py
Example 1:
class A:
  def method(self):
    print("A.method() called")

class B(A):
  def method(self):
    print("B.method() called")

b = B()
b.method()
```

This is a simple case with single inheritance.
In this case, when b.method() is called, it first searches for the method in class B.
In this case, class B had defined the method; hence, it is the one that was executed.
In the case where it is not present in B, then the method from its immediate super class (A) would be called.
So, the MRO for this case is: B -> A

```py
Example 2:
class A:
  def method(self):
    print("A.method() called")

class B:
  pass

class C(B, A):
  pass

c = C()
c.method()
```

The MRO for this case is:
C -> B -> A
The method only existed in A, where it was searched for last.

Source: <https://www.educative.io/edpresso/what-is-mro-in-python>

```py
Example 3:
class A:
  def method(self):
    print("A.method() called")

class B:
  def method(self):
    print("B.method() called")

class C(A, B):
  pass

class D(C, B):
  pass

d = D()
d.method()

```

The MRO for this can be a bit tricky.
The immediate superclass for D is C, so if the method is not found in D, it is searched for in C.
However, if it is not found in C, then you have to decide if you should check A (declared first in the list of C’s super classes) or check B (declared in D’s list of super classes after C).
In Python 3 onwards, this is resolved as first checking A.

So, the MRO becomes:

D -> C -> A -> B

### 8. What do you mean by GIL?

- The Global Interpreter Lock of Python allows only one thread to be executed ata time. It is often a hurdle, as it does not allow multi-threading in python to save time
- The python gil in simple word is a mutex (a lock) that allow only one thread to hold the control of the Python Interpreter
- This means the only one thread can be in state of execution at any point in time. The impact of gil is not visible to developer who execute single thread prohrams but it can be bottlenck in CPU and multi thread code.
- Since the GIL allows only one thread to execute at a time even in a multi-threaded architecture with more than one CPU core the GIL has gained a reutation as an infamous feture of python
- GIL in python doesnot allow mulithreading which can  sometimes be considered as a disadvantage.

### 9. With statement/ Context managers. Example

### 10. Difference between static and class methods

|Class  Method | Static Method |
|--------------|---------------|
|The class method takes cls (class) as first argument.|The static method does not take any specific parameter.|
|Class method can access and modify the class state.|Static Method cannot access or modify the class state.|
|The class method takes the class as parameter to know about the state of that class.|Static methods do not know about class state. These methods are used to do some utility tasks by taking some parameters.|
|@classmethod decorator is used here.|@staticmethod decorator is used here.|

### 11. Is Python A Fully Object Oriental Language?

- Python supports all the concept of "object oriented programming" but it is NOT fully object oriented because - The code in Python can also be written without creating classes.
- The answer is simply philosophy. Guido doesn't like hiding things, and many in the Python community agree with him.
- While it borrows heavily from the OOP language, it is also at the same time functional, procedural, imperative, and reflective.
- Python doesn't support strong encapsulation, which is only one of many features associated with the term "object-oriented".
- Python doesn’t support Interfaces

### 14. Explain OOPS Concept In Python

Like other general-purpose programming languages, Python is also an object-oriented language since its beginning. It allows us to develop applications using an Object-Oriented approach. In Python, we can easily create and use classes and objects.
An object-oriented paradigm is to design the program using classes and objects. The object is related to real-word entities such as book, house, pencil, etc. The oops concept focuses on writing the reusable code. It is a widespread technique to solve the problem by creating objects.
Major principles of object-oriented programming system are given below.

- Class
- Object
- Method
- Inheritance
- Polymorphism
- Data Abstraction
- Encapsulation

### 1. Difference Between List and Dictionary

|no|LIST|DICT|
|--|----|----|
|1|Lists are the collection of various elements (Heterogeneous ).
|Dictionary are collection of elements in the hashed structure as key-value pairs.|
|2|List is mutable in nature.|It is also mutable, but keys do not allow duplicates.|
|3| Placing all the elements inside square brackets [], separated by commas(,)
 list = ['a', 'b', 'c', 1,2,3]|Syntax:  Placing all key-value pairs inside curly brackets({}), separated by a comma. Also, each key-pair is separated by a semi-colon (:)
dict = {1: 'Apple', 2: 'Orange', 3: 'Mango'}|
|4|Indices are integer values starts from value 0.|The keys in the dictionary are of any data type|
|5|We can access the elements using the index value|We can access the elements using the keys|
|6|The default order of elements is always maintained|No guarantee of maintaining the order|
|7|List object is created using list() function|Dictionary object is created using dict() function|

### 3. Can We Use List Or Tuple As A Key In Dictionary?

- NO, List Can’t Be Used As Key In Dictionary
- NO, List Can’t Be Used As Key In Dictionary
- NO, List Can’t Be Used As Key In Dictionary

---

- Dictionaries are indexed by keys.
- Those Keys can be any immutable type i.e strings and numbers can always be keys.
T- uples can be used as keys if they contain only strings, numbers, or tuples.
- If a tuple contains any mutable object either directly or indirectly, it cannot be used as a key.
- You can’t use lists as keys, since lists can be modified in place using index assignments, slice assignments, or methods like append() and extend().

Tuple As Key

```py
tuple1 = (1,2,3)
tuple2 = (2,3,4)

d1 = {tuple1: 'First', tuple2: 'Second'}
print(d1)

OUTPUT:
{(1, 2, 3): 'First', (2, 3, 4): 'Second'}
```

List As Key

```py
list1 = [1,2,3]
list2 = [2,3,4]

d1 = {list1: 'First', list2: 'Second'}
print(d1)


OUTPUT:

Traceback (most recent call last):
  File "main.py", line 10, in <module>
    d1 = {list1: 'First', list2: 'Second'}
TypeError: unhashable type: 'list'
```

Tuple Having List As Key

```py

tuple1 = (1,2,3,[6,5,4])
tuple2 = (2,3,4)

d1 = {tuple1: 'First', tuple2: 'Second'}
print(d1)



OUTPUT:

Traceback (most recent call last):
  File "main.py", line 4, in <module>
    d1 = {tuple1: 'First', tuple2: 'Second'}
TypeError: unhashable type: 'list'
```

### 4. When To Use List And When To Tuple In Python?

- If you have data which is not meant to be changed in the first place, you should choose tuple data type over lists.

- And if you have data which is meant to be changed in the first place, you should choose list data type over tuple.

LIST

- Lists are mutable
List is a container to contain different types of objects and is used to iterate objects.
Syntax Of List
 list = ['a', 'b', 'c', 1,2,3]
List iteration is slower
Lists consume more memory
Operations like insertion and deletion are better performed.

Tuple
Tuples are immutable
Tuple is also similar to list but contains immutable objects.
Syntax Of Tuple
tuples = ('a', 'b', 'c', 1, 2)
Tuple processing is faster than List.
Tuple consume less memory
Elements can be accessed better.

## 5. Why Python Is Called As Dynamic Typed Programming

      Language OR What Is Duck Typing?
OTE: The "Duck typing" name comes from the phrase, “If it walks like a duck and it quacks like a duck, then it must be a duck.”

Python don't have any problem even if we don't declare the type of variable.
It states the kind of variable in the runtime of the program.
Python also take cares of the memory management which is crucial in programming. So, Python is a dynamically typed language.

# variable a is assigned to a string

a ="NitMan Talks"
print(type(a))
  
Output: <class 'str'>

# variable a is assigned to an integer

a = 7
print(type(a))

Output: <class 'int'>

6. What If We Don't Use “With” Statement
If We Don't use "WITH" Statement, We need to close the opened file manually but using close().

```py
In Case Of open():
file = open("hello.txt", "w")
file.write("Hello, World!")
file.close()
```

```py
# Safely open the file
file = open("hello.txt", "w")
try:
    file.write("Hello, World!")
finally:
    file.close()
```

```py
with open("hello.txt", "w") as file:
    file.write("Hello, World!")
```

2 Internal functions called in "WITH" Statement

.__enter__() is called by the with statement to enter the runtime context.
.__exit__() is called when the execution leaves the with code block.

7. Why Python Is Called As An Interpreted Language?
Interpreted simply means your code run line by line. While in compiled language whole program compiled at once.

In compilation, source code is first converted to object code and then to the machine code.

You can see that in a compiled language your whole program compiled at once and give the output.

But in interpreted language, every single line is converted to machine code directly. That's why Python is very slow, because it interpret one line at a time.

You have seen that if, you run code in Python and do any mistake at the bottom of your python code. And you execute the code then it will give you output till the correct code part and the remaining part gives the error in a console window where you do the error. Because the interpreted language executes line by line instead of executing the whole program at once.

But, the same thing in a compiled language you always get the error. Your whole code must be correct for the execution of the program.

## Q1. Difference Between List and Tuple in Python**

| __Aspect__           | __List__                             | __Tuple__                           |
|-----------------------|---------------------------------------|--------------------------------------|
| __Definition__        | Group of Comma separeated Values within Square Brackets and Square Brackets are mandatory. Eg: `i = [10, 20, 30, 40]`.        | a Group of Comma separeated Values within Parenthesis and Parenthesis are optional. Eg: `t = (10, 20, 30, 40)` `t = 10, 20, 30, 40.`     |
| __Syntax__            | Defined using square brackets: `[ ]` | Defined using parentheses: `( )`    |
| __Mutability__        | Mutable: Can add, remove, or modify elements. | Immutable: Cannot change after creation. |
| __Performance__       | Slower due to mutability.            | Faster due to immutability.         |
| __Use Case__          | Suitable for collections that may change. | Suitable for fixed collections (e.g., coordinates). |
| __Size__              | Can dynamically grow or shrink.      | Fixed size once created.            |
| __Methods__           | Supports methods like `.append()`, `.remove()`, `.sort()`. | Limited methods: Only `.count()` and `.index()`. |
| __Memory Usage__      | Requires more memory due to dynamic resizing. | More memory-efficient.              |
| __Hashability__       | Not hashable; cannot be used as dictionary keys. | Hashable if all elements are hashable. |
| __Examples__          | `my_list = [1, 2, 3]`               | `my_tuple = (1, 2, 3)`              |

---

### __Key Points__

1. __Mutability__:
   - Lists are mutable, making them ideal for scenarios where data might need to change.
   - Tuples are immutable, ensuring data integrity and better performance in some cases.

2. __When to Use__:
   - Use __lists__ when flexibility is needed (e.g., managing a collection of user inputs).
   - Use __tuples__ for fixed data (e.g., coordinates, configuration constants).

3. __Hashable Tuples__:
   - A tuple can be used as a key in a dictionary if all its elements are hashable.

---

### __Example: List__

```python
my_list = [1, 2, 3]
my_list.append(4)  # Adds 4 to the list
print(my_list)  # Output: [1, 2, 3, 4]
```

### __Example: Tuple__

```python
my_tuple = (1, 2, 3)
# my_tuple[0] = 10  # Raises a TypeError because tuples are immutable
print(my_tuple)  # Output: (1, 2, 3)
```

In Python, the term __"hashable"__ is used to describe an object that has a hash value that remains constant during its lifetime. In the context of dictionaries, hashable objects are critical because they are used as __keys__.

---

### __Q2. What Does Hashable Mean?__

1. __Hash Value__:  
   A hash value is a fixed-size integer that uniquely identifies an object, generated by the `hash()` function.  

2. __Immutability__:  
   To be hashable, an object must be immutable. This ensures that its hash value does not change over time, which is a key requirement for dictionary keys.

3. __Equality and Hashing__:  
   Hashable objects must implement the `__hash__()` method to compute the hash value and the `__eq__()` method for equality checks. Python dictionaries use these methods to organize and retrieve keys efficiently.

---

#### __Why Hashable Is Important for Dictionaries__

- __Key Uniqueness__:  
  Dictionary keys must be unique. Python uses the hash value of a key to quickly determine where to store or find a value in the dictionary.
  
- __Efficient Lookups__:  
  The hash value allows the dictionary to find a key in __O(1)__ time complexity on average.

---

#### __Hashable Objects__

Objects that are immutable (and hence hashable) include:

- __Strings__:  

  ```python
  my_dict = {"name": "Alice"}  # 'name' is hashable
  ```

- __Numbers (int, float, etc.)__:  

  ```python
  my_dict = {42: "Answer"}  # 42 is hashable
  ```

- __Tuples (if all elements are hashable)__:  

  ```python
  my_dict = {(1, 2): "coordinates"}  # (1, 2) is hashable
  ```

---

#### __Unhashable Objects__

Objects that are mutable (and hence not hashable) include:

- __Lists__:  
  Lists are mutable and cannot be used as dictionary keys.  

  ```python
  my_dict = {[1, 2]: "List"}  # Raises TypeError: unhashable type: 'list'
  ```
  
- __Sets__:  
  Like lists, sets are mutable and unhashable.  

  ```python
  my_dict = {set([1, 2]): "Set"}  # Raises TypeError
  ```

---

#### __Custom Hashable Objects__

You can make a custom object hashable by defining the `__hash__()` and `__eq__()` methods.

#### Example

```python
class MyHashableClass:
    def __init__(self, value):
        self.value = value

    def __hash__(self):
        return hash(self.value)  # Use the hash of 'value'

    def __eq__(self, other):
        return isinstance(other, MyHashableClass) and self.value == other.value

# Using custom hashable object as dictionary key
key = MyHashableClass(42)
my_dict = {key: "Custom Object"}
print(my_dict[key])  # Output: Custom Object
```

---

#### __Key Points in the Context of Dictionaries__

1. A dictionary key __must be hashable__.
2. Hashable objects allow Python to store dictionary keys in a hash table for fast lookups.
3. If you attempt to use an unhashable object as a key, Python will raise a `TypeError`.

#### Example unhash

```python
# Hashable example
hashable_key = "name"
my_dict = {hashable_key: "Alice"}
print(my_dict[hashable_key])  # Output: Alice

# Unhashable example
unhashable_key = [1, 2, 3]  # A list
my_dict = {unhashable_key: "List"}  # Raises TypeError
```

By ensuring that objects used as dictionary keys are hashable, Python maintains the efficiency and reliability of its dictionary implementation.

## 3. Difference between slice and indexing

Both are used to accessing element in sequence like list or string.

- Indexing is when you refer to a specific item in a sequence by its postion or index.

```py
l = [10,20,30]

# indexing
a = l[10] #  to grab a single element
print(a)

# slice
print(l[:2])
```

slice[start: stop,step]

## 4. List comprehension

def: It is very easy and compact way of creating list objects from any iterable objects(like
list,tuple,dictionary,range etc) based on some condition.

Syntax:

`list=[expression for item in list if condition]`

List comprehension is a neat way to create new List using a simple one line syntax

Much more compact and readable alternative to use a traditional.

```py

# Square numbers in a range
l = [i**2 for i in range(5)]
print(l)

## even number

l = [i for i in range(5) if i%2 == 0]
```

## 5. What is lambda in python? Why is it used?

- lambda is a small, anonymus function.
- Sometimes we can declare a function without any name,such type of nameless functions are called __anonymous functions or lambda functions__.
- The main purpose of anonymous function is just for instant use(i.e for one time usage)
- Used as arguments for __map(), filter(), and sorted()__

Syntax: lambda argument_list : expression

```py
lambda x: x*2
```

```py
numbers = [1,2,3,4,5]
sq = list(map(lambda x:x *2,numbers))
print("Double numbers:",sq)
```

Note:

- Lambda Function internally returns expression value and we are not required to write
return statement explicitly.

- By using Lambda Functions we can write very concise code so that readability of the program will be improved.

1. filter():
  We can use filter() function to filter values from the given sequence based on some condition.

  `filter(function,sequence)`
  where function argument is responsible to perform conditional check sequence can be list or tuple or string.

  ```py
  l=[0,5,10,15,20,25,30]

  l1=list(filter(lambda x:x%2==0,l))
  print(l1) #[0,10,20,30]
  ```

2. map()

  For every element present in the given sequence,apply some functionality and generate new element with the required modification. For this requirement we should go for map() function.

  `map(function,sequence)`

  The function can be applied on each element of sequence and generates new sequence.

  ```py
  l=[1,2,3,4,5]
  l1=list(map(lambda x:2*x,l))
  print(l1) #[2, 4, 6, 8, 10]
  ```

3. reduce()

reduce() function reduces sequence of elements into a single element by applying the
specified function.

reduce(function,sequence)
reduce() function present in functools module and hence we should write import
statement.

### all(iterable)

Returns True if every element in the iterable is truthy (not False, 0, None, '', etc.).

If even one element is falsy → returns False.

Empty iterable → returns True (vacuous truth).

```py
print(all([True, True, True]))       # True
print(all([1, 2, 3]))               # True (all non-zero)
print(all([1, 0, 3]))               # False (0 is falsy)
print(all([]))                      # True (empty case)
```

### any(iterable)

Returns True if at least one element in the iterable is truthy.

Returns False only if all elements are falsy.

Empty iterable → returns False.

```py
print(any([False, False, True]))    # True
print(any([0, "", None, []]))      # False (all falsy)
print(any([0, 1, 0]))              # True (1 is truthy)
print(any([]))                     # False (empty case)
```

## How is memory managed in python?

Handled automatically by garbage collection and a private heap space.

- Garbage collectionn: Python has a build-n garbage collector that handles circular references
- private heap: This heap contains all python objects and data strucures
- reference counting: Every object in python has a reference count, which tracks how variables or objects refer to that object.

- "Python manages memory automatically using a combination of private heap space, reference counting, and garbage collection.

- All objects and data structures are stored in a private heap managed by the Python interpreter.

- Python uses reference counting to track how many references point to an object; when the count reaches zero, memory is freed.

- For circular references, Python uses a garbage collector to detect and clean up unreachable objects.

- Additionally, Python uses memory pools (PyMalloc) to efficiently allocate small objects and reduce fragmentation."

- Mention gc.collect() if asked how to trigger garbage collection manually.

Example:

```py
a = [1, 2, 3]
b = a  # reference count increases
del a
del b  # memory freed automaticall
```

## break and continue control folw statements

- Break statement terminate the loop

```py
for num in range(19):
  if num ==5:
    print("Found 5! Exiting the loop.")
    break
    print(num)
```

- Continue statement is used when you want to skip a part of the movie but watch the rest.

```py
for num in range(19):
  if num ==5:
    continue
    print(num)
```

- pass: To fill up empty block, in python empty block of code will raise an error, so comes in handy to avoid that.

## negative indexing

Nagative indexes allow you to access elements from the end of a sequence.

it counting backword insted of forword.

## How do you copy an object in python?

- Assignment operator:
  It creates a reference, making both variable point to the same object in memory

  ```py
  a = [1,2,3]
  b = a
  
  b[0] =11
  
  print(b) #  [11, 2, 3]
  print(a) #  [11, 2, 3]  
  ```

- shared reference:
  Changes made through one varibale affect the other since the same memory

- Need for copy:
  To create indepedent copies, Python offers the copy module for shallow and deep copies.

1. shallow Copy: Duplicates the object but copies reference for nested objects, so changes in nested objects affect both copies.

- Creates a new object, but nested objects are still references to the original.
- Use copy.copy() from the copy module or slicing for lists.

```py
from copy import copy

l1 =[1,2,[3,4],5]

# shallow copy
l2 = copy(l1)

l2[3] = 7
l2[2].append(6)

print(l2) # [1, 2, [3, 4, 6], 7]
print(l1) # [1, 2, [3, 4, 6], 7]
```

2. Deep Copy: Creates a fully independent copy, including all nested object, using deepcopy from copy module.

- Use copy.deepcopy():

```py
from copy import deepcopy

l1 =[1,2,[3,4],5]

# shallow copy
l2 = deepcopy(l1)

l2[3] = 8
l2[2].append(6)

print(l2) # [1, 2, [3, 4, 6], 8]
print(l1) # [1, 2, [3, 4], 5]
```

## What is PEP 8 in Python?

PEP 8 stands for Python Enhancement Proposal 8. It is the official style guide for Python code that provides conventions for writing clean, readable, and consistent code.

## test it You can also mention tools like flake8, pylint, or black that automatically check/fix PEP 8 compliance

## What does `*args` and `**kwargs` mean?

- Stands for `arguments`.
`*args` allows you to pass a variable number of postional arguments to a function. It collects these aruguments into a touple

- Stands for `keyword arguments`.
`**kwargs` allow you to pass a variable number of keyword aruments. It collects these keyword arguments. It collects thses keyword arguments into a dictionay.

whenever we are creating a function and we are not sure total number of argument it take then we pass these two

```py
def function(*args, **kwargs):
  print(args) # ()
  print(kwargs) # {}
```

## How are arguments passed by value or by reference in python

- pass by value: Copy of the actual object is passed.
- Pass by reference: Reference to the actual object is passed.
but in python arguments are not passed by value or refrence but through "pass-by-assignment to pass by object"

## __Q3. Difference Between `pop()` and `remove()` in Python__

| __Aspect__           | __`pop()`__                                      | __`remove()`__                                  |
|-----------------------|--------------------------------------------------|------------------------------------------------|
| __Functionality__     | Removes an element by its __index__.             | Removes an element by its __value__.           |
| __Parameters__        | Takes an optional index as an argument.          | Takes the value of the element as an argument. |
| __Return Value__      | Returns the removed element.                     | Does not return the removed element.           |
| __Default Behavior__  | If no index is provided, removes the last element. | Must specify the value to remove.              |
| __Error Handling__    | Raises an `IndexError` if the list is empty or index is out of range. | Raises a `ValueError` if the value is not found. |
| __Mutability__        | Modifies the original list.                      | Modifies the original list.                    |

---

#### __Example: `pop()`__

```python
# Using pop() with and without an index
my_list = [10, 20, 30, 40, 50]

# Remove and return the last element
removed_item = my_list.pop()
print(removed_item)  # Output: 50
print(my_list)       # Output: [10, 20, 30, 40]

# Remove and return the element at index 1
removed_item = my_list.pop(1)
print(removed_item)  # Output: 20
print(my_list)       # Output: [10, 30, 40]
```

---

#### __Example: `remove()`__

```python
# Using remove() to remove an element by value
my_list = [10, 20, 30, 40, 50]

# Remove the element with value 30
my_list.remove(30)
print(my_list)  # Output: [10, 20, 40, 50]

# Remove a value that doesn't exist (raises ValueError)
# my_list.remove(100)  # Raises ValueError: list.remove(x): x not in list
```

---

#### __Key Differences__

1. __Index vs Value__:
   - `pop()` removes an element based on its position (index).
   - `remove()` removes the first occurrence of a specific value.

2. __Return Value__:
   - `pop()` returns the removed element.
   - `remove()` does not return the removed element.

3. __Default Behavior__:
   - `pop()` without an index removes the last element.
   - `remove()` always requires a value to specify which element to remove.

---

#### __When to Use__

- Use `**pop()**` when:
  - You need to remove an element by index or retrieve the removed element.
- Use `**remove()**` when:
  - You know the value to be removed but not its index.

## Diferentiate between Sorted vs sort

1. sorted():

- Returns a new list
- leaving the original iterable unchanged.
- Works on any iterable
- Syntax: `sorted(iterable, key=None, reverse=False)`

  ```py
  nums = [4, 2, 1, 3]
  new_nums = sorted(nums)
  print(new_nums)  # [1, 2, 3, 4]
  print(nums)      # [4, 2, 1, 3] → original unchanged
  ```

2. sort():

- Modifies the list in place
- Modifies the original list in-place.
- Does not return a new list (returns None).
- works only on lists
- syntax: `list.sort(key=None,reverse=False)`

```py
nums = [4, 2, 1, 3]
nums.sort()
print(nums)  # [1, 2, 3, 4]
```

## Compile time error vs Runtime error

- compile time and runtime errors- are error that happen at different stagrs in the execution of a program.
- Compile-time error are detected before the code runs and are often related to typos or incorrect syntax
- Runtime error occur while the code is runing, usually due to issues like divding by zero or accessing out of bounds elements in a list.

## What are generator and decorators?

- Generator : returns n iterator
- they useful when dealting with large dataset or infinite sequences
- Gererators remeber their state between yield

- Definition: Special type of function that uses yield instead of return to produce values one at a time.
- They are iterators that generate values on the fly, saving memory (lazy evaluation).
Useful for working with large datasets, streams, or infinite sequences.

---

- decorator: modify a function without modifying the code
- They take function as arguments
- They wrap the code or extend fuctionality of a fucntion

```py

def decore(func):
  def wrapper():
    print("yoo")
    func()
@decore
def greet():
  print("hello")
```

---

## oops

## @property decorator

Python programming provides us with a built-in @property decorator which makes usage of getters and setters much easier in Object-Oriented Programming.
 a way to control access to an attribute by defining getter, setter and deleter methods. This enhances encapsulation and ensures better control over class attributes. Example:

 Creating properties in Python

 ```py
 class Alphabet:
    def __init__(self, value):
        self._value = value

    @property
    def value(self):
        print("Getting value")
        return self._value

    @value.setter
    def value(self, value):
        print("Setting value to " + value)
        self._value = value

    @value.deleter
    def value(self):
        print("Deleting value")
        del self._value

# Usage
x = Alphabet("Peter")
print(x.value)

x.value = "Diesel"
del x.value
```

## What is the difference between abstraction and encapulation?

- Abstraction is about hiding the complexity of a system
- Focuses on 'what' raather than how
- working of brakes in cars

```py
from abc import ABC, abstractmethod

class Animal(ABC):
  @abstractmethod
  def make_sound(self):
    pass
class Dog(Animal):
  def make_sound(self):
    print("Bark")
```

---

- Encapsulation restricts access to the private cariable or methods.
- It hides certain parts of an object to protext its internal details
- Mainly concerned with secuirty and protection

```py
class Car:
  def __init__(self):
    self.__speed = 0
  def accelerate(self, value):
    self.__speed += value
  def get_speed(self):
    return self.__speed

car = Car()
car.__speed
```

## Ehst is method overriding? How is it different from method overloading?

- Method overloading: multiple methods with the same name but different parameters
- Method overriding: the child class overrides the behavior of the parent class;s method

## How does inheritance work in python

## What is the significance of self in python classes?

- self refers to the current instance of the class.
- It's automatically passed when you call amethod, but you still need to define it explicitly.
- It's what differentiates instance attributes from local variables.

## What are class methods and static methods? How are they different from instance methods?

### class Method

- work with class itself(not individual instances).
- Require cls as their first parameter.
- can modify class-level attributes

## Explain the differences between a set and a dictionary

set
--

- Unordered: The items are not stored in a specific sequence.
- Unique: No duplicates are allowed.
- Mutable: You can add or remoce items.
- Efficient lookups: Checking if an item exists in a set is very fast.

Dictionary
---

- Key-value pairs: Each element consists of a unique key and a value.
- orderd: The order of insertion i spreserves.
- Keys must be unique: You cannot have two identical keys but values can be repeated.
- Efficient looks: Searching for a value usong keys is very fast.

## What is the time complexity of inserting elements in a Linked List?

Insertion in a LinkedList can happen in three commom ways:

1. At the beginning (Head)
2. At the end(tail)
3. In the middle (At a specific position)

- At the begining (head) - O(1)
- At the end(tail) - O(N)
- In the middle (At a specific position) - O(N)

## How do you find the middle element of a linked list in one pass?

The two-pointer technique: Slow and Fast Poiner

- The slow pointer moves one steps at a time
- The fast pointer moves two steps at a time

Good question
** ## Write a fumction that takes a string as input and returns the length of the longest substring that contains no repeatng character

ex 1
input: s = "abcabcbb"
output: 3
Explanation: This answer is  "abc", with the length of 3.

ex2:
input s = "bbbbbb"
output: 1

eample 4
input: s = "pwwkew"
output: 3

explaination: The answer is "wke", with the length of 3 Notice that the answer must be a substring "pwke" is a subsequence and not a substring.

## Knapspack problem (Dp)

examp;
a =[60,100,120]
b = [10,20,30]
c =50
op = 220

ex2
a = [10,20,30,40]
b = [12,13,15,19]

c =10
op = 0

given two interger array A and B of size N which represent lues and weights aassociated with N items respectively

Given an interger C which represents knapsack capacity

out maximum valur subset of A such that sum of the weights of this subs et is smaller than or equal to c

## Asteroid collison problem(stack)

### Q4. Write a Python function that will reverse a string without using the slicing operation or reverse() function

```py title="using for loop"
def reverse_string(data: str)-> str:
  result = ""
  for char in data:
    result = char + result
  return result

reverse_string("Testing a string")
```

```py title="using while loop"
text: str = "Ashish"
def reverse_string(text: str)-> str:
    n = len(text)-1
    result = ''
    while n>=0 :
        result= result + text[n]
        n-=1
    return result
print(reverse_string(text))
```

### Q5. Write a program to delete all constants from a given string. "Python and Data Science"

```py
def return_string(data):
  vowels = 'aeiouAEIOU'
  result = ''.join([char for char in data if not char.isalpha() or char in vowels])
  return result

return_string(data ="Python and Data Science")

```

### Q6. Write a program that will find sum of all the prime between 1 to N

```py
def is_prime(number):
  for i in range(2,number):
    if(number % i ==0):
      return False
    return True

def add(number):
  total = 0
  for i in range(2,number + 1):
    if is_prime(i):
      total = total + i
  return total
print(add(10))
```

### Q7. What is a Generator in Python?

A generator in Python is a special type of iterable that produces values one at a time using the yield keyword, rather than creating and storing all values in memory at once.

- Generators are a memory-efficient way to handle large datasets or infinite sequences.

### __Creating Generators__

#### __1. Generator Function__

- Generator is a function which is responsible to generate a sequence of values.
- We can write generator functions just like ordinary functions, but it uses yield keyword to return values

A function that uses the `yield` keyword to produce values one at a time.

```python
def my_generator():
    for i in range(5):
        yield i

# Using the generator
gen = my_generator()
print(next(gen))  # Output: 0
print(next(gen))  # Output: 1

for value in gen:
    print(value)  # Output: 2, 3, 4
```

#### __2. Generator Expression__

A compact way to create a generator, similar to list comprehensions but with parentheses instead of square brackets.

```python
gen = (x**2 for x in range(5))

print(next(gen))  # Output: 0
print(next(gen))  # Output: 1

for value in gen:
    print(value)  # Output: 4, 9, 16
```

---

### __Difference Between Generators and Lists__

| __Aspect__        | __Generator__                                      | __List__                                 |
|--------------------|---------------------------------------------------|------------------------------------------|
| __Memory Usage__   | Memory-efficient; generates values on the fly.    | Stores all elements in memory.           |
| __Performance__    | Faster for large datasets or infinite sequences.  | Slower for large datasets due to memory overhead. |
| __Modification__   | Cannot modify elements once created.              | Can modify elements.                     |

---

### __Advantages of Generators__

1. __Memory Efficiency__:
   - Suitable for working with large datasets or streams of data.
2. __Improved Performance__:
   - No need to compute all elements upfront; computation happens only when needed.
3. __Simplified Code__:
   - Easily represent infinite sequences (e.g., Fibonacci series, prime numbers).

---

### __Use Case Example: Generator for Infinite Sequence__

```python
def infinite_numbers():
    num = 0
    while True:
        yield num
        num += 1

gen = infinite_numbers()

print(next(gen))  # Output: 0
print(next(gen))  # Output: 1
print(next(gen))  # Output: 2
```

#### Generators vs Normal Collections wrt performance

```py

import random
import time
names = ['Sunny','Bunny','Chinny','Vinny']
subjects = ['Python','Java','Blockchain']

def people_list(num_people):
  results = []
  for i in range(num_people):
    person = {
      'id':i,
      'name': random.choice(names),
      'subject':random.choice(subjects)
    }
  results.append(person)
  return results
t1 = time.time()
people = people_list(10000000)
t2 = time.time()
print(f'Took {t2-t1}')

def people_generator(num_people):
  for i in range(num_people):
    person = {
      'id':i,
      'name': random.choice(names),
      'major':random.choice(subjects)
      }
  yield person

t1 = time.time()
people = people_generator(10000000)
t2 = time.time()

print(f'Took {t2-t1}')

```

#### Generators vs Normal Collections wrt Memory Utilization

Normal Collection:

```py
l=[x*x for x in range(10000000000000000)]
print(l[0])
```

> We will get MemoryError in this case because all these values are required to store in the memory.

Generators:

```py
g=(x*x for x in range(10000000000000000))
print(next(g))
Output: 0
```

>We won't get any MemoryError because the values won't be stored at the beginning
---

### __Conclusion__

Generators are a powerful tool for creating efficient, iterable objects that avoid memory overhead. Use them when working with large datasets, streaming data, or infinite sequences to improve performance and resource usage.

> create speed of function execting genrator

### Q8. What is decorator? Multiple decorator

### __What is a Decorator in Python?__

A __decorator__ in Python is a function that modifies the behavior of another function or method. It allows you to "wrap" another function to add or alter its functionality without changing its structure or code.

---

### __How Decorators Work__

1. A decorator takes a function as an argument.
2. It defines a nested wrapper function that modifies or enhances the behavior of the original function.
3. The wrapper function is returned and replaces the original function.

#### __Syntax__

```python
@decorator_name
def function_to_decorate():
    pass
```

The `@decorator_name` syntax is equivalent to:

```python
function_to_decorate = decorator_name(function_to_decorate)
```

---

### __Single Decorator Example__

```python
# Define a decorator
def greet_decorator(func):
    def wrapper(name):
        print("Hello!")
        func(name)
        print("Goodbye!")
    return wrapper

# Apply the decorator
@greet_decorator
def say_name(name):
    print(f"My name is {name}.")

# Call the function
say_name("Ashish")
```

__Output__:

```
Hello!
My name is Ashish.
Goodbye!
```

---

### __Multiple Decorators__

You can stack multiple decorators on a single function by applying them one after the other.

#### __Example of Multiple Decorators__

```python
# Define decorators
def bold_decorator(func):
    def wrapper():
        return f"<b>{func()}</b>"
    return wrapper

def italic_decorator(func):
    def wrapper():
        return f"<i>{func()}</i>"
    return wrapper

# Apply multiple decorators
@bold_decorator
@italic_decorator
def get_text():
    return "Hello, World!"

# Call the function
print(get_text())
```

__Output__:

```
<b><i>Hello, World!</i></b>
```

__Explanation__:

1. The `italic_decorator` is applied first, wrapping the function output in `<i>`.
2. The `bold_decorator` is applied next, wrapping the result of the first decorator in `<b>`.

---

### __Key Points About Multiple Decorators__

1. __Order of Execution__:
   - Decorators are applied from the bottom to the top, but their effects are executed from the top down.
   - In the above example:
     - `italic_decorator` wraps the original function.
     - `bold_decorator` wraps the result of `italic_decorator`.

2. __Use Cases__:
   - You might stack multiple decorators for logging, validation, access control, or formatting.

---

### __Practical Use Cases of Decorators__

1. __Logging__:
   Add logging functionality to a function.

   ```python
   def log_decorator(func):
       def wrapper(*args, **kwargs):
           print(f"Calling function: {func.__name__}")
           return func(*args, **kwargs)
       return wrapper
   ```

2. __Access Control__:
   Restrict access to specific users or roles.

   ```python
   def admin_only(func):
       def wrapper(user):
           if user != "admin":
               print("Access Denied!")
           else:
               func(user)
       return wrapper

   @admin_only
   def view_admin_dashboard(user):
       print("Welcome to the admin dashboard!")
   ```

3. __Formatting Output__:
   Format the output of a function for display or use in templates.

---

Decorators are a powerful and flexible way to add functionality to your code in a clean and reusable manner. Multiple decorators help in stacking behaviors efficiently.

```py
def love(fun):
  def inner():
    return fun.__name__
  return inner
@love
def fun_test():
  print("testing")

print(fun_test())  
```

```py
def dob(fun):
  def inner(n):
    return fun(n**2)
  return inner

def calc(num):
  print(num)

@dob
def cal(num):
  print(num)

calc(11)
cal(11)
```

Q9. What is list comprehension? write some sample code? what is use of it?

### __What is List Comprehension in Python?__

List comprehension is a concise and elegant way to create lists in Python. It uses a single line of code to generate a new list by applying an expression to each item in an existing iterable.

---

### __Syntax of List Comprehension__

```python
[expression for item in iterable if condition]
```

1. __Expression__: An operation or transformation applied to each item in the iterable.
2. __Item__: The variable that takes the value of each element from the iterable.
3. __Iterable__: The data source (e.g., list, range, string, etc.).
4. __Condition (optional)__: A filtering condition that determines whether an item should be included.

---

### __Uses of List Comprehension__

1. __Simplifies Code__: Reduces multiple lines of code into one concise statement.
2. __Readable__: Improves code readability for simple list transformations.
3. __Efficient__: Faster than traditional `for` loops for small to medium-sized datasets.

---

### __Examples of List Comprehension__

#### __1. Basic List Creation__

```python
# Create a list of squares
squares = [x**2 for x in range(5)]
print(squares)  # Output: [0, 1, 4, 9, 16]
```

#### __2. With Filtering (Condition)__

```python
# Create a list of even numbers
evens = [x for x in range(10) if x % 2 == 0]
print(evens)  # Output: [0, 2, 4, 6, 8]
```

#### __3. Nested Loops__

```python
# Create a list of coordinate pairs
coordinates = [(x, y) for x in range(3) for y in range(2)]
print(coordinates)  # Output: [(0, 0), (0, 1), (1, 0), (1, 1), (2, 0), (2, 1)]
```

#### __4. Applying a Function__

```python
# Convert all strings in a list to uppercase
words = ["hello", "world", "python"]
uppercase_words = [word.upper() for word in words]
print(uppercase_words)  # Output: ['HELLO', 'WORLD', 'PYTHON']
```

#### __5. Conditional Transformation__

```python
# Replace negative numbers with 0
nums = [-1, 2, -3, 4]
non_negative = [x if x >= 0 else 0 for x in nums]
print(non_negative)  # Output: [0, 2, 0, 4]
```

#### __6. Flattening a Nested List__

```python
# Flatten a 2D list
matrix = [[1, 2], [3, 4], [5, 6]]
flattened = [num for row in matrix for num in row]
print(flattened)  # Output: [1, 2, 3, 4, 5, 6]
```

---

### __Advantages of List Comprehension__

- Concise and expressive.
- Avoids the need for explicit loops.
- Easy to read and understand for simple operations.

---

### __When to Avoid List Comprehension__

- When the logic is complex and includes multiple conditions or operations, traditional loops may be more readable.
- For very large datasets, using list comprehension may lead to high memory usage as it creates the entire list in memory.

---

### __Summary__

List comprehension is a powerful and elegant way to generate and manipulate lists in Python. It is particularly useful for creating new lists based on existing iterables in a concise and efficient manner.

#### Q. Write a program to display unique vowels present in the given word?

```py
vowels = ['a', 'e', 'i', 'o', 'u']
word = input("Enter the word to search for vowels: ")

# Using list comprehension to find unique vowels in the word
found = [letter for letter in vowels if letter in word]

print(found)
print(f"The number of different vowels present in '{word}' is {len(found)}")

```

Q10. Write code of fibonacci series?

```py
def fib():
  a,b = 0,1
  while True:
    yield a
    a,b = b,a+b
data = fib()
for _ in range(11):
  print(next(data))
```

```py
# Fibonacci series using generator
def fibonacci_generator(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

# Input: Number of terms
num_terms = int(input("Enter the number of terms: "))
print(f"Fibonacci series: {list(fibonacci_generator(num_terms))}")

```

Q11. What is dictionary? is this accept duplicate or not?
Q20. program to reverse dictionary key to value and value to key
Here’s a Python program to reverse the keys and values of a dictionary:

### __Program__

```python
# Original dictionary
original_dict = {
    "name": "Ashish",
    "age": 25,
    "course": "Python"
}

# Reversing the dictionary
reversed_dict = {value: key for key, value in original_dict.items()}

# Output the result
print("Original Dictionary:", original_dict)
print("Reversed Dictionary:", reversed_dict)
```

---

### __Output__

```
Original Dictionary: {'name': 'Ashish', 'age': 25, 'course': 'Python'}
Reversed Dictionary: {'Ashish': 'name', 25: 'age', 'Python': 'course'}
```

---

### __Explanation__

1. __`original_dict.items()`__: Provides an iterable of key-value pairs from the original dictionary.
2. __Dictionary Comprehension__: Swaps the keys and values by creating a new dictionary where:
   - `key` becomes `value`
   - `value` becomes `key`

---

### __Considerations__

- __Duplicate Values in the Original Dictionary__: If there are duplicate values in the original dictionary, the reversed dictionary will only keep one of the original keys (the last one processed). For example:

  ```python
  original_dict = {"a": 1, "b": 2, "c": 1}
  reversed_dict = {value: key for key, value in original_dict.items()}
  print(reversed_dict)  # Output: {1: 'c', 2: 'b'}
  ```

  The key `'a'` is overwritten by `'c'` for the value `1`.

- __Immutable Values__: Only hashable and immutable values in the original dictionary can be used as keys in the reversed dictionary. If a value is mutable (like a list), it will raise a `TypeError`.
Q21. what lambda function with example

### __What is a Lambda Function in Python?__

A __lambda function__ in Python is a small, anonymous function defined using the `lambda` keyword. It can have any number of input arguments but only one expression. The result of the expression is automatically returned.

---

### __Syntax__

```python
lambda arguments: expression
```

- __`arguments`__: Input parameters, like a regular function.
- __`expression`__: The computation or operation to perform and return.

---

### __Key Characteristics__

1. Anonymous: Lambda functions don't have a name (unlike normal functions defined using `def`).
2. Single Expression: They consist of only one expression, and the result is implicitly returned.
3. Typically used for short, simple operations.

---

### __Examples__

#### __1. Simple Lambda Function__

```python
# Lambda function to add two numbers
add = lambda x, y: x + y
print(add(5, 3))  # Output: 8
```

---

#### __2. Lambda Function Inside Another Function__

```python
# Function using a lambda to square a number
def square(n):
    return (lambda x: x ** 2)(n)

print(square(4))  # Output: 16
```

---

#### __3. Using Lambda with `map()`__

```python
# Doubling all numbers in a list
nums = [1, 2, 3, 4, 5]
doubled = list(map(lambda x: x * 2, nums))
print(doubled)  # Output: [2, 4, 6, 8, 10]
```

---

#### __4. Using Lambda with `filter()`__

```python
# Filtering even numbers from a list
nums = [1, 2, 3, 4, 5]
even_nums = list(filter(lambda x: x % 2 == 0, nums))
print(even_nums)  # Output: [2, 4]
```

---

#### __5. Using Lambda with `sorted()`__

```python
# Sorting a list of tuples by the second element
data = [(1, 'b'), (2, 'a'), (3, 'c')]
sorted_data = sorted(data, key=lambda x: x[1])
print(sorted_data)  # Output: [(2, 'a'), (1, 'b'), (3, 'c')]
```

---

### __When to Use Lambda Functions__

1. For small, quick operations.
2. As an argument to functions like `map()`, `filter()`, and `sorted()`.
3. When defining functions inline without needing a formal function name.

---

### __Limitations of Lambda Functions__

1. __Single Expression__: Lambdas are limited to one expression, so they're not suitable for complex logic.
2. __No Name__: Debugging and reusability can be harder because they're anonymous.
3. __No Statements__: Cannot contain statements like `if`, `for`, or `print` (only expressions).

---

### __Comparison with Regular Function__

```python
# Regular function
def add(x, y):
    return x + y

# Equivalent lambda function
add_lambda = lambda x, y: x + y
```

Both can be used interchangeably, but lambda is concise and often used for inline or short-lived operations.

### __`map()`, `filter()`, and `sorted()` in Python__

These are built-in Python functions commonly used for applying operations to collections like lists, tuples, or sets. They allow for efficient, functional-style operations.

---

### __1. `map()`__

The `map()` function applies a given function to each item in an iterable and returns a new iterable (a `map` object).

#### __Syntax__

```python
map(function, iterable)
```

- __`function`__: A function to apply to each element of the iterable.
- __`iterable`__: The collection (like a list, tuple) whose items the function will process.

#### __Example__

```python
# Doubling each number in a list
nums = [1, 2, 3, 4]
doubled = list(map(lambda x: x * 2, nums))
print(doubled)  # Output: [2, 4, 6, 8]
```

#### __Use Cases__

- Transforming data in a collection.
- Applying mathematical or custom operations on each element.

---

### __2. `filter()`__

The `filter()` function filters elements from an iterable based on a condition defined by a function. It returns a new iterable (a `filter` object) containing elements where the function evaluates to `True`.

#### __Syntax__

```python
filter(function, iterable)
```

- __`function`__: A function that returns `True` or `False` for each element.
- __`iterable`__: The collection to filter.

#### __Example__

```python
# Filtering even numbers from a list
nums = [1, 2, 3, 4, 5, 6]
evens = list(filter(lambda x: x % 2 == 0, nums))
print(evens)  # Output: [2, 4, 6]
```

#### __Use Cases__

- Extracting elements that meet a specific condition.
- Filtering data like even numbers, strings that match a pattern, etc.

---

### __3. `sorted()`__

The `sorted()` function sorts the elements of an iterable and returns a new sorted list.

#### __Syntax__

```python
sorted(iterable, key=None, reverse=False)
```

- __`iterable`__: The collection to be sorted.
- __`key`__ *(optional)*: A function defining the sorting logic (e.g., based on length or specific property).
- __`reverse`__ *(optional)*: If `True`, sorts in descending order; otherwise, ascending (default).

#### __Example__

```python
# Sorting numbers in ascending and descending order
nums = [5, 2, 9, 1, 3]
print(sorted(nums))               # Output: [1, 2, 3, 5, 9]
print(sorted(nums, reverse=True)) # Output: [9, 5, 3, 2, 1]

# Sorting strings by length
words = ["apple", "banana", "kiwi"]
sorted_by_length = sorted(words, key=len)
print(sorted_by_length)  # Output: ['kiwi', 'apple', 'banana']
```

#### __Use Cases__

- Sorting data numerically, alphabetically, or based on custom criteria.
- Rearranging complex data like dictionaries, tuples, or custom objects.

---

### __Summary of Differences__

| __Function__ | __Purpose__                                        | __Returns__       | __Use Case__                                |
|--------------|----------------------------------------------------|-------------------|---------------------------------------------|
| `map()`      | Applies a function to every element of an iterable | A `map` object    | Transform all elements of a collection      |
| `filter()`   | Filters elements based on a condition              | A `filter` object | Extract specific elements from a collection |
| `sorted()`   | Sorts elements based on criteria                   | A list            | Arrange elements in a specific order        |

These functions are integral for efficient data processing and align well with functional programming styles in Python.
Q22. Can you convert List to Dict object. (Scenario)
> Yes, you can convert a list to a dictionary in Python. However, how you do this depends on the structure of the list and the desired format of the dictionary. Here are a few common scenarios:

---

### __1. Convert a List of Tuples to a Dictionary__

If the list contains tuples where the first element is the key and the second is the value, you can use the `dict()` constructor.

```python
# List of tuples
list_of_tuples = [("a", 1), ("b", 2), ("c", 3)]

# Convert to dictionary
dict_obj = dict(list_of_tuples)
print(dict_obj)
```

__Output:__

```
{'a': 1, 'b': 2, 'c': 3}
```

---

### __2. Convert Two Lists (Keys and Values) into a Dictionary__

If you have two lists — one for keys and one for values — you can use the `zip()` function.

```python
# Lists of keys and values
keys = ["name", "age", "city"]
values = ["Alice", 25, "New York"]

# Convert to dictionary
dict_obj = dict(zip(keys, values))
print(dict_obj)
```

__Output:__

```
{'name': 'Alice', 'age': 25, 'city': 'New York'}
```

---

### __3. Convert a List of Elements into a Dictionary with Indices as Keys__

If you want to use the indices of the list elements as dictionary keys, you can use `enumerate()`.

```python
# List of values
values = ["Apple", "Banana", "Cherry"]

# Convert to dictionary
dict_obj = {index: value for index, value in enumerate(values)}
print(dict_obj)
```

__Output:__

```
{0: 'Apple', 1: 'Banana', 2: 'Cherry'}
```

---

### __4. Convert a Flat List into a Dictionary__

If the list alternates between keys and values, you can use slicing or the `zip()` function.

```python
# Flat list with alternating keys and values
flat_list = ["name", "Alice", "age", 25, "city", "New York"]

# Convert to dictionary
dict_obj = dict(zip(flat_list[0::2], flat_list[1::2]))
print(dict_obj)
```

__Output:__

```
{'name': 'Alice', 'age': 25, 'city': 'New York'}
```

---

## What are Python metaclasses, and how do they work?

The metaclasses in Python help in controlling the creation of classes. There is a built-in type metaclass in Python; custom metaclasses in Python can be defined using the inject methods or by enforcing the coding standards. Metaclasses are very helpful when multiple classes need to follow a particular set of rules. They make it easy for developers to enforce these rules and are mainly used in Python frameworks and library designs.

## What are constructors?

## 79. What is a class and an object in Python?

## 77. What is dictionary comprehension?

Dictionary comprehension in Python is a quick and clear way to create a dictionary using existing data like a list, tuple, or range. It works just like list comprehension but builds a dictionary instead of a list.

Key Features:

Builds a dictionary using a single-line expression.
Allows adding conditions or modifying values and keys.
Makes the code shorter, cleaner, and easier to read
Example:

```py
# Create a dictionary of squares for even numbers from 0 to 4
dict_comprehension = {i: i**2 for i in range(5) if i % 2 == 0}

print(dict_comprehension)

```

## How can the ternary operators be used in Python?

The ternary operator is the operator used to show the conditional statements in Python. This consists of the boolean true or false values, along with a statement that has to be checked.

Syntax:

[on_true] if [condition] else [on_false]<br>
x, y = 10, 20<br>
count = x if x < y else y<br>
print(count)
Explanation: The above expression is evaluated as if x<y else y, in this case, if x<y is true, then the value is returned as count=x, and if it is incorrect, then count=y will be stored into the result.

## Explain the use of the ‘with’ statement and its syntax

The ‘with’ statement in Python is used for managing resources efficiently and helps in file handling operations. It helps in simplifying the code by automatically opening and closing the files, even if there is an error during the execution. For opening a file with open(“filename”, “mode”) as file: is used, and the file is automatically closed.   With statements is a better approach than manually opening and closing a file using open() and close(). It also helps in preventing memory leakage and file access errors, which makes it the best choice for file handling operations.   Here is the syntax:

with open("filename", "mode") as file_var:

## What are the different types of inheritance in Python?

Inheritance is a major pillar in the OOPs concept. There are five types of inheritance available in Python. All of them are listed below:

Single Inheritance: A Situation where a class inherits properties from one superclass.
Multiple Inheritance: A Situation where a class inherits properties from multiple superclasses
Multilevel Inheritance: This is a scenario where a class inherits properties from a superclass, which itself inherits from another superclass. It forms a chain of inheritance across multiple levels
Hierarchical Inheritance: A Situation where multiple classes are inheriting properties from a single superclass
Hybrid Inheritance: A Situation where different types of inheritance are used.

## What is the use of slots in Python classes?

The __slots__ in a Python class help in limiting the attributes of an object. This prevents Python from creating a separate __dict__ for each instance, which helps in making the classes memory efficient and faster. This is very helpful when dealing with multiple objects. But __slot__ cannot be used to add new attributes to the instances, which reduces the flexibility. It is mainly used to improve the performance and make the class’s memory efficient.

### __5. Custom Conversion Logic__

If the list has a custom structure, you can use a loop or a dictionary comprehension to process it.

```python
# List of items
list_items = ["name", "Alice", "age", 25, "city", "New York"]

# Convert to dictionary (even indices are keys, odd indices are values)
dict_obj = {list_items[i]: list_items[i + 1] for i in range(0, len(list_items), 2)}
print(dict_obj)
```

__Output:__

```
{'name': 'Alice', 'age': 25, 'city': 'New York'}
```

---

### __General Notes__

1. __Duplicate Keys__: If the list contains duplicate keys (e.g., in case of a list of tuples), only the last key-value pair is retained in the dictionary.
2. __Invalid Data Structure__: If the list structure doesn't match the intended dictionary format (e.g., an odd number of elements in the flat list), you’ll need to handle such cases with error-checking or default values.
Q23. Diff between extend & append in list

### __Difference Between `extend()` and `append()` in Python Lists__

Both `extend()` and `append()` are methods used to add elements to a list in Python, but they behave differently.

---

### __1. `append()`__

- __Purpose__: Adds a single element to the end of the list.
- __Behavior__: Treats the argument as a single item, even if it is iterable (like a list or tuple).
- __Returns__: Does not return a new list; modifies the list in place.
  
#### __Example:__

```python
# Original list
my_list = [1, 2, 3]

# Append an element
my_list.append(4)
print(my_list)  # Output: [1, 2, 3, 4]

# Append a list as a single element
my_list.append([5, 6])
print(my_list)  # Output: [1, 2, 3, 4, [5, 6]]
```

---

### __2. `extend()`__

- __Purpose__: Extends the list by appending each element from the iterable (like another list or tuple) to the list.
- __Behavior__: Breaks the iterable into individual elements and adds them to the list.
- __Returns__: Does not return a new list; modifies the list in place.

#### __Example:__

```python
# Original list
my_list = [1, 2, 3]

# Extend the list with another list
my_list.extend([4, 5])
print(my_list)  # Output: [1, 2, 3, 4, 5]

# Extend the list with a tuple
my_list.extend((6, 7))
print(my_list)  # Output: [1, 2, 3, 4, 5, 6, 7]
```

---

### __Key Differences__

| __Feature__       | __`append()`__                      | __`extend()`__                          |
|--------------------|-------------------------------------|-----------------------------------------|
| __Argument__       | Takes a single element (any type). | Takes an iterable (e.g., list, tuple).  |
| __Behavior__       | Adds the entire element as-is.     | Adds each element of the iterable.      |
| __Effect__         | Increases the list length by 1.    | Increases the list length by the size of the iterable. |
| __Result__         | Adds nested lists or iterables.    | Flattens the iterable into the list.    |

---

### __Example Comparison__

```python
# Using append()
list1 = [1, 2, 3]
list1.append([4, 5])
print(list1)  # Output: [1, 2, 3, [4, 5]]

# Using extend()
list2 = [1, 2, 3]
list2.extend([4, 5])
print(list2)  # Output: [1, 2, 3, 4, 5]
```

---

### __When to Use?__

- Use __`append()`__ when you want to add a single element or when adding an entire object (like a list) as a single item.
- Use __`extend()`__ when you want to add multiple elements from an iterable to the list individually.

These methods make list manipulations more versatile and efficient depending on the task.
Q13. What are the main principles of oops?
Q14. Explain type of inheritance
Q15. What is aws lambda function
Q16. Explain your project briefly
Q17. regular expression for email validation

### __Regular Expression for Email Validation__

A regular expression (regex) can be used to validate email addresses by ensuring they conform to a specific pattern. Here's an example of a commonly used regex for email validation:

```python
import re

# Define a regex pattern for email validation
email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

# Sample email validation function
def validate_email(email):
    if re.match(email_regex, email):
        return True
    return False

# Test the function
print(validate_email("example@test.com"))  # Output: True
print(validate_email("invalid-email"))     # Output: False
```

---

### __Explanation of the Regex Pattern__

```regex
^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$
```

| __Component__          | __Meaning__                                                                 |
|-------------------------|-----------------------------------------------------------------------------|
| `^`                    | Start of the string.                                                       |
| `[a-zA-Z0-9._%+-]+`     | Matches the local part of the email (before the `@`). Can contain letters, digits, dots (`.`), underscores (`_`), percent signs (`%`), plus (`+`), and hyphens (`-`). |
| `@`                    | Matches the `@` symbol separating the local part and the domain.            |
| `[a-zA-Z0-9.-]+`        | Matches the domain name (e.g., `gmail`, `yahoo`). Can contain letters, digits, dots (`.`), and hyphens (`-`). |
| `\.`                   | Matches the dot (`.`) separating the domain and top-level domain (TLD).     |
| `[a-zA-Z]{2,}`          | Matches the top-level domain (TLD) with at least 2 characters (e.g., `com`, `org`). |
| `$`                    | End of the string.                                                         |

---

### __Examples of Valid and Invalid Emails__

#### __Valid Emails__

1. `example@test.com`
2. `user.name+tag+sorting@example.com`
3. `x@example.org`
4. `email@subdomain.example.com`

#### __Invalid Emails__

1. `plainaddress` (No `@` symbol)
2. `@missingusername.com` (No local part)
3. `username@.com` (Domain is missing)
4. `username@domain` (No TLD)

---

### __Important Notes__

- This regex is a basic implementation and covers most use cases.
- Some valid emails might not match this regex (e.g., unusual but technically valid domain names).
- For stricter validation or internationalized email addresses, consider libraries like __`email-validator`__:

  ```bash
  pip install email-validator
  ```

  ```python
  from email_validator import validate_email, EmailNotValidError

  try:
      valid = validate_email("example@test.com")
      print("Valid Email:", valid.email)
  except EmailNotValidError as e:
      print("Invalid Email:", str(e))
  ```

## How to define private and public variables

- Public variables: Accessible everywhere; no underscore.
- Protected variables: Should be used only in class and subclasses; single underscore _.
- Private variables: Accessible only inside the class; double underscore __. Python uses name mangling to prevent external access.

1. Public Variables

Definition:
Accessible from anywhere – inside the class, in subclasses, and outside the class.

How to define:
Simply define a variable without any underscores.

```py
class Employee:
    def __init__(self, name):
        self.name = name  # Public variable

emp = Employee("Ashish")
print(emp.name)  # Accessible outside the class → Ashish
```

2. Protected Variables

Definition:
Intended to be accessible only within the class and its subclasses.

Not strictly enforced in Python, it’s just a convention.

How to define:
Prefix the variable name with a single underscore _

```py
class Employee:
    def __init__(self, name, salary):
        self._salary = salary  # Protected variable

class Manager(Employee):
    def show_salary(self):
        print(self._salary)  # Accessible in subclass

emp = Employee("Ashish", 50000)
print(emp._salary)  # Technically accessible, but discouraged
```

3. Private Variables

Definition:
Variables that are accessible only within the class.
Python mangles the name to prevent accidental access from outside.

How to define:
Prefix the variable name with double underscore __.

```py
class Employee:
    def __init__(self, name, salary):
        self.__salary = salary  # Private variable

    def show_salary(self):
        print(self.__salary)

emp = Employee("Ashish", 50000)
emp.show_salary()  # 50000
print(emp.__salary)  # Error → AttributeError
```

## magic methods

magic methods in Python (also called dunder methods).
Magic methods are special methods in Python with double underscores (__method__).

They define the behavior of Python objects for built-in operations.

Python automatically calls them in response to operators or built-in functions.

| Magic Method  | Purpose / Example                               |
| ------------- | ----------------------------------------------- |
| `__init__`    | Constructor; called when creating an object     |
| `__str__`     | Defines string representation (used by `print`) |
| `__repr__`    | Developer-friendly string representation        |
| `__len__`     | Called by `len()`                               |
| `__add__`     | Defines behavior for `+` operator               |
| `__sub__`     | Defines behavior for `-` operator               |
| `__getitem__` | Access elements using indexing (`obj[key]`)     |
| `__setitem__` | Set element via indexing (`obj[key] = value`)   |
| `__iter__`    | Makes object iterable                           |
| `__next__`    | Returns next item for iterator                  |
| `__call__`    | Makes object callable like a function           |

```py
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def __str__(self):
        return f"{self.name} earns {self.salary}"

    def __add__(self, other):
        return self.salary + other.salary

emp1 = Employee("Ashish", 50000)
emp2 = Employee("Bindra", 60000)

print(emp1)          # Calls __str__: Ashish earns 50000
print(emp1 + emp2)   # Calls __add__: 110000
```

## iterables and iterators in Python

Definition: An iterable is any Python object that can return an iterator.

Examples: list, tuple, dict, set, str, etc.

Key point: You can loop over it using a for loop.
How to check if an object is iterable:

```py
from collections.abc import Iterable

print(isinstance([1, 2, 3], Iterable))  # True
print(isinstance(123, Iterable))        # False
```

2. Iterator

Definition: An iterator is an object that produces items one at a time from an iterable.

It implements two methods:

__iter__() → returns the iterator object itself

__next__() → returns the next value, raises StopIteration when exhausted
How to get an iterator from an iterable:

```py
my_list = [1, 2, 3]
it = iter(my_list)  # Get iterator

print(next(it))  # 1
print(next(it))  # 2
print(next(it))  # 3
# print(next(it))  # Raises StopIteration
```

3. Key Differences
| Feature    | Iterable               | Iterator                                          |
| ---------- | ---------------------- | ------------------------------------------------- |
| Definition | Can return an iterator | Produces items one by one                         |
| Methods    | `__iter__()`           | `__iter__()` and `__next__()`                     |
| Looping    | Can use `for` loop     | Can use `for` loop but is consumed after one pass |
| Example    | list, tuple, str, set  | `iter(list)`, generator objects                   |

4. Generators

Generators are special iterators created using:

yield keyword in functions

Generator expressions (x*x for x in range(5))

They are lazy, meaning they generate values on demand.

```py
def my_gen():
    for i in range(3):
        yield i

g = my_gen()
print(next(g))  # 0
print(next(g))  # 1
```

5. Interview-Friendly Answer

Iterable: Any object you can loop over (for), like lists, tuples, sets, strings.

Iterator: An object that produces items from an iterable one by one using __next__().

Key idea: You can convert an iterable to an iterator using iter(). Iterators are consumed once, while iterables can produce multiple iterators.

## 1. What is Caching in Python?

Python caching is a technique to store frequently used results in memory to avoid repeated computation and improve performance. Common approaches include functools.lru_cache for function results, manual caching with dictionaries, and caching frameworks in web apps like Django or Flask.”
Definition: Caching is the process of storing frequently used data in memory to avoid recomputation.

Helps improve performance for expensive operations like function calls, database queries, or API calls.

2. Common Python Caching Techniques
a) Using functools.lru_cache
lru_cache stands for Least Recently Used cache.

It stores results of a function call in memory and returns cached results if the same arguments are passed again.

```py
from functools import lru_cache

@lru_cache(maxsize=5)
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(10))
```

The function caches the last 5 calls.

Performance boost for recursive functions like Fibonacci.

b) Using a Dictionary

Simple manual caching using a dictionary.

```py
cache = {}

def square(n):
    if n in cache:
        return cache[n]
    result = n * n
    cache[n] = result
    return result

print(square(4))  # Computes and stores
print(square(4))  # Returns from cache
```

c) Caching in Web Frameworks

Django cache framework:

Stores database query results, templates, or API responses.

Backends: Memory, Redis, Memcached, file-based, database.

```py
from django.core.cache import cache

cache.set('my_key', 'my_value', timeout=60)  # 60 seconds
value = cache.get('my_key')
```

3. Why Use Caching

Faster performance by avoiding repeated computations.

Reduces load on databases and external APIs.

Improves user experience in web applications.

1. What is Reference Counter?
1. What is a .pyc file?
.pyc stands for Python Compiled file.

It is a bytecode-compiled version of a Python .py source file.

Python compiles .py files to bytecode before execution and stores it as .pyc for faster subsequent runs

## python chache

Q24. Define a class. SDLC models
Q25. Asked to describe iterators in Python, and implement it
Q26. Asked about generators? Asked how I implemented Python in my project
Q27. datatypes in python
Q28. SLice , list , dict , django, CROSS, API
Q29. Midlewares, session,cookies,APIs,oops
Q30. Reverse character string in python
Q32. map

## 671

Iteration is a general term for taking each item of something, one after another. Any time you use a loop, explicit or implicit, to go over a group of items, that is iteration.

In Python, iterable and iterator have specific meanings.

An iterable is an object that has an __iter__ method which returns an iterator, or which defines a __getitem__ method that can take sequential indexes starting from zero (and raises an IndexError when the indexes are no longer valid). So an iterable is an object that you can get an iterator from.

An iterator is an object with a next (Python 2) or __next__ (Python 3) method.

Whenever you use a for loop, or map, or a list comprehension, etc. in Python, the next method is called automatically to get each item from the iterator, thus going through the process of iteration.

An iterable is an object from which an iterator can be obtained, such as a list or string, while an iterator is an object that produces the next value in a sequence and maintains its state through an internal counter, obtained by calling the iter() function on an iterable. Key differences include: iterables provide the data, iterators control the traversal one item at a time; iterators are always iterable, but the reverse is not true; and iterables implement the __iter__() method, while iterators implement both __iter__() and __next__().  
Iterable
Definition: An object that can return an iterator.
Purpose: To allow iteration over its elements.
Implementation: Often includes a __iter__() method that returns an iterator, or a __getitem__() method that can be accessed with sequential indexes.
Examples: Lists, strings, dictionaries, and ranges are common iterables.
Usage: A for loop automatically calls iter() on the iterable, obtaining an iterator to go through the elements.
Iterator
Definition: An object that represents a stream of data and iterates over a collection of elements one by one.
Purpose: To control the iteration process by keeping track of the internal state.
Implementation: Implements both the __iter__() method (which returns itself) and the __next__() method.
Usage: The __next__() method retrieves the next item from the iterable. When there are no more items, it raises a StopIteration exception, which terminates the for loop.
Key Relationship
Every iterator is also an iterable.
Not every iterable is an iterator. A list is iterable, but it is not an iterator because it doesn't have the __next__() method and doesn't keep an internal state for traversal.

### __`map()`, `filter()`, and `sorted()` in Python__

These are built-in Python functions commonly used for applying operations to collections like lists, tuples, or sets. They allow for efficient, functional-style operations.

---

### __1. `map()`__

The `map()` function applies a given function to each item in an iterable and returns a new iterable (a `map` object).

#### __Syntax__

```python
map(function, iterable)
```

- __`function`__: A function to apply to each element of the iterable.
- __`iterable`__: The collection (like a list, tuple) whose items the function will process.

#### __Example__

```python
# Doubling each number in a list
nums = [1, 2, 3, 4]
doubled = list(map(lambda x: x * 2, nums))
print(doubled)  # Output: [2, 4, 6, 8]
```

#### __Use Cases__

- Transforming data in a collection.
- Applying mathematical or custom operations on each element.

---

### __2. `filter()`__

The `filter()` function filters elements from an iterable based on a condition defined by a function. It returns a new iterable (a `filter` object) containing elements where the function evaluates to `True`.

#### __Syntax__

```python
filter(function, iterable)
```

- __`function`__: A function that returns `True` or `False` for each element.
- __`iterable`__: The collection to filter.

#### __Example__

```python
# Filtering even numbers from a list
nums = [1, 2, 3, 4, 5, 6]
evens = list(filter(lambda x: x % 2 == 0, nums))
print(evens)  # Output: [2, 4, 6]
```

#### __Use Cases__

- Extracting elements that meet a specific condition.
- Filtering data like even numbers, strings that match a pattern, etc.

---

### __3. `sorted()`__

The `sorted()` function sorts the elements of an iterable and returns a new sorted list.

#### __Syntax__

```python
sorted(iterable, key=None, reverse=False)
```

- __`iterable`__: The collection to be sorted.
- __`key`__ *(optional)*: A function defining the sorting logic (e.g., based on length or specific property).
- __`reverse`__ *(optional)*: If `True`, sorts in descending order; otherwise, ascending (default).

#### __Example__

```python
# Sorting numbers in ascending and descending order
nums = [5, 2, 9, 1, 3]
print(sorted(nums))               # Output: [1, 2, 3, 5, 9]
print(sorted(nums, reverse=True)) # Output: [9, 5, 3, 2, 1]

# Sorting strings by length
words = ["apple", "banana", "kiwi"]
sorted_by_length = sorted(words, key=len)
print(sorted_by_length)  # Output: ['kiwi', 'apple', 'banana']
```

- Sorting data numerically, alphabetically, or based on custom criteria.
- Rearranging complex data like dictionaries, tuples, or custom objects.

---

| __Function__ | __Purpose__                                        | __Returns__       | __Use Case__                                |
|--------------|----------------------------------------------------|-------------------|---------------------------------------------|
| `map()`      | Applies a function to every element of an iterable | A `map` object    | Transform all elements of a collection      |
| `filter()`   | Filters elements based on a condition              | A `filter` object | Extract specific elements from a collection |
| `sorted()`   | Sorts elements based on criteria                   | A list            | Arrange elements in a specific order        |

These functions are integral for efficient data processing and align well with functional programming styles in Python.x  
Q33. filter
Q34. tertools (Advanced Iterators)

### __`itertools` (Advanced Iterators) in Python__

The __`itertools`__ module in Python provides a set of fast, memory-efficient tools for working with iterators. These tools allow you to create complex iterators for handling combinatorics, permutations, combinations, and more. It's part of Python's standard library.

---

### __Key Features__

1. Efficient iteration over large data sets without loading everything into memory.
2. Provides advanced functions for:
   - Infinite iterators
   - Iterators for combinations and permutations
   - Utility functions for iterator manipulation

---

### __Categories of Functions__

#### __1. Infinite Iterators__

These iterators produce values indefinitely and are useful for repetitive tasks.

- __`itertools.count(start=0, step=1)`__: Generates an infinite sequence starting at `start` and incremented by `step`.

  ```python
  from itertools import count
  for num in count(5, 2):  # Starts at 5, increments by 2
      if num > 15:
          break
      print(num)  # Output: 5, 7, 9, 11, 13, 15
  ```

- __`itertools.cycle(iterable)`__: Cycles through an iterable indefinitely.

  ```python
  from itertools import cycle
  counter = 0
  for item in cycle(['A', 'B', 'C']):
      if counter > 5:
          break
      print(item)  # Output: A, B, C, A, B, C
      counter += 1
  ```

- __`itertools.repeat(object, times=None)`__: Repeats an object a fixed number of times (or indefinitely if `times` is not specified).

  ```python
  from itertools import repeat
  for item in repeat("Hello", 3):
      print(item)  # Output: Hello, Hello, Hello
  ```

---

#### __2. Combinatoric Iterators__

Generate permutations, combinations, or Cartesian products.

- __`itertools.permutations(iterable, r=None)`__: Generates all possible permutations of `r` elements from the iterable.

  ```python
  from itertools import permutations
  for perm in permutations([1, 2, 3], 2):
      print(perm)  # Output: (1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)
  ```

- __`itertools.combinations(iterable, r)`__: Generates all possible combinations of `r` elements from the iterable.

  ```python
  from itertools import combinations
  for comb in combinations([1, 2, 3], 2):
      print(comb)  # Output: (1, 2), (1, 3), (2, 3)
  ```

- __`itertools.product(*iterables, repeat=1)`__: Generates the Cartesian product of input iterables.

  ```python
  from itertools import product
  for prod in product([1, 2], ['A', 'B']):
      print(prod)  # Output: (1, 'A'), (1, 'B'), (2, 'A'), (2, 'B')
  ```

---

#### __3. Utility Iterators__

Helpers for combining, grouping, or slicing iterators.

- __`itertools.chain(*iterables)`__: Combines multiple iterables into a single iterator.

  ```python
  from itertools import chain
  for item in chain([1, 2], ['A', 'B']):
      print(item)  # Output: 1, 2, A, B
  ```

- __`itertools.islice(iterable, start, stop, step)`__: Slices an iterable.

  ```python
  from itertools import islice
  for item in islice(range(10), 2, 8, 2):
      print(item)  # Output: 2, 4, 6
  ```

- __`itertools.groupby(iterable, key=None)`__: Groups items in an iterable by a key function.

  ```python
  from itertools import groupby
  data = [("cat", 1), ("cat", 2), ("dog", 3), ("dog", 4)]
  for key, group in groupby(data, lambda x: x[0]):
      print(key, list(group))  
      # Output: 
      # cat [('cat', 1), ('cat', 2)]
      # dog [('dog', 3), ('dog', 4)]
  ```

---

### __Advantages__

1. __Memory Efficiency__: Operates lazily, producing values on demand instead of storing them in memory.
2. __Combinatoric Power__: Simplifies tasks like generating permutations, combinations, or Cartesian products.
3. __Enhanced Productivity__: Provides many ready-to-use tools that reduce the need for custom implementations.

---

### __Real-World Example__

__Summing two lists element-wise using `itertools.zip_longest`:__

```python
from itertools import zip_longest

list1 = [1, 2, 3]
list2 = [4, 5]
result = [a + b for a, b in zip_longest(list1, list2, fillvalue=0)]
print(result)  # Output: [5, 7, 3]
```

---

### __Summary__

The `itertools` module is a powerful toolkit for working with iterators. It helps perform complex operations like infinite looping, combinations, or slicing in a memory-efficient way. This makes it especially useful in data processing, mathematical computations, and generating sequences.

## You are given a singly linked list that stores integer values in ascending order. Your task is to determine the time complexity for performing an insertion operation on the numeric value 6 in the given LinkedList

```py
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def insert_sorted(self, value):
        new_node = Node(value)
        # If the list is empty or the value should be inserted at the head
        if not self.head or self.head.data >= value:
            new_node.next = self.head
            self.head = new_node
            return

        # Traverse the list to find the insertion point
        current = self.head
        while current.next and current.next.data < value:
            current = current.next

        # Insert the new node
        new_node.next = current.next
        current.next = new_node

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

# Example usage
linked_list = SinglyLinkedList()
for val in [2, 5, 8, 12]:
    linked_list.insert_sorted(val)

print("Before insertion:")
linked_list.display()

linked_list.insert_sorted(6)

print("After insertion:")
linked_list.display()

```

## What is the difference between is and == operators in Python?

- Feature == Operator is Operator
- Comparison Type Compare the values of the objects Compares the identity (whether the objects are the same in memory)
- What it checks Checks if the two objects are equal Checks if the two objects are the same object in memory
- Use Case Used to compare the values of variables or objects Used to check if two variables refer to the same object in memory

```py
a = [1, 2]
b = [1, 2]

print(a == b)     # True: As both the lists have the same values
print(a is b)      # False: As a and b are different objects in memory


```

71. What are Python closures, and how are they useful?

The closure in Python is created when a function within another function (nested function) captures a variable from the outer function. These captured variables are stored even after the outer function’s execution is finished, which allows the inner functions to use these variables later.   The closure helps in maintaining the state of the program without the need to use global variables and classes. They are very helpful in the decorators, callbacks, and factory functions, where storing and reusing the data is very important.

## What is duck typing in Python?

Duck typing in Python refers to focusing on what the object can do without the need for the type of the object. The term ‘duck’ comes from the saying: “If it looks like a duck and quacks like a duck, it’s probably a duck.” Python follows this by only considering the behaviour and the methods of the object without checking the actual type of the object. For example: When an object is looped over, it is treated as an iterable, even if the object is not in list in Python. This makes Python more flexible and efficient, but the code must be checked properly to avoid runtime errors.

68. How do you handle large files efficiently in Python?
It is better to avoid loading the entire file into memory when working on large files, which may be time-consuming. Instead, loops can be used for better file handling, which reads the file line by line using the for line in file, which uses very little memory, and is efficient for text files. When working with binary files like PDF, images mmap module can be used, which helps in accessing the file content directly from the disk. Also, the chunk-based reading and the file buffering can be used for better file handling.

## What is monkey patching in Python?

Monkey patching in Python helps in changing or adding code to the program that is already running. The method in a class or a module can be replaced or updated easily without the need to change the source code. This is mainly used for testing and fixing small issues in the libraries. Monkey patching should be used carefully when dealing with large projects, as the changes can be harder to trace and debug.

66. How does Python handle type hinting?
Type handling is very useful in Python, which helps in adding additional information to the functions and variables, and specifying the kind of data expected. It does not affect the execution of the Python code, but helps others to understand the functions or the variables. It also allows tools like linkers and IDEs that help in catching errors in the code, and improve the process of debugging. Static type checkers like ‘mypy’ are used in large projects, which helps in improving the readability of the code and reducing errors. The type hints follow the Python PEP 484 format.

## 🧵 MRO (Method Resolution Order) in OOP / Python

## What is the GIL (Global Interpreter Lock) in Python?

The Global Interpreter Lock (GIL) is a mechanism in the standard Interpreter of Python that allows only one thread to execute a bytecode at a time. This helps in making the process of memory management simpler by preventing the race conditions, and also helps in proper multithreading, for the tasks that are bound to the CPU.   GIL is also very helpful for the IO-bound tasks like reading files or making network requests, where the threads are used, as the GIL is reassessed during the waiting. GIL is one of the main reasons for Python being among the best choices for CPU-bound multithreaded operations.

64. Why isn’t all memory deallocated when Python exits?
In Python, some objects that are referred to the other objects in a cyclic manner or are linked to global variables may not get deleted automatically when the program ends. Some portions of memory remain out of reach since they were reserved by the C library. The cleaning process of Python automatically attempts to release all the objects before program termination.

63. How do you securely store API keys and secrets in a Python application?
Storing API keys and secrets securely in a Python is really important if you want to protect sensitive information and prevent hackers from getting access. Below are the best steps to follow for securely handling secrets:

1. Use Environment Variables

Rather than directly embedding secrets in your Python files, save them as environment variables and then retrieve them with the os module.

import os

api_key = os.getenv("API_KEY")
How to set environment variables:

On Linux/macOS:

export API_KEY='your_api_key_here'
On Windows:

set API_KEY=your_api_key_here
2. Use a .env File with python-dotenv (for local development)

Create a .env file to keep your secrets, then load it securely using python-dotenv.

# .env

API_KEY=your_api_key_here
Install the library:

pip install python-dotenv
Then use it in your code:

from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("API_KEY")
3. Use Secret Management Services (for Production)

For production environments, use secret managers like:

AWS Secrets Manager
Azure Key Vault
Google Secret Manager
HashiCorp Vault
These services:

Store secrets in encrypted form.
Control access via IAM policies.
Rotate secrets automatically.

62. What is a Walrus Operator?
The Walrus Operator (:=) is a new feature introduced in Python 3.8. It allows you to assign a value to a variable and return the value within a single expression. This is known as an assignment expression, and is very helpful in making the Python code simpler, more readable, especially when the unwanted variables need to be avoided. The walrus operators are very helpful in loops and conditional statements in Python. Example:

```py
numbers = [1, 2, 3, 4, 5]

# Using the walrus operator
while (n := len(numbers)) > 0:
     print(numbers.pop())

```

## Does Python support Switch Case?

No, Python does not have a built-in switch statement like some other languages (such as C or Java). Instead, Python developers typically use Match and Case, if-elif-else chains, or dictionary mappings to achieve similar functionality, as these approaches help in writing cleaner and more readable code, compared to the traditional switch case method.

## Does Python support multiple inheritance?

Yes, Python supports multiple inheritance, which means a class can inherit from more than one parent class. In multiple inheritance, a class can have multiple base classes, and it inherits attributes and methods from all of them. This helps in increasing the reusability and the flexibility of the code. It is also confusing in cases like method resolution order (MRO), where multiple inheritance can result in an issue while searching a path.

Example:

```py
class Base1:
    # Body of 1st base class
    def __init__(self):
        print("Base1 initialized")

class Base2:
    # Body of 2nd base class
    def __init__(self):
        print("Base2 initialized")

class Derived(Base1, Base2):
    # Body of derived class
    def __init__(self):
        Base1.__init__(self)  # Calling constructor of Base1
        Base2.__init__(self)  # Calling constructor of Base2
        print("Derived class initialized")

# Example usage
d = Derived()


```

## How is memory managed in Python?

Memory management is handled by the Python memory manager in Python. The process of automatic memory management is done in Python by the Garbage Collector and Heap Space.

- Garbage collection is a built-in feature in Python that identifies and clears circular references automatically. Circular References are when two objects refer to each other, but aren’t needed by the program.
- A private heap memory contains all the Python objects and data structures.
Every object in Python has a reference count, which tracks how many variables or objects refer to that object. When the reference count drops to zero, Python frees up the memory for that object.
- Python uses a system of memory pools to optimize the allocation and deallocation of small objects. It improves performance, which helps in improving efficiency.

## What is multi-threading in Python?

Multithreading is a technique where the processors execute multiple threads concurrently within a single process. A thread is the smallest unit of a CPU’s execution that can run independently. By using multiple threads, a program can perform several tasks at the same time. This improves performance, especially for I/O-bound operations such as reading files, handling user inputs, and other similar tasks.

Example:

```py
import threading
import time

def show():
    for i in range(3):
        print(f"Running in thread: {threading.current_thread().name}")
        time.sleep(1)

# Create and start thread

t = threading.Thread(target=show)
t.start()

# Main thread continues

for i in range(3):
    print("Main thread working")
    time.sleep(1)

t.join()
print("Both threads finished.")
```

## Explain the use of yield in Python with an example

The yield keyword is used to create a generator function, which is used to return an iterator that helps in yielding one value at a time, instead of running the whole list at once. Using the yield keywords helps in making the memory more efficient, mainly when working on large datasets.

Example:

Python

```py
def countdown(n):
    while n > 0:
        yield n     # Yield the current value of n
        n -= 1     # Decrement n

# Using the generator
for number in countdown(5):
    print(number)

```

## What is the purpose of using super() in Python classes?

The super() function in Python is used to call methods from a parent class within a subclass. It is commonly used in object-oriented programming for ensuring that the parent class has been properly initialized, which helps in inheritance. The super() function helps in making the code simpler by avoiding the need to call the parent class again, when there is multiple inheritance.   Example:

```py
# Base class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_details(self):
        return f"Name: {self.name}, Age: {self.age}"

# Derived class
class Employee(Person):
    def __init__(self, name, age, id):
        # Call the constructor of the parent class using super()
        super().__init__(name, age)
        self.id = id

    def get_details(self):
        # Override the method to include employee ID
        return f"Name: {self.name}, Age: {self.age}, ID: {self.id}"

# Create an Employee object
emp = Employee("Lithin", 23, 1234)

# Print the details of the employee
print(emp.get_details())

```

## How do you identify missing values and deal with missing values in a Dataframe?

For identifying the missing values in the Pandas DataFrame, the isnull() and isna() functions can be used.

 missing_count=data_frame1.isnull().sum()
  There are two ways of handling the missing values :

1. Replace the  missing values with 0

df['col_name'].fillna(0)
2. Replace the missing values with the mean value of that column

<br>
df['col_name'] = df['col_name'].fillna((df['col_name'].mean()))<br>

## How do you load and preprocess data for machine learning in Python?

In Python loading and preprocessing data is very important step in any machine learning pipeline. Basically, structured and clean data enhance the accuracy and performance of model.

Here’s how to do it effectively in Python:

```py
1. Load Data Using Pandas or Numpy

import pandas as pd

# Load from CSV

df = pd.read_csv("data.csv")
2. Explore the Data

Use methods like .head(), .info(), .describe() to inspect structure and find out the missing or inconsistent values:

print(df.head())
print(df.info())
print(df.describe())
3. Handle Missing Values

# Fill missing values

df.fillna(method='ffill', inplace=True)

# Or drop missing rows

df.dropna(inplace=True)
4. Encode Categorical Variables

Convert non-numeric features into numeric format:

# Label encoding

df['Gender'] = df['Gender'].map({'Male': 0, 'Female': 1})

# One-hot encoding

df = pd.get_dummies(df, columns=['Country'])
5. Scale and Normalize Features

Use sklearn.preprocessing for standardization:

from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
df[['age', 'income']] = scaler.fit_transform(df[['age', 'income']])
6. Split the Data

from sklearn.model_selection import train_test_split

X = df.drop("target", axis=1)
y = df["target"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
```

## 48. How can you randomize the items of a list in Python?

To randomise the items in a list in Python, we use the `shuffle()` from the random module. Here is an example:

```py
import random

list1 = ["Intellipaat", "is", "the", "best", "edtech", "to", "learn", "python"]

# Shuffle the list items randomly
random.shuffle(list1)     # Shuffle the list items in random place

# Print the shuffled list
print(list1)


```

## . What do you understand about iterators in Python?

The Iterators in Python are objects that allow us to traverse through a collection (such as lists, tuples, dictionaries, or sets). They use the __iter__() and __next__() methods to retrieve the next element, until there are no methods left. Iterators are commonly used in for loops, and can be created for custom objects. They promote efficient memory usage and enable the lazy evaluation of elements in Python.

## 1. What is Reference Counter?

“Reference counter in Python is a mechanism used to keep track of how many references point to an object. Each object has a reference count. When the count drops to zero, the memory occupied by the object is automatically freed. This is part of Python’s memory management and helps in automatic garbage collection.”

- Python uses reference counting as a part of its memory management system.
- Every Python object keeps track of how many references point to it.
- This count is called the reference count.

2. How it Works

When you create a new reference to an object, the reference count increases.

When a reference is deleted or goes out of scope, the reference count decreases.

When the reference count becomes zero, Python automatically deletes the object from memory.

```py
import sys

a = [1, 2, 3]        # Create list object
print(sys.getrefcount(a))  # Output: 2 (1 from 'a', 1 from getrefcount argument)

b = a                 # New reference
print(sys.getrefcount(a))  # Output: 3

del b                 # Remove reference
print(sys.getrefcount(a))  # Output: 2

```

Explanation:

sys.getrefcount() shows the number of references pointing to the object.

When the reference count reaches 0, Python garbage collector frees the memory.
4. Why Reference Counting is Important

Prevents memory leaks by freeing unused objects.

Helps manage memory efficiently without manual intervention.

Works with Python’s garbage collector to clean cyclic references (cycles where objects reference each other).

## 1. What is a .pyc file?

- .pyc stands for Python Compiled file.
- It is a bytecode-compiled version of a Python .py source file.
- Python compiles .py files to bytecode before execution and stores it as .pyc for faster subsequent runs

“A .pyc file in Python is a compiled bytecode version of a .py source file. It is automatically generated by Python during module import to speed up execution by avoiding recompilation of unchanged source files. These files are stored in the __pycache__ directory.”

2. How .pyc files are generated

When you import a Python module, Python automatically compiles it to bytecode and stores it in the __pycache__ folder.

Example:
my_module.py

after importing
__pycache__/my_module.cpython-310.pyc

cpython-310 indicates Python version 3.10 used to compile.
3. Why .pyc files exist
Faster loading: Python can skip recompiling .py files on subsequent imports.

Portability: Bytecode is platform-independent within the same Python version.

Caching: Saves compilation time for large projects.

4. Key Points

.pyc files are not human-readable.

They are optional; Python can run .py files directly.

Stored in __pycache__ by default in Python 3.x.

Python automatically updates .pyc files if the .py source changes.

```py
# my_module.py
def hello():
    print("Hello World!")

# In Python shell
import my_module
my_module.hello()
```

## What is annotate in Django?

annotate() is a QuerySet method in Django ORM used to add summary or computed fields to each object in a queryset.

Typically used with aggregate functions like Count, Sum, Avg, Max, Min.

Adds the result as a new field for each object in the queryset.

2. Basic Syntax

```py
from django.db.models import Count, Sum, Avg
queryset.annotate(new_field=AggregateFunction('field_name'))
```

new_field → name of the computed field

AggregateFunction → Count, Sum, Avg, etc.

'field_name' → field to aggregate

Models:

```py
class Author(models.Model):
    name = models.CharField(max_length=100)

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    pages = models.IntegerField()
```

Use annotate() to count books per author:

```py
from django.db.models import Count

authors = Author.objects.annotate(num_books=Count('book'))
for author in authors:
    print(author.name, author.num_books)

```

Each Author object now has an extra field num_books.

Use annotate() to get total pages per author:

```py
from django.db.models import Sum

authors = Author.objects.annotate(total_pages=Sum('book__pages'))
for author in authors:
    print(author.name, author.total_pages)

```

annotate() adds computed fields to each object.

Often combined with aggregate() or filter() for more complex queries.

Works with related fields using Django’s double underscore (__).

5. Interview-Friendly Answer

“In Django, annotate() is a QuerySet method that allows you to add a calculated field to each object in the queryset. It’s commonly used with aggregate functions like Count, Sum, or Avg, and is very useful for reporting or summarizing related data.

## asynchronous programming

Async in Python

1. Definition

async is used to define asynchronous functions (also called coroutines) in Python.

These functions do not block the main thread while waiting for I/O operations.

Typically used with await to pause execution until the awaited task completes.

| Keyword     | Description                                               |
| ----------- | --------------------------------------------------------- |
| `async def` | Defines an asynchronous function (coroutine)              |
| `await`     | Waits for an asynchronous operation to complete           |
| `asyncio`   | Python’s library for managing async tasks and event loops |

```
import asyncio

async def fetch_data():
    print("Start fetching...")
    await asyncio.sleep(2)  # Simulates I/O operation
    print("Done fetching!")
    return {"data": 123}

async def main():
    print("Main started")
    result = await fetch_data()  # Wait for fetch_data to complete
    print(result)

# Run the event loop
asyncio.run(main())
```

Main started
Start fetching...
Done fetching!
{'data': 123}

asyncio.run(main()) starts the event loop.

await asyncio.sleep(2) simulates a non-blocking delay.

Why Use Async in Python?

Non-blocking I/O: Handles many tasks simultaneously without waiting.

Better performance for I/O-bound tasks (APIs, web scraping, DB queries).

Can replace traditional multithreading for certain scenarios with less overhead.

5. Important Notes

CPU-bound tasks do not benefit from async; use multiprocessing for those.

Async functions return coroutines, not actual results. You need await to get the result.

Async is widely used in FastAPI, aiohttp, and other asynchronous Python frameworks.

Async in Python allows functions to run asynchronously without blocking the main thread. Using async def and await, Python can handle multiple I/O-bound operations concurrently, which improves performance for tasks like network requests, database calls, or file operations.”

### 3. Difference Between List and Dict Comprehension

List Comprehension

Syntax:

```
    [expression for item in iterable if conditional]
```

Example:
Common Way:

```py
l = []
for i in range(10):
    if i%2:
        l.append(i)
print(l)

Using List Comprehension:
ls = [i for i in range(10) if i%2]
print(ls)

Output:
[1, 3, 5, 7, 9]
```

Dict Comprehension

Syntax :

```
     {key:value for (key,value) in iterable if conditional}
```

Example:
Common Way:

```py
d = {}
for i in range(1,10):
sqr = i*i
d[i] = i*i
print(d)

Using Dict Comprehension:
d1={n:n*n for n in range(1,10)}
print (d1)

Output:
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}
```

### 4. How Memory Managed In Python?

Memory management in Python involves a private heap containing all Python objects and data structures. Interpreter takes care of Python heap and that the programmer has no access to it.
The allocation of heap space for Python objects is done by Python memory manager. The core API of Python provides some tools for the programmer to code reliable and more robust program.
Python also has a build-in garbage collector which recycles all the unused memory. When an object is no longer referenced by the program, the heap space it occupies can be freed. The garbage collector determines objects which are no longer referenced by the program frees the occupied memory and make it available to the heap space.
The gc module defines functions to enable /disable garbage collector:

gc.enable() -Enables automatic garbage collection.
gc.disable() - Disables automatic garbage collection.

### 5. Difference Between Generators And Iterators

GENERATOR

Generators are iterators which can execute only once.
Generator uses “yield” keyword.
Generators are mostly used in loops to generate an iterator by returning all the values in the loop without affecting the iteration of the loop.
Every generator is an iterator.

 EXAMPLE:

```py
def sqr(n):
    for i in range(1, n+1):
        yield i*i 
a = sqr(3)  
print(next(a))
print(next(a))
print(next(a))
```

```
Output:
1
4
9
```

ITERATOR

An iterator is an object which contains a countable number of values and it is used to iterate over iterable objects like list, tuples, sets, etc.
Iterators are used mostly to iterate or convert other objects to an iterator using iter() function.
Iterator uses iter() and next() functions.
Every iterator is not a generator.

Example:

```py
iter_list = iter(['A', 'B', 'C'])
print(next(iter_list))
print(next(iter_list))
print(next(iter_list))
```

Output:
A
B
C

6. What is ‘init’ Keyword In Python?
__init__.py file
The __init__.py file lets the Python interpreter know that a directory contains code for a Python module. It can be blank. Without one, you cannot import modules from another folder into your project.
The role of the __init__.py file is similar to the __init__ function in a Python class. The file essentially the constructor of your package or directory without it being called such. It sets up how packages or functions will be imported into your other files.

__init__() function
The __init__ method is similar to constructors in C++ and Java. Constructors are used to initialize the object’s state.

```py
# A Sample class with init method  
class Person: 
    # init method or constructor   
    def __init__(self, name):  
        self.name = name  
      
    # Sample Method   
    def say_hi(self):  
        print('Hello, my name is', self.name)  
      
p = Person('Nitin')  
p.say_hi()   
```

Output:
Hello, my name is Nitin

### 7. Difference Between Modules and Packages in Python

Module

The module is a simple Python file that contains collections of functions and global variables and with having a .py extension file. It is an executable file and to organize all the modules we have the concept called Package in Python.

A module is a single file (or files) that are imported under one import and used. E.g.
import my_module

Package

The package is a simple directory having collections of modules. This directory contains Python modules and also having __init__.py file by which the interpreter interprets it as a Package. The package is simply a namespace. The package also contains sub-packages inside it.

A package is a collection of modules in directories that give a package hierarchy.
from my_package.abc import a

### 9. What are Generators. Explain it with Example

Generators are iterators which can execute only once.

Every generator is an iterator.

Generator uses “yield” keyword.

Generators are mostly used in loops to generate an iterator by returning all the values in the loop without affecting the iteration of the loop

```py
Example:
def sqr(n):
    for i in range(1, n+1):
        yield i*i 
a = sqr(3)  

print("The square are : ")
print(next(a))
print(next(a))
print(next(a))
```

Output:
The square are :  
1
4
9

### 10. What are in-built Data Types in Python

OR

#### Explain Mutable and Immutable Data Types

A first fundamental distinction that Python makes on data is about whether or not the value of an object changes.

DataType
Mutable Or Immutable?
Boolean (bool)
Immutable
Integer (int)
Immutable
Float
Immutable
String (str)
Immutable
tuple
Immutable
frozenset
Immutable
list
Mutable
set
Mutable
dict
Mutable

### 11. Explain Ternary Operator in Python?

The syntax for the Python ternary statement is as follows:

[if_true] if [expression] else [if_false]

Ternary Operator Example:

age = 25
discount = 5 if age < 65 else 10
print(discount)

### 12. What is Inheritance In Python

In inheritance, the child class acquires the properties and can access all the data members and functions defined in the parent class. A child class can also provide its specific implementation to the functions of the parent class.

In python, a derived class can inherit base class by just mentioning the base in the bracket after the derived class name.

Class A(B):  

```py
class A:  
    def display(self):  
        print("A Display")  

class B(A):  
    def show(self):  
        print("B Show")  
d = B()  
d.show()  
d.display()  


Output:
B Show
A Display
```

### 13. Difference Between Local and Global Variable in Python

 Local Variable
Global Variable
It is declared inside a function.
It is declared outside the function.
If it is not initialized, a garbage value is stored
If it is not initialized zero is stored as default.
It is created when the function starts execution and lost

when the functions terminate.
It is created before the program’s global execution starts and

lost when the program terminates.
Data sharing is not possible as data of the local variable can

be accessed by only one function.
Data sharing is possible as multiple functions can access the

same global variable.
Parameters passing is required for local variables to access

the value in other function
Parameters passing is not necessary for a global variable as it

is visible throughout the program
When the value of the local variable is modified in one

function, the changes are not visible in another function.
When the value of the global variable is modified in one

function changes are visible in the rest of the program.
Local variables can be accessed with the help of statements,

inside a function in which they are declared.
You can access global variables by any statement in the

program.
It is stored on the stack unless specified.
It is stored on a fixed location decided by the compiler.

### 14. Explain Break, Continue and Pass Statement

A break statement, when used inside the loop, will terminate the loop and exit. If used inside nested loops, it will break out from the current loop.
A continue statement will stop the current execution when used inside a loop, and the control will go back to the start of the loop.
A pass statement is a null statement. When the Python interpreter comes across the pass statement, it does nothing and is ignored.

```py
Break Statement Example

for i in range(10):    
    if i == 7:
        break  
    print( i, end = ",")

Output:
0,1,2,3,4,5,6,
```

```
Continue Statement Example

for i in range(10):    
    if i == 7:
        continue  
    print( i, end = ",")

Output:
0,1,2,3,4,5,6,8,9,
```

```
Pass Statement Example

def my_func():
    print('pass inside function')
    pass
my_func()

Output:
pass inside function
```

### 15. What is 'self' Keyword in python?

The ‘self’ parameter is a reference to the current instance of the class, and is used to access variables that belongs to the class.

```py
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(f"My name is {self.name}. I am {self.age} years old.")

c = Person("Nitin",23)
c.info()
```

Output:
My name is Nitin. I am 23 years old.

### 16. Difference Between Pickling and Unpickling?

Pickling:
In python, the pickle module accepts any Python object, transforms it into a string representation, and dumps it into a file by using the dump function. This process is known as pickling. The function used for this process is pickle.dump()
Unpickling:
The process of retrieving the original python object from the stored string representation is called unpickling.
The function used for this process is pickle.load()

They are inverses of each other.
Pickling, also called serialization, involves converting a Python object into a series of bytes which can be written out to a file.
Unpicking, or de-serialization, does the opposite–it converts a series of bytes into the Python object it represents.

17. Explain Function of List, Set, Tuple And Dictionary?
Functions Of List
sort(): Sorts the list in ascending order.
append(): Adds a single element to a list.
extend(): Adds multiple elements to a list.
index(): Returns the first appearance of the specified value.
max(list): It returns an item from the list with max value.
min(list): It returns an item from the list with min value.
len(list): It gives the total length of the list.
list(seq): Converts a tuple into a list.
cmp(list1, list2): It compares elements of both lists list1 and list2.
type(list): It returns the class type of an object.

Functions Of Tuple
cmp(tuple1, tuple2) - Compares elements of both tuples.
len(): total length of the tuple.
max(): Returns item from the tuple with max value.
min(): Returns item from the tuple with min value.
tuple(seq): Converts a list into tuple.
sum(): returns the arithmetic sum of all the items in the tuple.
any(): If even one item in the tuple has a Boolean value of True, it returns True. Otherwise, it returns False.
all(): returns True only if all items have a Boolean value of True. Otherwise, it returns False.
sorted(): a sorted version of the tuple.
index(): It takes one argument and returns the index of the first appearance of an item in a tuple
count(): It takes one argument and returns the number of times an item appears in the tuple.

Functions Of Dictionary
clear(): Removes all the elements from the dictionary
copy(): Returns a copy of the dictionary
fromkeys(): Returns a dictionary with the specified keys and value
get(): Returns the value of the specified key
items(): Returns a list containing a tuple for each key value pair
keys(): Returns a list containing the dictionary's keys
pop(): Removes the element with the specified key
popitem(): Removes the last inserted key-value pair
setdefault(): Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
update(): Updates the dictionary with the specified key-value pairs
values(): Returns a list of all the values in the dictionary
cmp(): compare two dictionaries

Functions Of Set
add(): Adds an element to the set
clear(): Removes all the elements from the set
copy(): Returns a copy of the set
difference(): Returns a set containing the difference between two or more sets
difference_update(): Removes the items in this set that are also included in another, specified set
discard(): Remove the specified item
intersection(): Returns a set, that is the intersection of two or more sets
intersection_update(): Removes the items in this set that are not present in other, specified set(s)
isdisjoint(): Returns whether two sets have a intersection or not
issubset(): Returns whether another set contains this set or not
issuperset(): Returns whether this set contains another set or not
pop(): Removes an element from the set
remove(): Removes the specified element
symmetric_difference(): Returns a set with the symmetric differences of two sets
symmetric_difference_update(): inserts the symmetric differences from this set and another
union(): Return a set containing the union of sets
update(): Update the set with another set, or any other iterable

### 18. What are Python Iterators?

An iterator is an object which contains a countable number of values and it is used to iterate over iterable objects like list, tuples, sets, etc.
Iterators are used mostly to iterate or convert other objects to an iterator using iter() function.
Iterator uses iter() and next() functions.
Every iterator is not a generator.

```py
Example:

iter_list = iter(['A', 'B', 'C'])
print(next(iter_list))
print(next(iter_list))
print(next(iter_list))

Output:
A
B
C
```

19. Explain Type Conversion in Python.
      [(int(), float(), ord(), oct(), str() etc.)]
int() - Converts any data type into an integer.
float() - Returns A floating point number from a number or string
oct() - Returns its octal representation in a string format.
hex() - Convert the integer into a suitable hexadecimal form for the number of the integer.
ord() - Returns the integer of the Unicode point of the character in the Unicode case or the byte value in the case of an 8-bit argument.
chr(number) - Returns the character (string) from the integer (represents unicode code point of the character).
eval() - Parses the expression argument and evaluates it as a python expression.
str() - Convert a value (integer or float) into a string.
repr() - Returns the string representation of the value passed to eval function by default. For the custom class object, it returns a string enclosed in angle brackets that contains the name and address of the object by default.

### 20. What does *args and **kwargs mean? Expain

When you are not clear how many arguments you need to pass to a particular function, then we use *args and **kwargs.

The *args keyword represents a varied number of arguments.  It is used to add together the values of multiple arguments

The **kwargs keyword represents an arbitrary number of arguments that are passed to a function.**kwargs keywords are stored in a dictionary. You can access each item by referring to the keyword you associated with an argument when you passed the argument.

```py
*args Python Example:

def sum(*args):
 total = 0
 for a in args:
  total = total + a
 print(total)

sum(1,2,3,4,5)

Output:
15
```

```py
**Kwargs Python Example

def show(**kwargs):
 print(kwargs)

show(A=1,B=2,C=3)


Output:
{'A': 1, 'B': 2, 'C': 3}
```

### 21. What is "Open" and "With" statement in Python?

Both Statements are used in case of file handling.
With the “With” statement, you get better syntax and exceptions handling.

```py
f = open("nitin.txt")
content = f.read()
print(content)
f.close()
```

```py
with open("nitin.txt") as f:
 content = f.read()
 print(content)
```

### 22. Different Ways To Read And Write In A File In Python?

Syntax of Python open file function:

file_object  = open("filename", "mode")

Read Only (‘r’) : Open text file for reading. The handle is positioned at the beginning of the file. If the file does not exists, raises I/O error. This is also the default mode in which file is opened.

Read and Write (‘r+’) : Open the file for reading and writing. The handle is positioned at the beginning of the file. Raises I/O error if the file does not exists.

Write Only (‘w’) : Open the file for writing. For existing file, the data is truncated and over-written. The handle is positioned at the beginning of the file. Creates the file if the file does not exists

Write and Read (‘w+’) : Open the file for reading and writing. For existing file, data is truncated and over-written. The handle is positioned at the beginning of the file.

Append Only (‘a’) : Open the file for writing. The file is created if it does not exist. The handle is positioned at the end of the file. The data being written will be inserted at the end, after the existing data.

Append and Read (‘a+’) : Open the file for reading and writing. The file is created if it does not exist. The handle is positioned at the end of the file. The data being written will be inserted at the end, after the existing data.

Text mode (‘t’): meaning \n characters will be translated to the host OS line endings when writing to a file, and back again when reading.

Exclusive creation (‘x’): File is created and opened for writing – but only if it doesn't already exist. Otherwise you get a FileExistsError.

Binary mode (‘b’): appended to the mode opens the file in binary mode, so there are also modes like 'rb', 'wb', and 'r+b'.

### 23. What is Pythonpath?

PYTHONPATH is an environment variable which you can set to add additional directories where python will look for modules and packages

The ‘PYTHONPATH’ variable holds a string with the name of various directories that need to be added to the sys.path directory list by Python.

The primary use of this variable is to allow users to import modules that are not made installable yet.

### 24. How Exception Handled In Python?

Try: This block will test the exceptional error to occur.

Except: Here you can handle the error.

Else: If there is no exception then this block will be executed.

Finally: Finally block always gets executed either exception is generated or not.

```
try:
      # Some Code....!

except:
      # Optional Block
      # Handling of exception (if required)

else:
      # Some code .....
      # execute if no exception

finally:
      # Some code .....(always executed)

```

26. What is ‘PIP’ In Python
Python pip is the package manager for Python packages. We can use pip to install packages that do not come with Python.

The basic syntax of pip commands in command prompt is:
pip 'arguments'
Pip install <package_name>

29. How to Get List of all keys in a Dictionary?

Using List:

```py
dct = {'A': 1, 'B': 2, 'C': 3}
all_keys = list(dct.keys())
print(all_keys)  # ['A', 'B', 'C']

Shortcut for Above Code:
dct = {'A': 1, 'B': 2, 'C': 3}
all_keys = list(dct)
print(all_keys)  # ['A', 'B', 'C']


Using Iterable Unpacking Operator:
d = {'A': 1, 'B': 2, 'C': 3}
x = [*d.keys()]
print(x)

Shortcut For Above Code:
d = {'A': 1, 'B': 2, 'C': 3}
x = [*d]
print(x)

Using Keys() Function:
d = {'A': 1, 'B': 2, 'C': 3}
x = d.keys()
print([k for k in x])


Using Iterable Unpacking Operator:
d = {'A': 1, 'B': 2, 'C': 3}
*x, = d.keys()
print(x)

Shortcut For Above Code:
d = {'A': 1, 'B': 2, 'C': 3}
*x, = d
print(x)
```

Output Is Same In All 7 Cases:
['A', 'B', 'C']

30. Difference Between Abstraction and Encapsulation.

 Abstraction
Encapsulation
Abstraction works on the design level.
Encapsulation works on the application level.
Abstraction is implemented to hide unnecessary data and withdrawing

relevant data.
Encapsulation is the mechanism of hiding the code and the data

together from the outside world or misuse.
It highlights what the work of an object instead of how the object

works is
It focuses on the inner details of how the object works. Modifications

can be done later to the settings.
Abstraction focuses on outside viewing, for example, shifting the car.
Encapsulation focuses on internal working or inner viewing, for

example, the production of the car.
Abstraction is supported in Java with the interface and the abstract

class.
Encapsulation is supported using, e.g. public, private and secure

access modification systems.
In a nutshell, abstraction is hiding implementation with the help of an

interface and an abstract class.
 In a nutshell, encapsulation is hiding the data with the help of getters

and setters.

31. Does Python Support Multiple Inheritance. (Diamond Problem)

Yes, Python Supports Multiple Inheritance.

What Is Diamond Problem?
What Java does not allow is multiple inheritance where one class can inherit properties from more than one class. It is known as the diamond problem.

```py
class A  
{
  public void display()  
    {
      System.out.println("class A");
    }  
}

class B extends A  
{ 
  @Override  
    public void display()  
    {  
      System.out.println("class B");  
    }  
} 

class C extends A  
{  
  @Override  
    public void display()  
      {  
        System.out.println("class C");  
       }  
} 

//not supported in Java  
public class D extends B,C  
{  
public static void main(String args[])  
{  
D d = new D();  
//creates ambiguity which display() method to call  
d.display();   
}  
}  
```

In the above figure, we find that class D is trying to inherit form class B and class C, that is not allowed in Java.

```py
Multiple Inheritance In Python:


class A:
 def abc(self):
  print("a")

class B(A):
 def abc(self):
  print("b")

class C(A):
 def abc(self):
  print("c")

class D(B,C):
 pass

d = D()
d.abc()
```

Output:
b

32. How to initialize Empty List, Tuple, Dict and Set?

Empty List:
a = []

Empty Tuple:
a = ()

Empty Dict:
a = {}
Empty Set:
a = set()

33. Difference Between .py and .pyc
.py files contain the source code of a program. Whereas, .pyc file contains the bytecode of your program.
Python compiles the .py files and saves it as .pyc files , so it can reference them in subsequent invocations.
The .pyc contain the compiled bytecode of Python source files. This code is then executed by Python's virtual machine .

34. How Slicing Works In String Manipulation. Explain.

Syntax: Str_Object[Start_Position:End_Position:Step]

s = 'HelloWorld'

Indexing:

print(s[:])

Output:
HelloWorld
print(s[:])  #HelloWorld
print(s[::])  #HelloWorld
print(s[:5])  #Hello
print(s[2:5])  #llo
print(s[2:8:2])  #loo
print(s[8:1:-1])  #lroWoll
print(s[-4:-2])  #or
print(s[::-1])  #dlroWolleH

35. Can You Concatenate Two Tuples. If Yes, How Is It Possible?        Since it is Immutable?

How To Concatenate Two Tuple:

t1 = (1,2,3)
t2 = (7,9,10)
t1 = t1 + t2
print("After concatenation is : ", t1 )

Output:
After concatenation is :  (1, 2, 3, 7, 9, 10)

Why Tuple Is Immutable and List Is Mutable?

tuple_1 = (1,2,3)
print(id(tuple_1))  #140180965800128
tuple_2 = (7,9,10)
print(id(tuple_2))  #140180965665600
tuple_1 = tuple_1 + tuple_2
tuple_3 = tuple_1
print("The tuple after concatenation is : ", tuple_1 )

# The tuple after concatenation is :  (1, 2, 3, 7, 9, 10)

print(id(tuple_3))  #140180966177280

list_1 = [1,2,3]
print(id(list_1))  #140180965602048
list_2 = [7,9,10]
print(id(list_2))  #140180965601408
list_1.extend(list_2)
list_3 = list_1
print("The List after concatenation is : ", list_1 )

# The List after concatenation is :  [1, 2, 3, 7, 9, 10]

print(id(list_3))  #140180965602048

36. Difference Between Python Arrays and Lists

LIST

ARRAY

The list can store the value of different types.

It can only consist of value of same type.

The list cannot handle the direct arithmetic operations.

It can directly handle arithmetic operations.

The lists are the build-in data structure so we don't need to

import it.

We need to import the array before work with the array

The lists are less compatible than the array to store the data.

An array are much compatible than the list.

It consumes a large memory.

It is a more compact in memory size comparatively list.

It is suitable for storing the longer sequence of the data item.

It is suitable for storing shorter sequence of data items.

We can print the entire list using explicit looping.

We can print the entire list without using explicit looping.

### 37. What Is _a, __a,  __a__ in Python?

_a
Python doesn't have real private methods, so one underline in the beginning of a variable/function/method name means it's a private variable/function/method and It is for internal use only
We also call it weak Private

__a
Leading double underscore tell python interpreter to rewrite name in order to avoid conflict in subclass.
Interpreter changes variable name with class extension and that feature known as the Mangling.
In Mangling python interpreter modify variable name with__.
So Multiple time It use as the Private member because another class can not access that variable directly.
Main purpose for __ is to use variable/method in class only If you want to use it outside of the class you can make public api.

__a__
Name with start with __ and ends with same considers special methods in Python.
Python provide this methods to use it as the operator overloading depending on the user.
Python provides this convention to differentiate between the user defined function with the module’s function

### 38. How To Read Multiple Values From Single Input?

By Using Split()

```py
x = list(map(int, input("Enter a multiple value: ").split()))
print("List of Values: ", x)

x = [int(x) for x in input("Enter multiple value: ").split()]
print("Number of list is: ", x)

x = [int(x) for x in input("Enter multiple value: ").split(",")]
print("Number of list is: ", x)
```

### 39. How To Copy and Delete A Dictionary

```py
Delete By Using clear():
d1 = {'A':1,'B':2,'C':3}
d1.clear()
print(d1)  #{}

Delete By Using pop():
d1 = {'A':1,'B':2,'C':3}
print(d1) #{'A': 1, 'B': 2, 'C': 3}
d1.pop('A')
print(d1)  # {'B': 2, 'C': 3}

Delete By Using del():
del d1['B']
print(d1)  # {'C': 3}
```

```py
Copy A Dictionary Using copy():
d2 = {'A':1,'B':2,'C':3}
print(d2)  # {'A': 1, 'B': 2, 'C': 3}
d3 = d2.copy()
print(d3)  # {'A': 1, 'B': 2, 'C': 3}

Copy A Dictionary Using ‘=’:
d2 = {'A':1,'B':2,'C':3}
print(d2)  # {'A': 1, 'B': 2, 'C': 3}
d3 = d2
print(d3) # {'A': 1, 'B': 2, 'C': 3}

```

```py
Benefit Of Using Copy():
d2 = {'A':1,'B':2,'C':3}
print(d2)  # {'A': 1, 'B': 2, 'C': 3}
d3 = d2.copy()
print(d3)  # {'A': 1, 'B': 2, 'C': 3}
del d2['B']
print(d2)   # {'A': 1, 'C': 3}
print(d3)   # {'A': 1, 'B':2, 'C': 3}

DrawBack Of Using ‘=’
d2 = {'A':1,'B':2,'C':3}
print(d2)  # {'A': 1, 'B': 2, 'C': 3}
d3 = d2
print(d3) # {'A': 1, 'B': 2, 'C': 3}
del d2['B']
print(d2)  # {'A': 1, 'C': 3}
print(d3)  # {'A': 1, 'C': 3}
```

40. Difference Between Anonymous and Lambda Function

Lambda function:

It can have any number of arguments but only one expression.
The expression is evaluated and returned.
Lambda functions can be used wherever function objects are required.

Anonymous function:

In Python, Anonymous function is a function that is defined without a name.
While normal functions are defined using the def keyword, Anonymous functions are defined using the lambda keyword.
Hence, anonymous functions are also called lambda functions.

Syntax:

lambda [arguments] : expression

Example:

square = lambda x : x * x
square(5) #25

The above lambda function definition is the same as the following function:
def square(x):
    return x * x

Anonymous Function:  We can declare a lambda function and call it as an anonymous function, without assigning it to a variable.
print((lambda x: x*x)(5))

Above, lambda x: x*x defines an anonymous function and call it once by passing arguments in the parenthesis (lambda x: x*x)(5).

## 41. How to achieve Multiprocessing and Multithreading in Python?

Multithreading:

It is a technique where multiple threads are spawned by a process to do different tasks, at about the same time, just one after the other.
This gives you the illusion that the threads are running in parallel, but they are actually run in a concurrent manner.
In Python, the Global Interpreter Lock (GIL) prevents the threads from running simultaneously.

Multiprocessing:

It is a technique where parallelism in its truest form is achieved.
Multiple processes are run across multiple CPU cores, which do not share the resources among them.
Each process can have many threads running in its own memory space.
In Python, each process has its own instance of Python interpreter doing the job of executing the instructions.

```py
# importing the multiprocessing module
import multiprocessing

def print_cube(num):
 print("Cube: {}".format(num * num * num))

def print_square(num):
 print("Square: {}".format(num * num))

if __name__ == "__main__":
 # creating processes
 p1 = multiprocessing.Process(target=print_square, args=(10, ))
 p2 = multiprocessing.Process(target=print_cube, args=(10, ))
 p1.start()
 p2.start()
 # wait until process 1 is finished
 p1.join()
 p2.join()

 # both processes finished
 print("Done!")
```

```py
# A multithreaded program in python
import time
from threading import Thread
num= 0

# The bottleneck of the code which is CPU-bound
def upgrade(n):
while num<400000000:
num=num+1

# Creation of multiple threads
t1 = Thread(target=upgrade, args=(num//2,))
t2 = Thread(target=upgrade, args=(num//2,))

# multi thread architecture, recording time
start = time.time()
t1.start()
t2.start()
t1.join()
t2.join()
end = time.time()

print('Time taken in seconds -', end - start)
```

## 42. What is GIL. Explain

The Global Interpreter Lock (GIL) of Python allows only one thread to be executed at a time. It is often a hurdle, as it does not allow multi-threading in python to save time

The Python Global Interpreter Lock or GIL, in simple words, is a mutex (or a lock) that allows only one thread to hold the control of the Python interpreter.

This means that only one thread can be in a state of execution at any point in time. The impact of the GIL isn’t visible to developers who execute single-threaded programs, but it can be a performance bottleneck in CPU-bound and multi-threaded code.

Since the GIL allows only one thread to execute at a time even in a multi-threaded architecture with more than one CPU core, the GIL has gained a reputation as an “infamous” feature of Python.

Basically, GIL in Python doesn’t allow multi-threading which can sometimes be considered as a disadvantage.

### 43. How Class and Object Created in Python?

Python is an object oriented programming language.
Almost everything in Python is an object, with its properties and methods.
A Class is like an object constructor, or a "blueprint" for creating objects.

Create a Class:
To create a class, use the keyword ‘class’:
class MyClass:
  x = 5

Create Object:
Now we can use the class named MyClass to create objects:
(Create an object named obj, and print the value of x:)

obj= MyClass()
print(obj.x)

44. Explain Namespace and Its Types in Python.
Namespace:

In python we deal with variables, functions, libraries and modules etc.
There is a chance the name of the variable you are going to use is already existing as name of another variable or as the name of another function or another method.
In such scenario, we need to learn about how all these names are managed by a python program. This is the concept of namespace.
Categories Of Namespace: Following are the three categories of namespace

Local Namespace: All the names of the functions and variables declared by a program are held in this namespace. This namespace exists as long as the program runs.

Global Namespace: This namespace holds all the names of functions and other variables that are included in the modules being used in the python program. It includes all the names that are part of the Local namespace.

Built-in Namespace: This is the highest level of namespace which is available with default names available as part of the python interpreter that is loaded as the programing environment. It include Global Namespace which in turn include the local namespace.

We can access all the names defined in the built-in namespace as follows.
builtin_names = dir(__builtins__)
for name in builtin_names:
    print(name)

45. Explain Recursion by Reversing a List.

```py
def reverseList(lst):
    if not lst:
        return []
    return [lst[-1]] + reverseList(lst[:-1])

print(reverseList([1, 2, 3, 4, 5]))

Output:
[5,4,3,2,1]
```

46. What are Unittests in Python
Unit Testing is the first level of software testing where the smallest testable parts of a software are tested. This is used to validate that each unit of the software performs as designed. The unittest test framework is python's xUnit style framework. This is how you can import it.

import unittest

Unit testing is a software testing method by which individual units of source code are put under various tests to determine whether they are fit for use (Source). It determines and ascertains the quality of your code.
Generally, when the development process is complete, the developer codes criteria, or the results that are known to be potentially practical and useful, into the test script to verify a particular unit's correctness. During test case execution, various frameworks log tests that fail any criterion and report them in a summary.
The developers are expected to write automated test scripts, which ensures that each and every section or a unit meets its design and behaves as expected.
Though writing manual tests for your code is definitely a tedious and time-consuming task, Python's built-in unit testing framework has made life a lot easier.
The unit test framework in Python is called unittest, which comes packaged with Python.
Unit testing makes your code future proof since you anticipate the cases where your code could potentially fail or produce a bug. Though you cannot predict all of the cases, you still address most of them.

### 47. How to use Map, Filter and Reduce Function in Python?

Map() Function

The map() function iterates through all items in the given iterable and executes the function we passed as an argument on each of them.

The syntax is:
map(function, iterable(s))

fruit = ["Apple", "Banana", "Pear"]
map_object = map(lambda s: s[0] == "A", fruit)
print(list(map_object))

Output:
[True, False, False]

Filter() Function

The filter() function takes a function object and an iterable and creates a new list.
As the name suggests, filter() forms a new list that contains only elements that satisfy a certain condition, i.e. the function we passed returns True.

The syntax is:
filter(function, iterable(s))

fruit = ["Apple", "Banana", "Pear"]
filter_object = filter(lambda s: s[0] == "A", fruit)
print(list(filter_object))

Output:
['Apple', 'Apricot']

Reduce() Function

The reduce() Function  works differently than map() and filter(). It does not return a new list based on the function and iterable we've passed. Instead, it returns a single value.

Also, in Python 3 reduce() isn't a built-in function anymore, and it can be found in the functools module.

The syntax is:
reduce(function, sequence[, initial])

from functools import reduce
list = [2, 4, 7, 3]
print(reduce(lambda x, y: x + y, list))
print("With an initial value: " + str(reduce(lambda x, y: x + y, list, 10)))

Output:
16
With an initial value: 26

48. Difference Between Shallow Copy and Deep Copy

Shallow Copy:
Shallow copies duplicate as little as possible. A shallow copy of a collection is a copy of the collection structure, not the elements. With a shallow copy, two collections now share the individual elements.

Shallow copying is creating a new object and then copying the non static fields of the current object to the new object. If the field is a value type, a bit by bit copy of the field is performed. If the field is a reference type, the reference is copied but the referred object is not, therefore the original object and its clone refer to the same object.

Deep Copy:
Deep copies duplicate everything. A deep copy of a collection is two collections with all of the elements in the original collection duplicated.

Deep copy is creating a new object and then copying the non-static fields of the current object to the new object. If a field is a value type, a bit by bit copy of the field is performed. If a field is a reference type, a new copy of the referred object is performed. A deep copy of an object is a new object with entirely new instance variables, it does not share objects with the old. While performing Deep Copy the classes to be cloned must be flagged as [Serializable].

49. How An Object Be Copied in Python
You can Explain Deep Copy and Shallow Copy In This
50. What does term MONKEY PATCHING refer to in python?
In Python, the term monkey patch refers to dynamic (or run-time) modifications of a class or module. In Python, we can actually change the behavior of code at run-time.

# monkey.py

class A:
     def func(self):
          print ("func() is called")

We use above module (monkey) in below code and change behavior of func() at run-time by assigning different value.

import monkey
def monkey_func(self):
 print ("monkey_func() is called")

# replacing address of "func" with "monkey_func"

monkey.A.func = monkey_func
obj = monkey.A()

# calling function "func" whose address got replaced

# with function "monkey_func()"

obj.func()

Examples:
Output :monkey_func() is called

51. What is Operator Overloading & Dunder Method.
Dunder methods in Python are special methods.
In Python, we sometimes see method names with a double underscore (__), such as the __init__ method that every class has. These methods are called “dunder” methods.
In Python, Dunder methods are used for operator overloading and customizing some other function’s behavior.

Some Examples:
- __add__(self, other)
– __sub__(self, other)

* __mul__(self, other)
/ __truediv__(self, other)
// __floordiv__(self, other)
% __mod__(self, other)
** __pow__(self, other)

>> __rshift__(self, other)
<< __lshift__(self, other)
& __and__(self, other)
| __or__(self, other)
^ __xor__(self, other)

52. Draw Pattern.

# This is the example of print simple pyramid pattern  

n = int(input("Enter the number of rows"))  

# outer loop to handle number of rows  

for i in range(0, n):  
    # inner loop to handle number of columns  
    # values is changing according to outer loop  
        for j in range(0, i + 1):  
            # printing stars  
            print("* ", end="")
  
        # ending line after each row  
        print()  

Output:
*
- *

* * *
* * * *
* * * * *

-  
- -  

* * *  
* * * *  
* * *  
- -  
-

             * 
             * * 
            * * * 
           * * * * 
            * * * 
             * * 
              *

     * 
     * * 
    * * * 
   * * * *
  * * * * *
