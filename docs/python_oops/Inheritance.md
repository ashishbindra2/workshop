
### Using Members of One Class inside Another Class:

We can use members of one class inside another class by using the following ways

1) By Composition (Has-A Relationship)
2) By Inheritance (IS-A Relationship)

### 1) By Composition (Has-A Relationship):

- By using Class Name or by creating object we can access members of one class inside another class is nothing but composition (Has-A Relationship).
- The main advantage of Has-A Relationship is Code Reusability.

**Demo Program-1:**

```python
class Engine:
    a=10
    def __init__(self):
        self.b=20
    def m1(self):
        print('Engine Specific Functionality')
class Car:
    def __init__(self):
        self.engine=Engine()
    def m2(self):
        print('Car using Engine Class Functionality')
        print(self.engine.a)
        print(self.engine.b)
        self.engine.m1()
c=Car()
c.m2()
```

**Output:**
```
Car using Engine Class Functionality
10
20
Engine Specific Functionality
```

**Demo Program-2:**

```python
class Car:
    def __init__(self,name,model,color):
        self.name=name
        self.model=model
        self.color=color
    def getinfo(self):
        print("Car Name:{} , Model:{} and Color:{}".format(self.name,self.model,self.color))

class Employee:
    def __init__(self,ename,eno,car):
        self.ename=ename
        self.eno=eno
        self.car=car
    def empinfo(self):
        print("Employee Name:",self.ename)
        print("Employee Number:",self.eno)
        print("Employee Car Info:")
        self.car.getinfo()
c=Car("Innova","2.5V","Grey")
e=Employee('Durga',10000,c)
e.empinfo()
```

**Output:**
```
Employee Name: Durga
Employee Number: 10000
Employee Car Info:
Car Name: Innova, Model: 2.5V and Color:Grey
```

In the above program Employee class Has-A Car reference and hence Employee class can access all members of Car class.

**Demo Program-3:**

```python
class X:
    a=10
    def __init__(self):
        self.b=20
    def m1(self):
            print("m1 method of X class")

class Y:
    c=30
    def __init__(self):
        self.d=40
    def m2(self):
        print("m2 method of Y class")

    def m3(self):
        x1=X()
        print(x1.a)
        print(x1.b)
        x1.m1()
        print(Y.c)
        print(self.d)
        self.m2()
        print("m3 method of Y class")
y1=Y()
y1.m3()
```

**Output:**
```
10
20
m1 method of X class
30
40
m2 method of Y class
m3 method of Y class
```

### 2) By Inheritance (IS-A Relationship):

What ever variables, methods and constructors available in the parent class by default available to the child classes and we are not required to rewrite. Hence the main advantage of inheritance is Code Reusability and we can extend existing functionality with some more extra functionality.

**Syntax: class childclass(parentclass)**

```python
class P:
    a=10
    def __init__(self):
        self.b=10
    def m1(self):
        print('Parent instance method')
    @classmethod
    def m2(cls):
        print('Parent class method')
    @staticmethod
    def m3():
        print('Parent static method')

class C(P):
    pass

c=C()
print(c.a)
print(c.b)
c.m1()
c.m2()
c.m3()
```

**Output:**
```
10
10
Parent instance method
Parent class method
Parent static method
```

```python
class P:
    10 methods
class C(P):
    5 methods
```

In the above example Parent class contains 10 methods and these methods automatically available to the child class and we are not required to rewrite those methods(Code Reusability)  
Hence child class contains 15 methods.

**Note:** What ever members present in Parent class are by default available to the child  
class through inheritance.

```python
class P:
    def m1(self):
        print("Parent class method")
class C(P):
    def m2(self):
        print("Child class method")

c=C();
c.m1()
c.m2()
```

**Output:**
```
Parent class method
Child class method
```

What ever methods present in Parent class are automatically available to the child class and hence on the child class reference we can call both parent class methods and child  
class methods.

Similarly variables also

```python
class P:
    a=10
    def __init__(self):
        self.b=20
class C(P):
    c=30
    def __init__(self):
        super().__init__()===>Line-1
        self.d=30

c1=C()
print(c1.a,c1.b,c1.c,c1.d)
```

If we comment Line-1 then variable b is not available to the child class.  
**Demo program for Inheritance:**

```python
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def eatndrink(self):
        print('Eat Biryani and Drink Beer')

class Employee(Person):
    def __init__(self,name,age,eno,esal):
        super().__init__(name,age)
        self.eno=eno
        self.esal=esal

    def work(self):
        print("Coding Python is very easy just like drinking Chilled Beer")
    def empinfo(self):
        print("Employee Name:",self.name)
        print("Employee Age:",self.age)
        print("Employee Number:",self.eno)
        print("Employee Salary:",self.esal)

e=Employee('Durga', 48, 100, 10000)
e.eatndrink()
e.work()
e.empinfo()
```

**Output:**
```
Eat Biryani and Drink Beer
Coding Python is very easy just like drinking Chilled Beer
Employee Name: Durga
Employee Age: 48
Employee Number: 100
Employee Salary: 10000
```

### IS-A vs HAS-A Relationship:

- If we want to extend existing functionality with some more extra functionality then we should go for IS-A Relationship.
- If we dont want to extend and just we have to use existing functionality then we should go for HAS-A Relationship.
- Eg: Employee class extends Person class Functionality But Employee class just uses Car functionality but not extending
```
   Person
     ^
     | IS - A
     |
  Employee ----HAS - A----> Car
```

```python
class Car:
    def __init__(self,name,model,color):
        self.name=name
        self.model=model
        self.color=color
    def getinfo(self):
        print("\tCar Name:{} \n\t Model:{} \n\t Color:{}".format(self.name,self.model, self.color))

class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def eatndrink(self):
        print('Eat Biryani and Drink Beer')

class Employee(Person):
    def __init__(self,name,age,eno,esal,car):
        super().__init__(name,age)
        self.eno=eno
        self.esal=esal
        self.car=car
    def work(self):
        print("Coding Python is very easy just like drinking Chilled Beer")
    def empinfo(self):
        print("Employee Name:",self.name)
        print("Employee Age:",self.age)
        print("Employee Number:",self.eno)
        print("Employee Salary:",self.esal)
        print("Employee Car Info:")
        self.car.getinfo()

c=Car("Innova","2.5V","Grey")
e=Employee('Durga',48,100,10000,c)
e.eatndrink()
e.work()
e.empinfo()
```

**Output:**
```
Eat Biryani and Drink Beer
Coding Python is very easy just like drinking Chilled Beer
Employee Name: Durga
Employee Age: 48
Employee Number: 100
Employee Salary: 10000
Employee Car Info:
    Car Name:Innova
    Model:2.5V
    Color:Grey
```

In the above example Employee class extends Person class functionality but just uses Car  
class functionality.

### Composition vs Aggregation:

### Composition:

Without existing container object if there is no chance of existing contained object then the container and contained objects are strongly associated and that strong association is nothing but Composition.

**Eg:** University contains several Departments and without existing university object there is no chance of existing Department object. Hence University and Department objects are strongly associated and this strong association is nothing but Composition.

```
 University Object (Container Object)
   ( (o) (o) (o) (o) (o) )  <-- Department Object (Contained Object)
```
### Aggregation:

Without existing container object if there is a chance of existing contained object then the container and contained objects are weakly associated and that weak association is nothing but Aggregation.

**Eg:** Department contains several Professors. Without existing Department still there may be a chance of existing Professor. Hence Department and Professor Objects are weakly associated, which is nothing but Aggregation.

```
 Department Object          Professor Object
 (Container Object)         (Contained Object)
   (  x ----------------->  ( )
      x ----------------->  ( )
      :                      :
      x ----------------->  ( )  )
```

**Coding Example:**

```python
class Student:
    collegeName='DURGASOFT'
    def __init__(self,name):
        self.name=name
print(Student.collegeName)
s=Student('Durga')
print(s.name)
```

**Output:**
```
Durga
```

In the above example without existing Student object there is no chance of existing his name. Hence Student Object and his name are strongly associated which is nothing but Composition.

But without existing Student object there may be a chance of existing collegeName. Hence Student object and collegeName are weakly associated which is nothing but Aggregation.
### Conclusion:

The relation between object and its instance variables is always Composition where as the relation between object and static variables is Aggregation.

**Note:** Whenever we are creating child class object then child class constructor will be executed. If the child class does not contain constructor then parent class constructor will be executed, but parent object won't be created.

```python
class P:
    def __init__(self):
        print(id(self))
class C(P):
    pass
c=C()
print(id(c))
```

**Output:**
```
6207088
6207088
```

```python
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
class Student(Person):
    def __init__(self,name,age,rollno,marks):
        super().__init__(name,age)
        self.rollno=rollno
        self.marks=marks
    def __str__(self):
        return 'Name={}\nAge={}\nRollno={}\nMarks={}'.format(self.name,self.age,self.rollno,self.marks)
s1=Student('durga',48,101,90)
print(s1)
```

**Output:**
```
Name=durga
Age=48
Rollno=101
Marks=90
```

**Note:** In the above example when ever we are creating child class object both parent and child class constructors got executed to perform initialization of child object.
### Types of Inheritance:

### 1) Single Inheritance:

The concept of inheriting the properties from one class to another class is known as single inheritance.

```python
class P:
    def m1(self):
        print("Parent Method")
class C(P):
    def m2(self):
        print("Child Method")
c=C()
c.m1()
c.m2()
```

**Output:**
```
Parent Method
Child Method
```

```
 P
 ^
 |      Single Inheritance
 C
```

### 2) Multi Level Inheritance:

The concept of inheriting the properties from multiple classes to single class with the concept of one after another is known as multilevel inheritance.

```python
class P:
    def m1(self):
        print("Parent Method")
class C(P):
    def m2(self):
        print("Child Method")
class CC(C):
    def m3(self):
        print("Sub Child Method")
c=CC()
c.m1()
c.m2()
c.m3()
```

**Output:**
```
Parent Method
Child Method
Sub Child Method
```

```
 P
 ^
 |
 C      Multi – Level Inheritance
 ^
 |
 CC
```

### 3) Hierarchical Inheritance:

The concept of inheriting properties from one class into multiple classes which are present at same level is known as Hierarchical Inheritance

```
     P
    ^ ^
   /   \       Hierarchical
  C1   C2      Inheritance
```

```python
class P:
    def m1(self):
        print("Parent Method")
class C1(P):
    def m2(self):
        print("Child1 Method")
class C2(P):
    def m3(self):
        print("Child2 Method")
c1=C1()
c1.m1()
c1.m2()
c2=C2()
c2.m1()
c2.m3()
```

**Output:**
```
Parent Method
Child1 Method
Parent Method
Child2 Method
```

### 4) Multiple Inheritance:

The concept of inheriting the properties from multiple classes into a single class at a time, is known as multiple inheritance.

```
 P1   P2
   ^ ^
    \/          Multiple
    C           Inheritance
```

```python
class P1:
    def m1(self):
        print("Parent1 Method")
class P2:
    def m2(self):
        print("Parent2 Method")
class C(P1,P2):
    def m3(self):
        print("Child2 Method")
c=C()
c.m1()
c.m2()
c.m3()
```

**Output:**
```
Parent1 Method
Parent2 Method
Child2 Method
```

If the same method is inherited from both parent classes, then Python will always consider the order of Parent classes in the declaration of the child class.

class C(P1, P2): → P1 method will be considered  
class C(P2, P1): → P2 method will be considered

```python
class P1:
    def m1(self):
        print("Parent1 Method")
class P2:
    def m1(self):
        print("Parent2 Method")
class C(P1,P2):
    def m2(self):
        print("Child Method")
c=C()
c.m1()
c.m2()
```

**Output:**
```
Parent1 Method
Child Method
```

### 5) Hybrid Inheritance:

Combination of Single, Multi level, multiple and Hierarchical inheritance is known as Hybrid Inheritance.

```
 A   B   C
  ^  ^  ^
   \ | /
     D
     ^
     |
     E
     ^
     |
     F
    / \
   v   v
  G     H
```

### 6) Cyclic Inheritance:

The concept of inheriting properties from one class to another class in cyclic way, is called Cyclic inheritance.Python won't support for Cyclic Inheritance of course it is really not required.  
**Eg - 1:** class A(A):pass  
NameError: name 'A' is not defined

```
  +--+
  v  |
  A--+
```

Eg - 2:

```python
class A(B):
    pass
class B(A):
    pass
```

NameError: name 'B' is not defined

```
  A
 ^ |
 | v
  B
```

### Method Resolution Order (MRO):

- In Hybrid Inheritance the method resolution order is decided based on MRO algorithm.
- This algorithm is also known as C3 algorithm.
- Samuele Pedroni proposed this algorithm.
- It follows DLR (Depth First Left to Right) i.e Child will get more priority than Parent.
- Left Parent will get more priority than Right Parent.
- MRO(X) = X+Merge(MRO(P1),MRO(P2),...,ParentList)

### Head Element vs Tail Terminology:

- Assume C1,C2,C3,...are classes.
- In the list: C1C2C3C4C5....
- C1 is considered as Head Element and remaining is considered as Tail.

### How to find Merge:

- Take the head of first list
- If the head is not in the tail part of any other list, then add this head to the result and remove it from the lists in the merge.
- If the head is present in the tail part of any other list, then consider the head element of the next list and continue the same process.

**Note:** We can find MRO of any class by using mro() function.  
print(ClassName.mro())
### Demo Program-1 for Method Resolution Order:

```
       A
      ^ ^
     /   \
    B     C
     ^   ^
      \ /
       D
```

mro(A) = A, object  
mro(B) = B, A, object  
mro(C) = C, A, object  
mro(D) = D, B, C, A, object

**test.py**

```python
class A:pass
class B(A):pass
class C(A):pass
class D(B,C):pass
print(A.mro())
print(B.mro())
print(C.mro())
print(D.mro())
```

**Output:**
```
[<class '__main__.A'>, <class 'object'>]
[<class '__main__.B'>, <class '__main__.A'>, <class 'object'>]
[<class '__main__.C'>, <class '__main__.A'>, <class 'object'>]
[<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>,
<class 'object'>]
```

### Demo Program-2 for Method Resolution Order:

```
              Object
            ^   ^   ^
           /    |    \
          A     B     C
          ^    ^ ^    ^ ^
           \  /   \  /  |
            X       Y   |
            ^       ^   |
             \     /    |
                P ------+

   (X -> A,B    Y -> B,C    P -> X,Y,C)
```

mro(A)=A,object  
mro(B)=B,object  
mro(C)=C,object  
mro(X)=X,A,B,object  
mro(Y)=Y,B,C,object  
mro(P)=P,X,A,Y,B,C,object

### Finding mro(P) by using C3 Algorithm:

**Formula:** MRO(X) = X+Merge(MRO(P1),MRO(P2),...,ParentList)  
mro(p) = P+Merge(mro(X),mro(Y),mro(C),XYC)  
= P+Merge(XABO,YBCO,CO,XYC)  
= P+X+Merge(ABO,YBCO,CO,YC)  
= P+X+A+Merge(BO,YBCO,CO,YC)  
= P+X+A+Y+Merge(BO,BCO,CO,C)  
= P+X+A+Y+B+Merge(O,CO,CO,C)  
= P+X+A+Y+B+C+Merge(O,O,O)  
= P+X+A+Y+B+C+O

**test.py**

```python
class A:pass
class B:pass
class C:pass
class X(A,B):pass
class Y(B,C):pass
class P(X,Y,C):pass
print(A.mro())#AO
print(X.mro())#XABO
print(Y.mro())#YBCO
print(P.mro())#PXAYBCO
```

**Output:**
```
[<class '__main__.A'>, <class 'object'>]
[<class '__main__.X'>, <class '__main__.A'>, <class '__main__.B'>, <class 'object'>]
[<class '__main__.Y'>, <class '__main__.B'>, <class '__main__.C'>, <class 'object'>]
[<class '__main__.P'>, <class '__main__.X'>, <class '__main__.A'>, <class '__main__.Y'>,
<class '__main__.B'>,
<class '__main__.C'>, <class 'object'>]
```

**test.py**

```python
class A:
    def m1(self):
        print('A class Method')
class B:
    def m1(self):
        print('B class Method')
class C:
    def m1(self):
        print('C class Method')
class X(A,B):
    def m1(self):
        print('X class Method')
class Y(B,C):
    def m1(self):
        print('Y class Method')
class P(X,Y,C):
    def m1(self):
        print('P class Method')
p=P()
p.m1()
```

**Output: P class Method**

In the above example P class m1() method will be considered.If P class does not contain m1() method then as per MRO, X class method will be considered. If X class does not contain then A class method will be considered and this process will be continued.

The method resolution in the following order: PXAYBCO
### Demo Program-3 for Method Resolution Order:

```
             Object
           ^   ^   ^
          /    |    \
         D     E     F
         ^ ^   ^     ^
         |  \  |     |
         |   \ |     |
         C    B      |
         ^\___^______|      (C -> D, F)
          \   |             (B -> D, E)
           \  |
             A              (A -> B, C)
```

mro(o) = object  
mro(D) = D,object  
mro(E) = E,object  
mro(F) = F,object  
mro(B) = B,D,E,object  
mro(C) = C,D,F,object  
mro(A) = A+Merge(mro(B),mro(C),BC)  
= A+Merge(BDEO,CDFO,BC)  
= A+B+Merge(DEO,CDFO,C)  
= A+B+C+Merge(DEO,DFO)  
= A+B+C+D+Merge(EO,FO)  
= A+B+C+D+E+Merge(O,FO)  
= A+B+C+D+E+F+Merge(O,O)  
= A+B+C+D+E+F+O

**test.py**

```python
class D:pass
class E:pass
class F:pass
class B(D,E):pass
class C(D,F):pass
class A(B,C):pass
print(D.mro())
print(B.mro())
print(C.mro())
print(A.mro())
```

**Output:**
```
[<class '__main__.D'>, <class 'object'>]
[<class '__main__.B'>, <class '__main__.D'>, <class '__main__.E'>, <class 'object'>]
[<class '__main__.C'>, <class '__main__.D'>, <class '__main__.F'>, <class 'object'>]
[<class '__main__.A'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.D'>,
<class '__main__.E'>,
<class '__main__.F'>, <class 'object'>]
```

### super() Method:

super() is a built-in method which is useful to call the super class constructors,variables and methods from the child class.

### Demo Program-1 for super():

```python
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        print('Name:',self.name)
        print('Age:',self.age)

class Student(Person):
    def __init__(self,name,age,rollno,marks):
        super().__init__(name,age)
        self.rollno=rollno
        self.marks=marks

    def display(self):
        super().display()
        print('Roll No:',self.rollno)
        print('Marks:',self.marks)

s1=Student('Durga',22,101,90)
s1.display()
```

**Output:**
```
Name: Durga
Age: 22
Roll No: 101
Marks: 90
```

In the above program we are using super() method to call parent class constructor and display() method

### Demo Program-2 for super():

```python
class P:
    a=10
    def __init__(self):
        self.b=10
    def m1(self):
        print('Parent instance method')
    @classmethod
    def m2(cls):
        print('Parent class method')
    @staticmethod
    def m3():
        print('Parent static method')

class C(P):
    a=888
    def __init__(self):
        self.b=999
        super().__init__()
        print(super().a)
        super().m1()
        super().m2()
        super().m3()

c=C()
```

**Output:**
```
10
Parent instance method
Parent class method
Parent static method
```

In the above example we are using super() to call various members of Parent class.
### How to Call Method of a Particular Super Class:

We can use the following approaches

**1) super(D, self).m1()**

It will call m1() method of super class of D.

**2) A.m1(self)**

It will call A class m1() method

```python
class A:
    def m1(self):
        print('A class Method')
class B(A):
    def m1(self):
        print('B class Method')
class C(B):
    def m1(self):
        print('C class Method')
class D(C):
    def m1(self):
        print('D class Method')
class E(D):
    def m1(self):
        A.m1(self)

e=E()
e.m1()
```

**Output: A class Method**

### Various Important Points about super():

**Case-1:** From child class we are not allowed to access parent class instance variables by using super(), Compulsory we should use self only.  
But we can access parent class static variables by using super().

```python
class P:
    a=10
    def __init__(self):
        self.b=20

class C(P):
    def m1(self):
        print(super().a)#valid
        print(self.b)#valid
        print(super().b)#invalid
c=C()
c.m1()
```

**Output:**
```
10
20
AttributeError: 'super' object has no attribute 'b'
```

**Case-2:** From child class constructor and instance method, we can access parent class instance method, static method and class method by using super()

```python
class P:
    def __init__(self):
        print('Parent Constructor')
    def m1(self):
        print('Parent instance method')
    @classmethod
    def m2(cls):
        print('Parent class method')
    @staticmethod
    def m3():
        print('Parent static method')

class C(P):
    def __init__(self):
        super().__init__()
        super().m1()
        super().m2()
        super().m3()

    def m1(self):
        super().__init__()
        super().m1()
        super().m2()
        super().m3()

c=C()
c.m1()
```

**Output:**
```
Parent Constructor
Parent instance method
Parent class method
Parent static method
Parent Constructor
Parent instance method
Parent class method
Parent static method
```

**Case-3:** From child class, class method we cannot access parent class instance methods and constructors by using super() directly(but indirectly possible). But we can access parent class static and class methods.

```python
class P:
    def __init__(self):
        print('Parent Constructor')
    def m1(self):
        print('Parent instance method')
    @classmethod
    def m2(cls):
        print('Parent class method')
    @staticmethod
    def m3():
        print('Parent static method')

class C(P):
    @classmethod
    def m1(cls):
        #super().__init__()--->invalid
        #super().m1()--->invalid
        super().m2()
        super().m3()

C.m1()
```

**Output:**
```
Parent class method
Parent static method
```

**From Class Method of Child Class, how to call Parent Class Instance Methods**

**and Constructors:**

```python
class A:
    def __init__(self):
        print('Parent constructor')

    def m1(self):
        print('Parent instance method')

class B(A):
    @classmethod
    def m2(cls):
        super(B,cls).__init__(cls)
        super(B,cls).m1(cls)

B.m2()
```

**Output:**
```
Parent constructor
Parent instance method
```

**Case-4:** In child class static method we are not allowed to use super() generally (But in special way we can use)

```python
class P:
    def __init__(self):
        print('Parent Constructor')
    def m1(self):
        print('Parent instance method')
    @classmethod
    def m2(cls):
        print('Parent class method')
    @staticmethod
    def m3():
        print('Parent static method')

class C(P):
    @staticmethod
    def m1():
        super().m1()-->invalid
        super().m2()--->invalid
        super().m3()--->invalid

C.m1()
```

RuntimeError: super(): no arguments

### How to Call Parent Class Static Method from Child Class Static

### Method by using super():

```python
class A:

    @staticmethod
    def m1():
        print('Parent static method')

class B(A):
    @staticmethod
    def m2():
        super(B,B).m1()

B.m2()
```

**Output: Parent static method**


