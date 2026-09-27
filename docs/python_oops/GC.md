
## Garbage Collection

- In old languages like C++, programmer is responsible for both creation and destruction of objects.Usually programmer taking very much care while creating object, but nEglecting destruction of useless objects. Because of his nEglectance, total memory can be filled with useless objects which creates memory problems and total application will be down with Out of memory error.

- But in Python, We have some assistant which is always running in the background to destroy useless objects.Because this assistant the chance of failing Python program with memory problems is very less. This assistant is nothing but Garbage Collector.
- Hence the main objective of Garbage Collector is to destroy useless objects.

- If an object does not have any reference variable then that object eligible for Garbage Collection.

### How to enable and disable Garbage Collector in our

### Program:

By default Gargbage collector is enabled, but we can disable based on our requirement. In this context we can use the following functions of gc module.

```
gc.isenabled() → Returns True if GC enabled
gc.disable()→ To disable GC explicitly
gc.enable()→ To enable GC explicitly
```

```python
import gc
print(gc.isenabled())
gc.disable()
print(gc.isenabled())
gc.enable()
print(gc.isenabled())
```

**Output:**
```
True
False
True
```

### Destructors:

- Destructor is a special method and the name should be __del__
- Just before destroying an object Garbage Collector always calls destructor to perform clean up activities (Resource deallocation activities like close database connection etc).
- Once destructor execution completed then Garbage Collector automatically destroys that object.

**Note:** The job of destructor is not to destroy object and it is just to perform clean up activities.

```python
import time
class Test:
    def __init__(self):
        print("Object Initialization...")
    def __del__(self):
        print("Fulfilling Last Wish and performing clean up activities...")

t1=Test()
t1=None
time.sleep(5)
print("End of application")
```

**Output:**
```
Object Initialization...
Fulfilling Last Wish and performing clean up activities...
End of application
```

**Note:** If the object does not contain any reference variable then only it is eligible fo GC. ie if the reference count is zero then only object eligible for GC.

```python
import time
class Test:
    def __init__(self):
        print("Constructor Execution...")
    def __del__(self):
        print("Destructor Execution...")

t1=Test()
t2=t1
t3=t2
del t1
time.sleep(5)
print("object not yet destroyed after deleting t1")
del t2
time.sleep(5)
print("object not yet destroyed even after deleting t2")
print("I am trying to delete last reference variable...")
del t3
```

**Example:**

```python
import time
class Test:
    def __init__(self):
        print("Constructor Execution...")
    def __del__(self):
        print("Destructor Execution...")

list=[Test(),Test(),Test()]
del list
time.sleep(5)
print("End of application")
```

**Output:**
```
Constructor Execution...
Constructor Execution...
Constructor Execution...
Destructor Execution...
Destructor Execution...
Destructor Execution...
End of application
```

### How to find the Number of References of an Object:

sys module contains getrefcount() function for this purpose.  
sys.getrefcount (objectreference)

```python
import sys
class Test:
    pass
t1=Test()
t2=t1
t3=t1
t4=t1
print(sys.getrefcount(t1))
```

**Output 5**

**Note:** For every object, Python internally maintains one default reference variable self.