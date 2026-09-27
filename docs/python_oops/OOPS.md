### What is Class

- In Python every thing is an object. To create objects we required some Model or Plan or Blue print, which is nothing but class.
- We can write a class to represent properties (attributes) and actions (behaviour) of object.

- Properties can be represented by variables
- Actions can be represented by Methods.

- Hence class contains both variables and methods.

### How to define a Class?

We can define a class by using class keyword.

**Syntax:**

```
class className:
    ''' documenttation string '''
    variables:instance variables,static and local variables
    methods: instance methods,static methods,class methods
```

Documentation string represents description of the class. Within the class doc string is always optional. We can get doc string by using the following 2 ways.

```python
print(classname.__doc__)
help(classname)
```

**Example:**

```python
class Student:
    ''''' This is student class with required data'''
print(Student.__doc__)
help(Student)
```

Within the Python class we can represent data by using variables.

There are 3 types of variables are allowed.

1) Instance Variables (Object Level Variables)
2) Static Variables (Class Level Variables)
3) Local variables (Method Level Variables)  
Within the Python class, we can represent operations by using methods. The following are various types of allowed methods

4) Instance Methods
5) Class Methods
6) Static Methods

**Example for Class:**

```python
class Student:
    '''''Developed by durga for python demo'''
    def __init__(self):
        self.name='durga'
        self.age=40
        self.marks=80

    def talk(self):
        print("Hello I am :",self.name)
        print("My Age is:",self.age)
        print("My Marks are:",self.marks)
```

### What is Object

Pysical existence of a class is nothing but object. We can create any number of objects for a class.

**Syntax to Create Object:** referencevariable = classname()

**Example: s = Student()**

### What is Reference Variable?

The variable which can be used to refer object is called reference variable.  
By using reference variable, we can access properties and methods of object.

**Program:** Write a Python program to create a Student class and Creates an object to it. Call the method talk() to display student details

```python
class Student:

    def __init__(self,name,rollno,marks):
        self.name=name
        self.rollno=rollno
        self.marks=marks

    def talk(self):
        print("Hello My Name is:",self.name)
        print("My Rollno is:",self.rollno)
        print("My Marks are:",self.marks)

s1=Student("Durga",101,80)
s1.talk()
```

**Output:**

```
D:\durgaclasses>py test.py
Hello My Name is: Durga
My Rollno is: 101
My Marks are: 80
```

### Self Variable

- self is the default variable which is always pointing to current object (like this keyword in Java)
- By using self we can access instance variables and instance methods of object.

**Note:**

1) self should be first parameter inside constructor  
def **init**(self):

2) self should be first parameter inside instance methods  
def talk(self):

### Constructor Concept

- Constructor is a special method in python.
- The name of the constructor should be **init**(self)
- Constructor will be executed automatically at the time of object creation.
- The main purpose of constructor is to declare and initialize instance variables.
- Per object constructor will be exeucted only once.
- Constructor can take atleast one argument(atleast self)
- Constructor is optional and if we are not providing any constructor then python will provide default constructor.

**Example:**

```python
def __init__(self,name,rollno,marks):
        self.name=name
        self.rollno=rollno
        self.marks=marks
```

**Program to demonistrate Constructor will execute only once per Object:**

```python
class Test:

    def __init__(self):
        print("Constructor exeuction...")

    def m1(self):
        print("Method execution...")

t1=Test()
t2=Test()
t3=Test()
t1.m1()
```

**Output:**

```
Constructor exeuction...
Constructor exeuction...
Constructor exeuction...
Method execution...
```

**Program:**

```python
class Student:

    ''''' This is student class with required data'''
    def __init__(self,x,y,z):
        self.name=x
        self.rollno=y
        self.marks=z

    def display(self):
        print("Student Name:{}\nRollno:{} \nMarks:{}".format(self.name,self.rollno,self.marks))

s1=Student("Durga",101,80)
s1.display()
s2=Student("Sunny",102,100)
s2.display()
```

**Output:**

```
Student Name:Durga
Rollno:101
Marks:80
Student Name:Sunny
Rollno:102
Marks:100
```

### Differences between Methods and Constructors

| Method | Constructor |
| --- | --- |
| 1) Name of method can be any name | 1) Constructor name should be always `__init__` |
| 2) Method will be executed if we call that method | 2) Constructor will be executed automatically at the time of object creation. |
| 3) Per object, method can be called any number of times. | 3) Per object, Constructor will be executed only once |
| 4) Inside method we can write business logic | 4) Inside Constructor we have to declare and initialize instance variables |

### Types of Variables

Inside Python class 3 types of variables are allowed.

1) Instance Variables (Object Level Variables)
2) Static Variables (Class Level Variables)
3) Local variables (Method Level Variables)

### 1) Instance Variables

- If the value of a variable is varied from object to object, then such type of variables are called instance variables.
- For every object a separate copy of instance variables will be created.

### Where we can declare Instance Variables

1) Inside Constructor by using self variable
2) Inside Instance Method by using self variable
3) Outside of the class by using object reference variable

### 1) Inside Constructor by using Self Variable

We can declare instance variables inside a constructor by using self keyword. Once we creates object, automatically these variables will be added to the object.

```python
class Employee:

    def __init__(self):
        self.eno=100
        self.ename='Durga'
        self.esal=10000

e=Employee()
print(e.__dict__)
```

Output: {'eno': 100, 'ename': 'Durga', 'esal': 10000}

### 2) Inside Instance Method by using Self Variable

We can also declare instance variables inside instance method by using self variable. If any instance variable declared inside instance method, that instance variable will be added once we call taht method.

```python
class Test:

    def __init__(self):
        self.a=10
        self.b=20

    def m1(self):
        self.c=30

t=Test()
t.m1()
print(t.__dict__)
```

Output: {'a': 10, 'b': 20, 'c': 30}

### 3) Outside of the Class by using Object Reference Variable

We can also add instance variables outside of a class to a particular object.

```python
class Test:

    def __init__(self):
        self.a=10
        self.b=20
    def m1(self):
        self.c=30

t=Test()
t.m1()
t.d=40
print(t.__dict__)
```

Output {'a': 10, 'b': 20, 'c': 30, 'd': 40}

### How to Access Instance Variables

We can access instance variables with in the class by using self variable and outside of the  
class by using object reference.

```python
class Test:

    def __init__(self):
        self.a=10
        self.b=20
    def display(self):
        print(self.a)
        print(self.b)

t=Test()
t.display()
print(t.a,t.b)
```

**Output:**

```
10
20
10 20
```

### How to delete Instance Variable from the Object

1) Within a class we can delete instance variable as follows  
del self.variableName

2) From outside of class we can delete instance variables as follows  
del objectreference.variableName

```python
class Test:
    def __init__(self):
        self.a=10
        self.b=20
        self.c=30
        self.d=40
    def m1(self):
        del self.d

t=Test()
print(t.__dict__)
t.m1()
print(t.__dict__)
del t.c
print(t.__dict__)
```

**Output:**

```
{'a': 10, 'b': 20, 'c': 30, 'd': 40}
{'a': 10, 'b': 20, 'c': 30}
{'a': 10, 'b': 20}
```

**Note:** The instance variables which are deleted from one object,will not be deleted from other objects.

```python
class Test:
    def __init__(self):
        self.a=10
        self.b=20
        self.c=30
        self.d=40

t1=Test()
t2=Test()
del t1.a
print(t1.__dict__)
print(t2.__dict__)
```

**Output:**

```
{'b': 20, 'c': 30, 'd': 40}
{'a': 10, 'b': 20, 'c': 30, 'd': 40}
```

If we change the values of instance variables of one object then those changes won't be reflected to the remaining objects, because for every object we are separate copy of instance variables are available.

```python
class Test:
    def __init__(self):
        self.a=10
        self.b=20

t1=Test()
t1.a=888
t1.b=999
t2=Test()
print('t1:',t1.a,t1.b)
print('t2:',t2.a,t2.b)
```

**Output:**

```
t1: 888 999
t2: 10 20
```

### 2) Static Variables

- If the value of a variable is not varied from object to object, such type of variables we have to declare with in the class directly but outside of methods. Such types of variables are called Static variables.
- For total class only one copy of static variable will be created and shared by all objects of that class.
- We can access static variables either by class name or by object reference. But recommended to use class name.

### Instance Variable vs Static Variable

**Note:** In the case of instance variables for every object a seperate copy will be created,but in the case of static variables for total class only one copy will be created and shared by every object of that class.

```python
class Test:
    x=10
    def __init__(self):
        self.y=20

t1=Test()
t2=Test()
print('t1:',t1.x,t1.y)
print('t2:',t2.x,t2.y)
Test.x=888
t1.y=999
print('t1:',t1.x,t1.y)
print('t2:',t2.x,t2.y)
```

**Output:**

```
t1: 10 20
t2: 10 20
t1: 888 999
t2: 888 20
```

### Various Places to declare Static Variables

1) In general we can declare within the class directly but from out side of any method
2) Inside constructor by using class name
3) Inside instance method by using class name
4) Inside classmethod by using either class name or cls variable
5) Inside static method by using class name

```python
class Test:
    a=10
    def __init__(self):
        Test.b=20
    def m1(self):
        Test.c=30
    @classmethod
    def m2(cls):
        cls.d1=40
        Test.d2=400
    @staticmethod
    def m3():
        Test.e=50
print(Test.__dict__)
t=Test()
print(Test.__dict__)
t.m1()
print(Test.__dict__)
Test.m2()
print(Test.__dict__)
Test.m3()
print(Test.__dict__)
Test.f=60
print(Test.__dict__)
```

### How to access Static Variables

1) inside constructor: by using either self or classname
2) inside instance method: by using either self or classname
3) inside class method: by using either cls variable or classname
4) inside static method: by using classname
5) From outside of class: by using either object reference or classname

```python
class Test:
    a=10
    def __init__(self):
        print(self.a)
        print(Test.a)
    def m1(self):
        print(self.a)
        print(Test.a)
    @classmethod
    def m2(cls):
        print(cls.a)
        print(Test.a)
    @staticmethod
    def m3():
        print(Test.a)
t=Test()
print(Test.a)
print(t.a)
t.m1()
t.m2()
t.m3()
```

### Where we can modify the Value of Static Variable

Anywhere either with in the class or outside of class we can modify by using classname. But inside class method, by using cls variable.

```python
class Test:
    a=777
    @classmethod
    def m1(cls):
        cls.a=888
    @staticmethod
    def m2():
        Test.a=999
print(Test.a)
Test.m1()
print(Test.a)
Test.m2()
print(Test.a)
```

**Output:**

```
777
888
999
*****
```

### If we change the Value of Static Variable by using either self OR

### Object Reference Variable

If we change the value of static variable by using either self or object reference variable, then the value of static variable won't be changed, just a new instance variable with that name will be added to that particular object.

```python
class Test:
    a=10
    def m1(self):
        self.a=888
t1=Test()
t1.m1()
print(Test.a)
print(t1.a)
```

**Output:**

```
10
888
```

```python
class Test:
    x=10
    def __init__(self):
        self.y=20

t1=Test()
t2=Test()
print('t1:',t1.x,t1.y)
print('t2:',t2.x,t2.y)
t1.x=888
t1.y=999
print('t1:',t1.x,t1.y)
print('t2:',t2.x,t2.y)
```

**Output:**

```
t1: 10 20
t2: 10 20
t1: 888 999
t2: 10 20
```

```python
class Test:
    a=10
    def __init__(self):
        self.b=20
t1=Test()
t2=Test()
Test.a=888
t1.b=999
print(t1.a,t1.b)
print(t2.a,t2.b)
```

**Output:**

```
888 999
888 20
```

```python
class Test:
    a=10
    def __init__(self):
        self.b=20
    def m1(self):
        self.a=888
        self.b=999

t1=Test()
t2=Test()
t1.m1()
print(t1.a,t1.b)
print(t2.a,t2.b)
```

**Output:**

```
888 999
10 20
```

```python
class Test:
    a=10
    def __init__(self):
        self.b=20
    @classmethod
    def m1(cls):
        cls.a=888
        cls.b=999

t1=Test()
t2=Test()
t1.m1()
print(t1.a,t1.b)
print(t2.a,t2.b)
print(Test.a,Test.b)
```

**Output:**

```
888 20
888 20
888 999
```

### How to Delete Static Variables of a Class

1) We can delete static variables from anywhere by using the following syntax del classname.variablename

2) But inside classmethod we can also use cls variable  
del cls.variablename

```python
class Test:
    a=10
    @classmethod
    def m1(cls):
        del cls.a
Test.m1()
print(Test.__dict__)
```

**Example:**

```python
class Test:
    a=10
    def __init__(self):
        Test.b=20
        del Test.a
    def m1(self):
        Test.c=30
        del Test.b
    @classmethod
    def m2(cls):
        cls.d=40
        del Test.c
    @staticmethod
    def m3():
        Test.e=50
        del Test.d
print(Test.__dict__)
t=Test()
print(Test.__dict__)
t.m1()
print(Test.__dict__)
Test.m2()
print(Test.__dict__)
Test.m3()
print(Test.__dict__)
Test.f=60
print(Test.__dict__)
del Test.e
print(Test.__dict__)
```

******Note:**

- By using object reference variable/self we can read static variables, but we cannot modify or delete.
- If we are trying to modify, then a new instance variable will be added to that particular object.
- t1.a = 70
- If we are trying to delete then we will get error.

**Example:**

```python
class Test:
    a=10

t1=Test()
del t1.a ===>AttributeError: a
```

We can modify or delete static variables only by using classname or cls variable.

```python
import sys
class Customer:
    ''''' Customer class with bank operations.. '''
    bankname='DURGABANK'
    def __init__(self,name,balance=0.0):
        self.name=name
        self.balance=balance
    def deposit(self,amt):
        self.balance=self.balance+amt
        print('Balance after deposit:',self.balance)
    def withdraw(self,amt):
        if amt>self.balance:
            print('Insufficient Funds..cannot perform this operation')
            sys.exit()
        self.balance=self.balance-amt
        print('Balance after withdraw:',self.balance)

print('Welcome to',Customer.bankname)
name=input('Enter Your Name:')
c=Customer(name)
while True:
    print('d-Deposit \nw-Withdraw \ne-exit')
    option=input('Choose your option:')
    if option=='d' or option=='D':
        amt=float(input('Enter amount:'))
        c.deposit(amt)
    elif option=='w' or option=='W':
        amt=float(input('Enter amount:'))
        c.withdraw(amt)
    elif option=='e' or option=='E':
        print('Thanks for Banking')
        sys.exit()
    else:
        print('Invalid option..Plz choose valid option')
```

**Output:**

```
D:\durga_classes>py test.py
Welcome to DURGABANK
Enter Your Name:Durga
d-Deposit
w-Withdraw
e-exit
```

Choose your option:d  
Enter amount:10000  
Balance after deposit: 10000.0  
d-Deposit  
w-Withdraw  
e-exit

Choose your option:d  
Enter amount:20000  
Balance after deposit: 30000.0  
d-Deposit  
w-Withdraw  
e-exit

Choose your option:w  
Enter amount:2000  
Balance after withdraw: 28000.0  
d-Deposit  
w-Withdraw  
e-exit

Choose your option:r  
Invalid option..Plz choose valid option  
d-Deposit  
w-Withdraw  
e-exit

Choose your option:e  
Thanks for Banking

### 3) Local Variables

- Sometimes to meet temporary requirements of programmer,we can declare variables inside a method directly,such type of variables are called local variable or temporary variables.
- Local variables will be created at the time of method execution and destroyed once method completes.
- Local variables of a method cannot be accessed from outside of method.

```python
class Test:
    def m1(self):
        a=1000
        print(a)
    def m2(self):
        b=2000
        print(b)
t=Test()
t.m1()
t.m2()
```

**Output:**

```
1000
2000
```

```python
class Test:
    def m1(self):
        a=1000
        print(a)
    def m2(self):
        b=2000
        print(a) #NameError: name 'a' is not defined
        print(b)
t=Test()
t.m1()
t.m2()
```

### Types of Methods

Inside Python class 3 types of methods are allowed

1) Instance Methods
2) Class Methods
3) Static Methods

### 1) Instance Methods

- Inside method implementation if we are using instance variables then such type of methods are called instance methods.
- Inside instance method declaration, we have to pass self variable. def m1(self):
- By using self variable inside method we can able to access instance variables.
- Within the class we can call instance method by using self variable and from outside of the class we can call by using object reference.

```python
class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def display(self):
        print('Hi',self.name)
        print('Your Marks are:',self.marks)
    def grade(self):
        if self.marks>=60:
            print('You got First Grade')
        elif self.marks>=50:
            print('Yout got Second Grade')
        elif self.marks>=35:
            print('You got Third Grade')
        else:
            print('You are Failed')
n=int(input('Enter number of students:'))
for i in range(n):
    name=input('Enter Name:')
    marks=int(input('Enter Marks:'))
    s= Student(name,marks)
    s.display()
    s.grade()
    print()
```

Ouput:  
D:\durga_classes>py test.py  
Enter number of students:2  
Enter Name:Durga  
Enter Marks:90  
Hi Durga  
Your Marks are: 90  
You got First Grade

Enter Name:Ravi  
Enter Marks:12  
Hi Ravi  
Your Marks are: 12  
You are Failed

### Setter and Getter Methods

We can set and get the values of instance variables by using getter and setter methods.

### Setter Method

setter methods can be used to set values to the instance variables. setter methods also known as mutator methods.

Syntax:  
def setVariable(self,variable):  
self.variable=variable

Example:  
def setName(self,name):  
self.name=name

### Getter Method

Getter methods can be used to get values of the instance variables. Getter methods also known as accessor methods.

Syntax:  
def getVariable(self):  
return self.variable

Example:  
def getName(self):  
return self.name

```python
class Student:
    def setName(self,name):
        self.name=name

    def getName(self):
        return self.name

    def setMarks(self,marks):
        self.marks=marks

    def getMarks(self):
        return self.marks

n=int(input('Enter number of students:'))
for i in range(n):
    s=Student()
    name=input('Enter Name:')
    s.setName(name)
    marks=int(input('Enter Marks:'))
    s.setMarks(marks)

    print('Hi',s.getName())
    print('Your Marks are:',s.getMarks())
    print()
```

**Output:**

```
D:\python_classes>py test.py
Enter number of students:2
```

Enter Name:Durga  
Enter Marks:100  
Hi Durga  
Your Marks are: 100

Enter Name:Ravi  
Enter Marks:80  
Hi Ravi  
Your Marks are: 80

### 2) Class Methods

- Inside method implementation if we are using only class variables (static variables), then such type of methods we should declare as class method.
- We can declare class method explicitly by using @classmethod decorator.
- For class method we should provide cls variable at the time of declaration
- We can call classmethod by using classname or object reference variable.

```python
class Animal:
    lEgs=4
    @classmethod
    def walk(cls,name):
        print('{} walks with {} lEgs...'.format(name,cls.lEgs))
Animal.walk('Dog')
Animal.walk('Cat')
```

**Output:**

```
D:\python_classes>py test.py
Dog walks with 4 lEgs...
Cat walks with 4 lEgs...
```

### Program to track the Number of Objects created for a Class

```python
class Test:
    count=0
    def __init__(self):
        Test.count =Test.count+1
    @classmethod
    def noOfObjects(cls):
        print('The number of objects created for test class:',cls.count)

t1=Test()
t2=Test()
Test.noOfObjects()
t3=Test()
t4=Test()
t5=Test()
Test.noOfObjects()
```

### 3) Static Methods

- In general these methods are general utility methods.
- Inside these methods we won't use any instance or class variables.
- Here we won't provide self or cls arguments at the time of declaration.
- We can declare static method explicitly by using @staticmethod decorator
- We can access static methods by using classname or object reference

```python
class DurgaMath:

    @staticmethod
    def add(x,y):
        print('The Sum:',x+y)

    @staticmethod
    def product(x,y):
        print('The Product:',x*y)

    @staticmethod
    def average(x,y):
        print('The average:',(x+y)/2)

DurgaMath.add(10,20)
DurgaMath.product(10,20)
DurgaMath.average(10,20)
```

**Output:**

```
The Sum: 30
The Product: 200
The average: 15.0
```

Note:

- In general we can use only instance and static methods.Inside static method we can access class level variables by using class name.
- Class methods are most rarely used methods in python.

### Passing Members of One Class to Another Class

We can access members of one class inside another class.

```python
class Employee:
    def __init__(self,eno,ename,esal):
        self.eno=eno
        self.ename=ename
        self.esal=esal
    def display(self):
        print('Employee Number:',self.eno)
        print('Employee Name:',self.ename)
        print('Employee Salary:',self.esal)
class Test:
    def modify(emp):
        emp.esal=emp.esal+10000
        emp.display()
e=Employee(100,'Durga',10000)
Test.modify(e)
```

**Output:**

```
D:\python_classes>py test.py
Employee Number: 100
Employee Name: Durga
Employee Salary: 20000
```

In the above application, Employee class members are available to Test class.

## Inner Classes

Sometimes we can declare a class inside another class, such type of classes are called inner classes.

Without existing one type of object if there is no chance of existing another type of object, then we should go for inner classes.

**Example:** Without existing Car object there is no chance of existing Engine object. Hence Engine class should be part of Car class.

class Car:  
.....  
class Engine:  
......

**Example:** Without existing university object there is no chance of existing Department object

class University:  
.....  
class Department:  
......

**Example:** Without existing Human there is no chance of existin Head. Hence Head should be part of Human.

class Human:  
class Head:

**Note:** Without existing outer class object there is no chance of existing inner class object. Hence inner class object is always associated with outer class object.  
**Demo Program-1:**

```python
class Outer:
    def __init__(self):
        print("outer class object creation")
    class Inner:
        def __init__(self):
            print("inner class object creation")
        def m1(self):
            print("inner class method")
o=Outer()
i=o.Inner()
i.m1()
```

**Output:**

```
outer class object creation
inner class object creation
inner class method
```

**Note:** The following are various possible syntaxes for calling inner class method

```python
o = Outer()
```

i = o.Inner()  
i.m1()

1) i = Outer().Inner()  
i.m1()

2) Outer().Inner().m1()

**Demo Program-2:**

```python
class Person:
    def __init__(self):
        self.name='durga'
        self.db=self.Dob()
    def display(self):
        print('Name:',self.name)
    class Dob:
        def __init__(self):
            self.dd=10
            self.mm=5
            self.yy=1947
        def display(self):
            print('Dob={}/{}/{}'.format(self.dd,self.mm,self.yy))
p=Person()
p.display()
x=p.db
x.display()
```

**Output:**

```
Name: durga
Dob=10/5/1947
```

**Demo Program-3:**

Inside a class we can declare any number of inner classes.

```python
class Human:

    def __init__(self):
        self.name = 'Sunny'
        self.head = self.Head()
        self.brain = self.Brain()
    def display(self):
        print("Hello..",self.name)

    class Head:
        def talk(self):
            print('Talking...')

    class Brain:
        def think(self):
            print('Thinking...')

h=Human()
h.display()
h.head.talk()
h.brain.think()
```

**Output:**

```
Hello.. Sunny
Talking...
Thinking...
```
