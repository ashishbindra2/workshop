
## POLYMORPHISM

poly means many. Morphs means forms.  
Polymorphism means 'Many Forms'.

Eg1: Yourself is best example of polymorphism.In front of Your parents You will have one type of behaviour and with friends another type of behaviour.Same person but different behaviours at different places,which is nothing but polymorphism.

Eg2: + operator acts as concatenation and arithmetic addition

Eg3: * operator acts as multiplication and repetition operator

Eg4: The Same method with different implementations in Parent class and child classes.(overriding)

Related to Polymorphism the following 4 topics are important

1) Duck Typing Philosophy of Python

2) Overloading
3) Operator Overloading
4) Method Overloading
5) Constructor Overloading

6) Overriding
7) Method Overriding
8) Constructor Overriding

### 1) Duck Typing Philosophy of Python

In Python we cannot specify the type explicitly. Based on provided value at runtime the type will be considered automatically. Hence Python is considered as Dynamically Typed Programming Language.

def f1(obj):  
obj.talk()

**What is the Type of obj? We cannot decide at the Beginning. At Runtime we**

**can Pass any Type. Then how we can decide the Type?**

At runtime if 'it walks like a duck and talks like a duck,it must be duck'. Python follows this principle. This is called Duck Typing Philosophy of Python.

```python
class Duck:
    def talk(self):
        print('Quack.. Quack..')

class Dog:
    def talk(self):
        print('Bow Bow..')

class Cat:
    def talk(self):
        print('Moew Moew ..')

class Goat:
    def talk(self):
        print('Myaah Myaah ..')

def f1(obj):
    obj.talk()

l=[Duck(),Cat(),Dog(),Goat()]
for obj in l:
    f1(obj)
```

**Output:**

```
Quack.. Quack..
Moew Moew ..
Bow Bow..
Myaah Myaah ..
```

The problem in this approach is if obj does not contain talk() method then we will get AttributeError.

```python
class Duck:
    def talk(self):
        print('Quack.. Quack..')

class Dog:
    def bark(self):
        print('Bow Bow..')
def f1(obj):
    obj.talk()

d=Duck()
f1(d)

d=Dog()
f1(d)
```

**Output:**

```
D:\durga_classes>py test.py
Quack.. Quack..
Traceback (most recent call last):
 File "test.py", line 22, in <module>
  f1(d)
 File "test.py", line 13, in f1
  obj.talk()
AttributeError: 'Dog' object has no attribute 'talk'
```

But we can solve this problem by using hasattr() function.

hasattr(obj,'attributename') → attributename can be Method Name OR Variable Name

### Demo Program with hasattr() Function

```python
class Duck:
    def talk(self):
        print('Quack.. Quack..')

class Human:
    def talk(self):
        print('Hello Hi...')

class Dog:
    def bark(self):
        print('Bow Bow..')

def f1(obj):
    if hasattr(obj,'talk'):
        obj.talk()
    elif hasattr(obj,'bark'):
        obj.bark()

d=Duck()
f1(d)

h=Human()
f1(h)

d=Dog()
f1(d)
Myaah Myaah Myaah...
```

### 2) Overloading

We can use same operator or methods for different purposes.

Eg 1: + operator can be used for Arithmetic addition and String concatenation  
print(10+20)#30  
print('durga'+'soft')#durgasoft

Eg 2: *operator can be used for multiplication and string repetition purposes.  
print(10*20)#200  
print('durga'*3)#durgadurgadurga

Eg 3: We can use deposit() method to deposit cash or cheque or dd  
deposit(cash)  
deposit(cheque)  
deposit(dd)

There are 3 types of Overloading

1) Operator Overloading
2) Method Overloading
3) Constructor Overloading

### 1) Operator Overloading

- We can use the same operator for multiple purposes, which is nothing but operator overloading.
- Python supports operator overloading.

Eg 1: + operator can be used for Arithmetic addition and String concatenation  
print(10+20)#30  
print('durga'+'soft')#durgasoft

Eg 2: *operator can be used for multiplication and string repetition purposes.  
print(10*20)#200  
print('durga'*3)#durgadurgadurga

### Demo program to use + operator for our class objects

```python
class Book:
    def __init__(self,pages):
        self.pages=pages

b1=Book(100)
b2=Book(200)
print(b1+b2)
```

D:\durga_classes>py test.py  
Traceback (most recent call last):  
File "test.py", line 7, in <module>  
print(b1+b2)  
TypeError: unsupported operand type(s) for +: 'Book' and 'Book'

- We can overload + operator to work with Book objects also. i.e Python supports Operator Overloading.
- For every operator Magic Methods are available. To overload any operator we have to override that Method in our class.
- Internally + operator is implemented by using **add**() method.This method is called magic method for + operator. We have to override this method in our class.

### Demo Program to Overload + Operator for Our Book Class Objects

```python
class Book:
    def __init__(self,pages):
        self.pages=pages

    def __add__(self,other):
        return self.pages+other.pages

b1=Book(100)
b2=Book(200)
print('The Total Number of Pages:',b1+b2)
```

**Output: The Total Number of Pages: 300**

The following is the list of operators and corresponding magic methods.

| # | Operator | Magic Method |
| --- | --- | --- |
| 1 | `+` | `object.__add__(self,other)` |
| 2 | `-` | `object.__sub__(self,other)` |
| 3 | `*` | `object.__mul__(self,other)` |
| 4 | `/` | `object.__div__(self,other)` |
| 5 | `//` | `object.__floordiv__(self,other)` |
| 6 | `%` | `object.__mod__(self,other)` |
| 7 | `**` | `object.__pow__(self,other)` |
| 8 | `+=` | `object.__iadd__(self,other)` |
| 9 | `-=` | `object.__isub__(self,other)` |
| 10 | `*=` | `object.__imul__(self,other)` |
| 11 | `/=` | `object.__idiv__(self,other)` |
| 12 | `//=` | `object.__ifloordiv__(self,other)` |
| 13 | `%=` | `object.__imod__(self,other)` |
| 14 | `**=` | `object.__ipow__(self,other)` |
| 15 | `<` | `object.__lt__(self,other)` |
| 16 | `<=` | `object.__le__(self,other)` |
| 17 | `>` | `object.__gt__(self,other)` |
| 18 | `>=` | `object.__ge__(self,other)` |
| 19 | `==` | `object.__eq__(self,other)` |
| 20 | `!=` | `object.__ne__(self,other)` |

### Overloading > and <= Operators for Student Class Objects

```python
class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def __gt__(self,other):
        return self.marks>other.marks
    def __le__(self,other):
        return self.marks<=other.marks

print("10>20 =",10>20)
s1=Student("Durga",100)
s2=Student("Ravi",200)
print("s1>s2=",s1>s2)
print("s1<s2=",s1<s2)
print("s1<=s2=",s1<=s2)
print("s1>=s2=",s1>=s2)
```

**Output:**

```
10>20 = False
s1>s2= False
s1<s2= True
s1<=s2= True
s1>=s2= False
```

**Program to Overload Multiplication Operator to Work on Employee Objects:**

```python
class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    def __mul__(self,other):
        return self.salary*other.days

class TimeSheet:
    def __init__(self,name,days):
        self.name=name
        self.days=days

e=Employee('Durga',500)
t=TimeSheet('Durga',25)
print('This Month Salary:',e*t)
```

**Output: This Month Salary: 12500**

### 2) Method Overloading

- If 2 methods having same name but different type of arguments then those methods are said to be overloaded methods.  
Eg: m1(int a)  
m1(double d)

- But in Python Method overloading is not possible.
- If we are trying to declare multiple methods with same name and different number of arguments then Python will always consider only last method.

### Demo Program

```python
class Test:
    def m1(self):
        print('no-arg method')
    def m1(self,a):
        print('one-arg method')
    def m1(self,a,b):
        print('two-arg method')

t=Test()
#t.m1()
#t.m1(10)
t.m1(10,20)
```

Output: two-arg method

In the above program python will consider only last method.

### How we can handle Overloaded Method Requirements in Python

Most of the times, if method with variable number of arguments required then we can handle with default arguments or with variable number of argument methods.

### Demo Program with Default Arguments

```python
class Test:
    def sum(self,a=None,b=None,c=None):
        if a!=None and b!= None and c!= None:
            print('The Sum of 3 Numbers:',a+b+c)
        elif a!=None and b!= None:
            print('The Sum of 2 Numbers:',a+b)
        else:
            print('Please provide 2 or 3 arguments')
t=Test()
t.sum(10,20)
t.sum(10,20,30)
t.sum(10)
```

**Output:**

```
The Sum of 2 Numbers: 30
The Sum of 3 Numbers: 60
Please provide 2 or 3 arguments
```

### Demo Program with Variable Number of Arguments

```python
class Test:
    def sum(self,*a):
        total=0
        for x in a:
            total=total+x
        print('The Sum:',total)

t=Test()
t.sum(10,20)
t.sum(10,20,30)
t.sum(10)
t.sum()
```

### 3) Constructor Overloading

- Constructor overloading is not possible in Python.
- If we define multiple constructors then the last constructor will be considered.

```python
class Test:
    def __init__(self):
        print('No-Arg Constructor')

    def __init__(self,a):
        print('One-Arg constructor')

    def __init__(self,a,b):
        print('Two-Arg constructor')
#t1=Test()
#t1=Test(10)
t1=Test(10,20)
```

Output: Two-Arg constructor

- In the above program only Two-Arg Constructor is available.
- But based on our requirement we can declare constructor with default arguments and variable number of arguments.

### Constructor with Default Arguments

```python
class Test:
    def __init__(self,a=None,b=None,c=None):
        print('Constructor with 0|1|2|3 number of arguments')

t1=Test()
t2=Test(10)
t3=Test(10,20)
t4=Test(10,20,30)
```

**Output:**

```
Constructor with 0|1|2|3 number of arguments
Constructor with 0|1|2|3 number of arguments
Constructor with 0|1|2|3 number of arguments
Constructor with 0|1|2|3 number of arguments
```

### Constructor with Variable Number of Arguments

```python
class Test:
    def __init__(self,*a):
        print('Constructor with variable number of arguments')

t1=Test()
t2=Test(10)
t3=Test(10,20)
t4=Test(10,20,30)
t5=Test(10,20,30,40,50,60)
```

**Output:**

```
Constructor with variable number of arguments
Constructor with variable number of arguments
Constructor with variable number of arguments
Constructor with variable number of arguments
Constructor with variable number of arguments
```

### 3) Overriding

### Method Overriding

- What ever members available in the parent class are bydefault available to the child  
class through inheritance. If the child class not satisfied with parent class  
implementation then child class is allowed to redefine that method in the child class based on its requirement. This concept is called overriding.
- Overriding concept applicable for both methods and constructors.

### Demo Program for Method Overriding

```python
class P:
    def property(self):
        print('Gold+Land+Cash+Power')
    def marry(self):
        print('Appalamma')
class C(P):
    def marry(self):
        print('Katrina Kaif')

c=C()
c.property()
c.marry()
```

**Output:**

```
Gold+Land+Cash+Power
Katrina Kaif
```

From Overriding method of child class,we can call parent class method also by using super() method.

```python
class P:
    def property(self):
        print('Gold+Land+Cash+Power')
    def marry(self):
        print('Appalamma')
class C(P):
    def marry(self):
        super().marry()
        print('Katrina Kaif')

c=C()
c.property()
c.marry()
```

**Output:**

```
Gold+Land+Cash+Power
Appalamma
Katrina Kaif
```

### Demo Program for Constructor Overriding

```python
class P:
    def __init__(self):
        print('Parent Constructor')

class C(P):
    def __init__(self):
        print('Child Constructor')

c=C()
```

Output: Child Constructor  
In the above example,if child class does not contain constructor then parent class constructor will be executed

From child class constuctor we can call parent class constructor by using super() method.

### Demo Program to call Parent Class Constructor by using super()

```python
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

class Employee(Person):
    def __init__(self,name,age,eno,esal):
        super().__init__(name,age)
        self.eno=eno
        self.esal=esal

    def display(self):
        print('Employee Name:',self.name)
        print('Employee Age:',self.age)
        print('Employee Number:',self.eno)
        print('Employee Salary:',self.esal)

e1=Employee('Durga',48,872425,26000)
e1.display()
e2=Employee('Sunny',39,872426,36000)
e2.display()
```

**Output:**

```
Employee Name: Durga
Employee Age: 48
Employee Number: 872425
Employee Salary: 26000
```

Employee Name: Sunny  
Employee Age: 39  
Employee Number: 872426  
Employee Salary: 36000

# OOP’s Part - 4

### Agenda

**1) Abstract Method**

**2) Abstract class**

**3) Interface**

**4) Public,Private and Protected Members**

**5) **str**() Method**

**6) Difference between str() and repr() functions**

**7) Small Banking Application**

### Abstract Method

- Sometimes we don't know about implementation, still we can declare a method. Such types of methods are called abstract methods.i.e abstract method has only declaration but not implementation.
- In python we can declare abstract method by using @abstractmethod decorator as follows.

- @abstractmethod
- def m1(self): pass

- @abstractmethod decorator present in abc module. Hence compulsory we should  
import abc module,otherwise we will get error.
- abc → abstract base class module

```python
class Test:
    @abstractmethod
    def m1(self):
        pass
```

NameError: name 'abstractmethod' is not defined

**Eg:**

```python
from abc import *
class Test:
    @abstractmethod
    def m1(self):
        pass
```

**Eg:**

```python
from abc import *
class Fruit:
    @abstractmethod
    def taste(self):
        pass
```

Child classes are responsible to provide implemention for parent class abstract methods.

### Abstract class

Some times implementation of a class is not complete,such type of partially implementation classes are called abstract classes. Every abstract class in Python should be derived from ABC class which is present in abc module.

**Case-1:**

```python
from abc import *
class Test:
    pass

t=Test()
```

In the above code we can create object for Test class b'z it is concrete class and it does not conatin any abstract method.

**Case-2:**

```python
from abc import *
class Test(ABC):
    pass

t=Test()
```

In the above code we can create object, even it is derived from ABC class,b'z it does not contain any abstract method.

**Case-3:**

```python
from abc import *
class Test(ABC):
    @abstractmethod
    def m1(self):
        pass

t=Test()
```

TypeError: Can't instantiate abstract class Test with abstract methods m1

**Case-4:**

```python
from abc import *
class Test:
    @abstractmethod
    def m1(self):
        pass

t=Test()
```

We can create object even class contains abstract method b'z we are not extending ABC class.

**Case-5:**

```python
from abc import *
class Test:
    @abstractmethod
    def m1(self):
        print('Hello')

t=Test()
t.m1()
```

**Output: Hello**

**Conclusion:** If a class contains atleast one abstract method and if we are extending ABC  
class then instantiation is not possible.

"abstract class with abstract method instantiation is not possible"

Parent class abstract methods should be implemented in the child classes. Otherwise we cannot instantiate child class.If we are not creating child class object then we won't get any error.

**Case-1:**

```python
from abc import *
class Vehicle(ABC):
    @abstractmethod
    def noofwheels(self):
        pass

class Bus(Vehicle): pass
```

It is valid because we are not creating Child class object.

**Case-2:**

```python
from abc import *
class Vehicle(ABC):
    @abstractmethod
    def noofwheels(self):
        pass

class Bus(Vehicle): pass
b=Bus()
```

TypeError: Can't instantiate abstract class Bus with abstract methods noofwheels

**Note:** If we are extending abstract class and does not override its abstract method then child class is also abstract and instantiation is not possible.

```python
from abc import *
class Vehicle(ABC):
    @abstractmethod
    def noofwheels(self):
        pass

class Bus(Vehicle):
    def noofwheels(self):
        return 7

class Auto(Vehicle):
    def noofwheels(self):
        return 3
b=Bus()
print(b.noofwheels())#7

a=Auto()
print(a.noofwheels())#3
```

**Note:** Abstract class can contain both abstract and non-abstract methods also.

### Interfaces In Python

In general if an abstract class contains only abstract methods such type of abstract class is considered as interface.

```python
from abc import *
class DBInterface(ABC):
    @abstractmethod
    def connect(self):pass

    @abstractmethod
    def disconnect(self):pass

class Oracle(DBInterface):
    def connect(self):
        print('Connecting to Oracle Database...')
    def disconnect(self):
        print('Disconnecting to Oracle Database...')

class Sybase(DBInterface):
    def connect(self):
        print('Connecting to Sybase Database...')
    def disconnect(self):
        print('Disconnecting to Sybase Database...')

dbname=input('Enter Database Name:')
classname=globals()[dbname]
x=classname()
x.connect()
x.disconnect()
```

D:\durga_classes>py test.py  
Enter Database Name:Oracle  
Connecting to Oracle Database...  
Disconnecting to Oracle Database...

D:\durga_classes>py test.py  
Enter Database Name:Sybase  
Connecting to Sybase Database...  
Disconnecting to Sybase Database...

**Note:** The inbuilt function globals()[str] converts the string 'str' into a class name and returns the classname.  
**Demo Program-2:** Reading class name from the file

**config.txt**

EPSON

**test.py**

```python
from abc import *
class Printer(ABC):
    @abstractmethod
    def printit(self,text):pass

    @abstractmethod
    def disconnect(self):pass

class EPSON(Printer):
    def printit(self,text):
        print('Printing from EPSON Printer...')
        print(text)
    def disconnect(self):
        print('Printing completed on EPSON Printer...')

class HP(Printer):
    def printit(self,text):
        print('Printing from HP Printer...')
        print(text)
    def disconnect(self):
        print('Printing completed on HP Printer...')

with open('config.txt','r') as f:
    pname=f.readline()

classname=globals()[pname]
x=classname()
x.printit('This data has to print...')
x.disconnect()
```

**Output:**

```
Printing from EPSON Printer...
This data has to print...
Printing completed on EPSON Printer...
```

### Concreate class vs Abstract Class vs Inteface

1) If we dont know anything about implementation just we have requirement specification then we should go for interface.
2) If we are talking about implementation but not completely then we should go for abstract class. (partially implemented class).
3) If we are talking about implementation completely and ready to provide service then we should go for concrete class.

```python
from abc import *
class CollegeAutomation(ABC):
    @abstractmethod
    def m1(self): pass
    @abstractmethod
    def m2(self): pass
    @abstractmethod
    def m3(self): pass
class AbsCls(CollegeAutomation):
    def m1(self):
        print('m1 method implementation')
    def m2(self):
        print('m2 method implementation')

class ConcreteCls(AbsCls):
    def m3(self):
        print('m3 method implemnentation')

c=ConcreteCls()
c.m1()
c.m2()
c.m3()
```

### Public, Protected and Private Attributes

By default every attribute is public. We can access from anywhere either within the class or from outside of the class.  
**Eg: name = 'durga'**

Protected attributes can be accessed within the class anywhere but from outside of the  
class only in child classes. We can specify an attribute as protected by prefexing with _  
symbol.

**Syntax: _variablename = value**

**Eg: _name='durga'**

But is is just convention and in reality does not exists protected attributes.

private attributes can be accessed only within the class.i.e from outside of the class we cannot access. We can declare a variable as private explicitly by prefexing with 2 underscore symbols.

**syntax: __variablename=value**

**Eg: __name='durga'**

```python
class Test:
    x=10
    _y=20
    __z=30
    def m1(self):
        print(Test.x)
        print(Test._y)
        print(Test.__z)

t=Test()
t.m1()
print(Test.x)
print(Test._y)
print(Test.__z)
```

**Output:**

```
10
20
30
10
20
Traceback (most recent call last):
 File "test.py", line 14, in <module>
  print(Test.__z)
AttributeError: type object 'Test' has no attribute '__z'
```

### How to Access Private Variables from Outside of the Class

We cannot access private variables directly from outside of the class.  
But we can access indirectly as follows objectreference._classname__variablename

```python
class Test:
    def __init__(self):
        self.__x=10

t=Test()
print(t._Test__x)#10
```

### **str**() method

- Whenever we are printing any object reference internally **str**() method will be called which is returns string in the following format  
<**main**.classname object at 0x022144B0>

- To return meaningful string representation we have to override **str**() method.

```python
class Student:
    def __init__(self,name,rollno):
        self.name=name
        self.rollno=rollno

    def __str__(self):
        return 'This is Student with Name:{} and Rollno:{}'.format(self.name,self.rollno)

s1=Student('Durga',101)
s2=Student('Ravi',102)
print(s1)
print(s2)
```

### Output without Overriding str()

<**main**.Student object at 0x022144B0>  
<**main**.Student object at 0x022144D0>

### Output with Overriding str()

This is Student with Name: Durga and Rollno: 101  
This is Student with Name: Ravi and Rollno: 102

**Difference between str() and repr()**

**OR**

**Difference between **str**() and **repr**()**

- str() internally calls **str**() function and hence functionality of both is same.
- Similarly,repr() internally calls **repr**() function and hence functionality of both is same.
- str() returns a string containing a nicely printable representation object.
- The main purpose of str() is for readability.It may not possible to convert result string to original object.

```python
import datetime
today=datetime.datetime.now()
s=str(today)#converting datetime object to str
print(s)
d=eval(s)#converting str object to datetime
```

D:\durgaclasses>py test.py  
2018-05-18 22:48:19.890888  
Traceback (most recent call last):  
File "test.py", line 5, in <module>  
d=eval(s)#converting str object to datetime  
File "<string>", line 1  
2018-05-18 22:48:19.890888  
^  
SyntaxError: invalid token

But repr() returns a string containing a printable representation of object.  
The main goal of repr() is unambigouous. We can convert result string to original object by using eval() function,which may not possible in str() function.

```python
import datetime
today=datetime.datetime.now()
s=repr(today)#converting datetime object to str
print(s)
d=eval(s)#converting str object to datetime
print(d)
```

**Output:**

```
datetime.datetime(2018, 5, 18, 22, 51, 10, 875838)
2018-05-18 22:51:10.875838
```

**Note:** It is recommended to use repr() instead of str()

### Mini Project: Banking Application

```python
class Account:
    def __init__(self,name,balance,min_balance):
        self.name=name
        self.balance=balance
        self.min_balance=min_balance

    def deposit(self,amount):
        self.balance +=amount

    def withdraw(self,amount):
        if self.balance-amount >= self.min_balance:
            self.balance -=amount
        else:
            print("Sorry, Insufficient Funds")

    def printStatement(self):
        print("Account Balance:",self.balance)

class Current(Account):
    def __init__(self,name,balance):
        super().__init__(name,balance,min_balance=-1000)
    def __str__(self):
        return "{}'s Current Account with Balance :{}".format(self.name,self.balance)

class Savings(Account):
    def __init__(self,name,balance):
        super().__init__(name,balance,min_balance=0)
    def __str__(self):
        return "{}'s Savings Account with Balance :{}".format(self.name,self.balance)

c=Savings("Durga",10000)
print(c)
c.deposit(5000)
c.printStatement()
c.withdraw(16000)
c.withdraw(15000)
print(c)

c2=Current('Ravi',20000)
c2.deposit(6000)
print(c2)
c2.withdraw(27000)
print(c2)
```

**Output:**

```
D:\durgaclasses>py test.py
Durga's Savings Account with Balance :10000
Account Balance: 15000
Sorry, Insufficient Funds
Durga's Savings Account with Balance :0
Ravi's Current Account with Balance :26000
Ravi's Current Account with Balance :-1000
```
