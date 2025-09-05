# List

In Python, `extend()` and `append()` are methods used to add elements to a list, but they work in different ways. Here's a detailed comparison:

---

## METHODS

### **`append()` Method**

- **Functionality**: Adds a single element (object) to the end of the list.  
- **Effect**: Treats the argument as a single item and appends it directly.  

#### **Example**

```python
# Using append
my_list = [1, 2, 3]
my_list.append(4)
print(my_list)  # Output: [1, 2, 3, 4]

# Appending a list (nested list)
my_list.append([5, 6])
print(my_list)  # Output: [1, 2, 3, 4, [5, 6]]
```

> **Note**: If you append another list, it gets added as a single element, resulting in a nested list.

---

### **`extend()` Method**

- **Functionality**: Adds all the elements of an iterable (e.g., list, tuple, string) to the end of the list.  
- **Effect**: Iterates over the argument and appends each element to the list individually.  

## Example

```python
# Using extend
my_list = [1, 2, 3]
my_list.extend([4, 5])
print(my_list)  # Output: [1, 2, 3, 4, 5]

# Extending with a string (iterable)
my_list.extend("67")
print(my_list)  # Output: [1, 2, 3, 4, 5, '6', '7']
```

> **Note**: If you pass a list to `extend`, its elements are added individually, not as a nested list.

---

### **Key Differences**

| **Aspect**             | **`append()`**                              | **`extend()`**                              |
|-------------------------|---------------------------------------------|---------------------------------------------|
| **Type of argument**    | Any object (single element)                | Iterable (list, tuple, string, etc.)        |
| **Behavior**            | Adds the argument as a single item.        | Adds each element of the argument.          |
| **Nested lists**        | Creates a nested list when a list is appended. | Merges elements into the original list.    |
| **Use case**            | Add one item or object to the list.        | Add multiple elements from an iterable.     |

---

### **When to Use Which**

- Use **`append()`** when you want to add a single element (e.g., an integer, string, or even a list as a nested list).
- Use **`extend()`** when you want to combine another iterable's elements into your list.

#### **Comparison Example**

```python
# Append vs Extend
list1 = [1, 2, 3]

list1.append([4, 5])  # Adds as a single element (nested list)
print(list1)  # Output: [1, 2, 3, [4, 5]]

list2 = [1, 2, 3]
list2.extend([4, 5])  # Adds elements individually
print(list2)  # Output: [1, 2, 3, 4, 5]
```

### **Summary**

- Use `append()` for adding a single object.  
- Use `extend()` for adding multiple elements.

#### 36. Python Program to Add Two Matrices

```py
# Program to add two matrices using nested loop

X = [[12,7,3],
    [4 ,5,6],
    [7 ,8,9]]

Y = [[5,8,1],
    [6,7,3],
    [4,5,9]]

result = [[0,0,0],
         [0,0,0],
         [0,0,0]]

# iterate through rows
for i in range(len(X)):
   # iterate through columns
   for j in range(len(X[0])):
       result[i][j] = X[i][j] + Y[i][j]

for r in result:
   print(r)

```

```py
# Program to add two matrices using list comprehension

X = [[12,7,3],
    [4 ,5,6],
    [7 ,8,9]]

Y = [[5,8,1],
    [6,7,3],
    [4,5,9]]

result = [[X[i][j] + Y[i][j]  for j in range(len(X[0]))] for i in range(len(X))]

for r in result:
   print(r)
```

#### 37. Python Program to Transpose a Matrix

```py
# Program to transpose a matrix using a nested loop

X = [[12,7],
    [4 ,5],
    [3 ,8]]

result = [[0,0,0],
         [0,0,0]]

# iterate through rows
for i in range(len(X)):
   # iterate through columns
   for j in range(len(X[0])):
       result[j][i] = X[i][j]

for r in result:
   print(r)

```

```py
''' Program to transpose a matrix using list comprehension'''

X = [[12,7],
    [4 ,5],
    [3 ,8]]

result = [[X[j][i] for j in range(len(X))] for i in range(len(X[0]))]

for r in result:
   print(r)
```

### 38. Python Program to Multiply Two Matrices

Matrix Multiplication using Nested Loop

Program to multiply two matrices using nested loops

```py
# 3x3 matrix

X = [[12,7,3],
    [4 ,5,6],
    [7 ,8,9]]

# 3x4 matrix

Y = [[5,8,1,2],
    [6,7,3,0],
    [4,5,9,1]]

# result is 3x4

result = [[0,0,0,0],
         [0,0,0,0],
         [0,0,0,0]]

# iterate through rows of X

for i in range(len(X)):

# iterate through columns of Y

   for j in range(len(Y[0])):
       # iterate through rows of Y
       for k in range(len(Y)):
           result[i][j] += X[i][k] * Y[k][j]

for r in result:
   print(r)
```

Matrix Multiplication Using Nested List Comprehension

```py
# Program to multiply two matrices using list comprehension

# 3x3 matrix
X = [[12,7,3],
    [4 ,5,6],
    [7 ,8,9]]

# 3x4 matrix
Y = [[5,8,1,2],
    [6,7,3,0],
    [4,5,9,1]]

# result is 3x4
result = [[sum(a*b for a,b in zip(X_row,Y_col)) for Y_col in zip(*Y)] for X_row in X]

for r in result:
   print(r)

```

### 50. Python Program to Access Index of a List Using for Loop

```py
data = ["a", "b", "c"]
for i in range(len(data)): 
    print(i, data[i])
```

```py
my_list = [21, 44, 35, 11]

for index, val in enumerate(my_list):
    print(index, val)
```

#### 51. Python Program to Flatten a Nested List

```py
my_list = [[1], [2, 3], [4, 5, 6, 7]]

flat_list = [num for sublist in my_list for num in sublist]
print(flat_list)
```

```py
# Example 2: Using Nested for Loops (non pythonic way)
my_list = [[1], [2, 3], [4, 5, 6, 7]]

flat_list = []
for sublist in my_list:
    for num in sublist:
        flat_list.append(num)

print(flat_list)
```

```py
# Example 3: Using itertools package
import itertools

my_list = [[1], [2, 3], [4, 5, 6, 7]]

flat_list = list(itertools.chain(*my_list))
print(flat_list)
```

```py
# Example 4: Using sum()
my_list = [[1], [2, 3], [4, 5, 6, 7]]

flat_list = sum(my_list, [])
print(flat_list)
```

```py
from functools import reduce

my_list = [[1], [2, 3], [4, 5, 6, 7]]
reduce(lambda x,y: x+y, my_list)
```

### 52. Python Program to Slice Lists

The format for list slicing is [start:stop:step].

```py
my_list = [1, 2, 3, 4, 5]

print(my_list[2:])
```

```py
my_list = [1, 2, 3, 4, 5]

print(my_list[::2])
```

### 55. Python Program to Check If a List is Empty

```py
# Example 1: Using Boolean operation
my_list = []
if not my_list:
    print("the list is empty")
```

```py
# Example 2: Using len()
my_list = []
if len(my_list) == 0:
    print("the list is empty")
```

```py
# Example 3: Comparing with []
my_list = []
if my_list == []:
    print("The list is empty")
```

### 58. Python Program to Concatenate Two Lists

```py
# Example 1: Using + operator
list_1 = [1, 'a']
list_2 = [3, 4, 5]

list_joined = list_1 + list_2
print(list_joined)
```

```py
# Example 2: Using iterable unpacking operator *
list_1 = [1, 'a']
list_2 = range(2, 4)

list_joined = [*list_1, *list_2]
print(list_joined)
```

```py
# Example 3: With unique values
list_1 = [1, 'a']
list_2 = [1, 2, 3]

list_joined = list(set(list_1 + list_2))
print(list_joined)
```

```py
# Example 4: Using extend()
list_1 = [1, 'a']
list_2 = [1, 2, 3]

list_2.extend(list_1)
print(list_2)
```

### 60. Python Program to Split a List Into Evenly Sized Chunks

```py
# Example 1: Using yield
def split(list_a, chunk_size):

  for i in range(0, len(list_a), chunk_size):
    yield list_a[i:i + chunk_size]

chunk_size = 2
my_list = [1,2,3,4,5,6,7,8,9]
print(list(split(my_list, chunk_size)))
```

> [[1, 2], [3, 4], [5, 6], [7, 8], [9]]

```py

chunk_size = 2
list_chunked = [my_list[i:i + chunk_size] for i in range(0, len(my_list), chunk_size)]
print(list_chunked)
```

```py
# Example 2: Using numpy
import numpy as np

my_list = [1,2,3,4,5,6,7,8,9]
print(np.array_split(my_list, 5))
```

#### 64. Python Program to Get the Last Element of the List

```py
my_list = ['a', 'b', 'c', 'd', 'e']

# print the last element
print(my_list[-1])
```

```py
my_list[len(my_list)- 1]
```

#### 85. Python Program to Iterate Through Two Lists in Parallel

```py
# Example 1: Using zip
list_1 = [1, 2, 3, 4]
list_2 = ['a', 'b', 'c']

for i, j in zip(list_1, list_2):
    print(i, j)
```

```py
# loop until the longer list stops
for i,j in itertools.zip_longest(list_1,list_2):
    print(i,j)
```

### 95. Python Program to Remove Duplicate Element From a List

```py
l=[1,21,2,1,2,21,12,34,] 
l1=set(l)

l1
```

> {1, 2, 12, 21, 34}

```py
# Example 2: Remove the items that are duplicated in two lists
list_1 = [1, 2, 1, 4, 6]
list_2 = [7, 8, 2, 1]

print(list(set(list_1) ^ set(list_2)))
```

> [4, 6, 7, 8]

```py
l=[1,21,2,1,2,21,12,34,] 
l1=[]

for x in l:
    if x not in l1:
        l1.append(x) 

print(l1)
```

> [1, 21, 2, 12, 34]

```py
l=[1,21,2,1,2,21,12,34,] 
l1= []

[l1.append(x) for x in l if x not in l1]

print(l1)
```

```py
l=[1,21,2,1,2,21,12,34] 
l1= []

l1 = []
l3 = [l1.append(x)  if x not in l1 else x for x in l]

print(l1)
l3
```

> [1, 21, 2, 12, 34]
[None, None, None, 1, 2, 21, None, None]
