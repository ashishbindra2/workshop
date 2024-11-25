# List
In Python, `extend()` and `append()` are methods used to add elements to a list, but they work in different ways. Here's a detailed comparison:

---

### **`append()` Method**

- **Functionality**: Adds a single element (object) to the end of the list.  
- **Effect**: Treats the argument as a single item and appends it directly.  

#### **Example**:
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

#### **Example**:
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

#### **Comparison Example**:
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
#### 37. Python Program to Transpose a Matrix
#### 38. Python Program to Multiply Two Matrices
#### 50. Python Program to Access Index of a List Using for Loop

#### 51. Python Program to Flatten a Nested List
#### 52. Python Program to Slice Lists
#### 55. Python Program to Check If a List is Empty
#### 58. Python Program to Concatenate Two Lists
#### 60. Python Program to Split a List Into Evenly Sized Chunks
#### 64. Python Program to Get the Last Element of the List
#### 85. Python Program to Iterate Through Two Lists in Parallel
#### 95. Python Program to Remove Duplicate Element From a List
