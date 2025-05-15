# Set
## Set Data Structure
- If we want to represent a group of unique values as a single entity then we should go
for set.
- Duplicates are not allowed.
- Insertion order is not preserved.But we can sort the elements.
- Indexing and slicing not allowed for the set.
- Heterogeneous elements are allowed.
- Set objects are mutable i.e once we creates set object we can perform any changes in
that object based on our requirement.
- We can represent set elements within curly braces and with comma seperation
- We can apply mathematical operations like union,intersection,difference etc on set
objects.

### Creation of Set objects:
```py
s={10,20,30,40}
print(s)
print(type(s))

# Output
# {40, 10, 20, 30}
# <class 'set'>
```

We can create set objects by using set() function
s=set(any sequence)

```py
# Eg 1:
1. l = [10,20,30,40,10,20,10]
2. s=set(l)
3. print(s) # {40, 10, 20, 30}

# Eg 2:
1. s=set(range(5))
2. print(s) #{0, 1, 2, 3, 4}
```

**Note:** While creating empty set we have to take special care.
Compulsory we should use set() function.

s={} ==>It is treated as dictionary but not empty set.

```py
# Eg:
s={}
print(s)
print(type(s))

# Output
# {}
# <class 'dict'>

# Eg:
 s=set()
 print(s)
 print(type(s))

#  Output
#  set()
#  <class 'set'>
```

### Important functions of set:
1. add(x):
Adds item x to the set

```py
# Eg:
1. s={10,20,30}
2. s.add(40);
3. print(s) #{40, 10, 20, 30}
2. update(x,y,z):
```

To add multiple items to the set.
Arguments are not individual elements and these are Iterable objects like List,range etc.
All elements present in the given Iterable objects will be added to the set.

```py
# Eg:
1. s={10,20,30}
2. l=[40,50,60,10]
3. s.update(l,range(5))
4. print(s)

# Output
7. {0, 1, 2, 3, 4, 40, 10, 50, 20, 60, 30}
```
### Q. What is the difference between add() and update() functions in set?
We can use add() to add individual item to the Set,where as we can use update() function
to add multiple items to Set.
add() function can take only one argument where as update() function can take any
number of arguments but all arguments should be iterable objects.

### Q. Which of the following are valid for set s?
1. s.add(10)
2. s.add(10,20,30) TypeError: add() takes exactly one argument (3 given)
3. s.update(10) TypeError: 'int' object is not iterable
4. s.update(range(1,10,2),range(0,10,2))
3. copy():

Returns copy of the set.
It is cloned object.
```py
s={10,20,30}
s1=s.copy()
print(s1)
```

4. pop():
It removes and returns some random element from the set.

```py
s={40,10,30,20}
 print(s)
 print(s.pop())
 print(s)

#  Output
#  {40, 10, 20, 30}
#  40
#  {10, 20, 30}

```

5. remove(x):
It removes specified element from the set.
If the specified element not present in the Set then we will get KeyError
```py
s={40,10,30,20}
s.remove(30)
print(s) # {40, 10, 20}
s.remove(50) ==>KeyError: 50
```

6. discard(x):
It removes the specified element from the set.
If the specified element not present in the set then we won't get any error.
```py
s={10,20,30}
s.discard(10)
print(s) ===>{20, 30}
s.discard(50)
print(s) ==>{20, 30}
```
Q. What is the difference between remove() and discard() functions in Set?
Q. Explain differences between pop(),remove() and discard() functionsin Set?


---

### 🔹 Q1: What is the difference between `remove()` and `discard()` functions in a `set`?

| Feature        | `remove()`                             | `discard()`                               |
| -------------- | -------------------------------------- | ----------------------------------------- |
| Purpose        | Removes a specific element             | Also removes a specific element           |
| Error Handling | Raises `KeyError` if element not found | Does **not** raise an error               |
| Use Case       | Use when you are sure element exists   | Use when element **may or may not** exist |

#### ✅ Example:

```python
s = {1, 2, 3}

s.remove(2)     # Works fine
s.discard(3)    # Works fine
s.remove(4)     # ❌ Raises KeyError
s.discard(4)    # ✅ Does nothing
```

---

### 🔹 Q2: Explain differences between `pop()`, `remove()`, and `discard()` in a `set`

| Function     | Behavior                                     | Removes...       | Raises Error if Not Found | Return Value        |
| ------------ | -------------------------------------------- | ---------------- | ------------------------- | ------------------- |
| `pop()`      | Removes and returns **an arbitrary** element | Random element   | ❌ Only if set is empty    | ✔️ The removed item |
| `remove(x)`  | Removes element `x`                          | Specific element | ✔️ Yes (`KeyError`)       | ❌ Returns `None`    |
| `discard(x)` | Removes element `x`                          | Specific element | ❌ No error if not found   | ❌ Returns `None`    |

#### ✅ Example:

```python
s = {10, 20, 30}

print(s.pop())     # Removes and prints a random element

s.remove(20)       # Removes 20
s.discard(40)      # Does nothing, no error

s.remove(40)       # ❌ Raises KeyError
```

---

### ✅ Summary:

* Use **`remove()`** if you're sure the item exists.
* Use **`discard()`** if the item may not be in the set.
* Use **`pop()`** to remove and get a random item (often used when order doesn't matter).

7.clear():
To remove all elements from the Set.
```py
 s={10,20,30}
 print(s) #  {10, 20, 30}

 s.clear()
 print(s) #  set()
```

### Mathematical operations on the Set:
1. union():

    x.union(y) ==>We can use this function to return all elements present in both sets
    x.union(y) or x|y

    Eg:

```py
x={10,20,30,40}
y={30,40,50,60}

print(x.union(y)) #{10, 20, 30, 40, 50, 60}
print(x|y) #{10, 20, 30, 40, 50, 60}
```

2. intersection():

x.intersection(y) or x&y
Returns common elements present in both x and y

Eg:
```py
x={10,20,30,40}
y={30,40,50,60}

print(x.intersection(y)) #{40, 30}
print(x&y) #{40, 30}
```

3. difference():

    `x.difference(y) or x-y`

    returns the elements present in x but not in y
    
    Eg:
    ```py
    x={10,20,30,40}
    y={30,40,50,60}
    print(x.difference(y)) #{10, 20}
    print(x-y) #{10, 20}
    print(y-x) #{50, 60}
    ```
4. symmetric_difference():

`x.symmetric_difference(y) or x^y`

Returns elements present in either x or y but not in both
Eg:
```py
x={10,20,30,40}
y={30,40,50,60}
print(x.symmetric_difference(y)) #{10, 50, 20, 60}
print(x^y) #{10, 50, 20, 60}
```

Membership operators: (in , not in)
```py
 s=set("durga")

 print(s)  # {'u', 'g', 'r', 'd', 'a'}
 print('d' in s) # True
 print('z' in s)  # False
```
Set Comprehension:

Set comprehension is possible.
```py
s={x*x for x in range(5)}
print(s) #{0, 1, 4, 9, 16}
s={2**x for x in range(2,10,2)}
print(s) #{16, 256, 64, 4}

### set objects won't support indexing and slicing:
# Eg:
s={10,20,30,40}
print(s[0]) # ==>TypeError: 'set' object does not support indexing
print(s[1:3]) # ==>TypeError: 'set' object is not subscriptable
```

Q.Write a program to eliminate duplicates present in the list?
Approach-1:
```py

l=eval(input("Enter List of values: "))
s=set(l)
print(s)

 Enter List of values: [10,20,30,10,20,40]
 {40, 10, 20, 30}
```
Approach-2:

```py
l=eval(input("Enter List of values: "))
l1=[]
for x in l:
    if x not in l1:
        l1.append(x)
print(l1)
Enter List of values: [10,20,30,10,20,40]
[10, 20, 30, 40]
```

Q. Write a program to print different vowels present in the given word?
```py
w=input("Enter word to search for vowels: ")
s=set(w)
v={'a','e','i','o','u'}
d=s.intersection(v)

print("The different vowel present in",w,"are",d)

Enter word to search for vowels: durga
The different vowel present in durga are {'u', 'a'}
```

#### 42. Python Program to Illustrate Different Set Operations
```py
# Python Program to Illustrate Different Set Operations

# Define two sets
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

print("Set 1:", set1)
print("Set 2:", set2)

# Union of sets
union_set = set1 | set2
print("\nUnion of Set1 and Set2:", union_set)

# Intersection of sets
intersection_set = set1 & set2
print("Intersection of Set1 and Set2:", intersection_set)

# Difference of sets
difference_set1 = set1 - set2
difference_set2 = set2 - set1
print("Difference of Set1 - Set2:", difference_set1)
print("Difference of Set2 - Set1:", difference_set2)

# Symmetric Difference of sets
symmetric_difference_set = set1 ^ set2
print("Symmetric Difference of Set1 and Set2:", symmetric_difference_set)

# Subset and Superset
print("\nIs Set1 subset of Set2?", set1.issubset(set2))
print("Is Set1 superset of Set2?", set1.issuperset(set2))

# Disjoint sets
print("Are Set1 and Set2 disjoint?", set1.isdisjoint(set2))

```