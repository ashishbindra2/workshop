### Important Interview Question

- - -
***Q1. What is the difference between is operator & == operator in Python***

    Ans. In general 'is' operator meant for reference comparsion or address compression i.e if two reference are pointing to same object then only is operator returns True.
    == operator meants for cntent comparision i.e even though objects are different, if the content is the same then == operator return True
l1 = [10,20,30,40]
l2 = [10,20,30,40]

print(l1 is l2) # False

id(l1)
id(l2) # id are different

print(l1 ==l2) # True

l3 = l1

print(l1 is l3) # True
Q2. Explain about Ternary operator or conditional operator?

     x = first_value if condition else second_value
       
    If condition is True then first value will be considered otherewise second value will be considered.
   
    
# eg - 1  find Max of 2 given number

max = a if a > b else b

# Nesting of ternary operator is possible

max a if a>b and a>c else b if b >c else c
Q3 . What are various in built data types avaliable in python?

    first 5 are fundamental data types

    1. int
    2. float
    3. complex   
    4. str
    5. bool
    
    6. list
    7. touple
    8. set
    9. dict 
    10. frozenset
    11. bytes
    12. bytearray
    13. range
    

Q4. Explain mutability and immutability with an example?

- Mutable means changeable where as immutable means non changeable.
- Onece we creates an object, if we are allowed to chances its content that object is said to be mutable object
  - eg. list object is mutable
  - l = [1,2,3,4]
  - l[1] = 77
- Once we create an object, if we are not allowed to chnage its content then that object is said to be immutable.
  - eg
    - t = (1,2,3,4)
    - t[1] = 777 # typeError

Q5. In python which object are mutable and which are immutable
ans. All fundamentaldata types are immutable

- list -> mutable
- touple -> immutable
- set -> mutable
- Dict -> mutable
- frozenset -> immutable
- bytes -> immutable
- bytearrray ->mutable
- range -> immutable

Q.6 Explain the difference b/w list and touple?
ans.

1. - List is group of comma seperated values with square brackets and sequare braketa are mandatory
       `l= [10,20,30,40]`
   - Tuple is a group of comma seprated value within parenthesis and paranthis are optional
       - `t = (10,20,30,40)`
       - `t = 10,20,30,40`
2. - List objects are mutable i.e once we creates list object, we can changes its content
        `l[0] = 777`
   - Touple objects are immutable i.e once we create touple object,we are not allowed to change its content
    `t[0] = 777 # typeError`
3. - List object require more memory
   - Touple objects require less memory
4. - List object won't be reusable
   - Touple object are reusable
5. - Performance of list is low i.e operation of list object require more time
   - Performance of touple is high i.e operations on touple object required less time
6. - Comprehension concept is applicable for list
    - Comprehension concept is not applicable for touple
7. - **list objects are unhashable types and hece we cannot store in set, in dict as key**
    - Touple object are hashable type and hence we can store in set and in dict as key
8. - If the content is not fixed and keep on changing then it is recommended to go fore list object
        - eg to store youtube comments
     - if the content is fixed and nerver changes then we should go for touple object
         - eg Allowed input value for vender machine
9. - Unpacking is possible in list but packing is not possible
       - `l = a,b,c,d,e` -> it is not list
       - `a,b,c,d,e = l` -> valid
    - Both packing and unpacking are possible in touple
Q7. Q What is the difference between set and frozenset?

- All proerty of set and frozenset are same except the following difference.
- Set is mutable where as frozenset is immutable
- We can add new elements to the set as it is mutable
- As frozenset is mutable, add, remove such type of terminology is nit applicablee.

# set

s = {10, 20, 30, 40}
s.add(50)
print(s)
s = {10, 20, 30, 40}

fs = frozenset(s)
fs.add(50)
print(fs) # Attribute error

#### Q8. What is different between List and Dist ?

|  S.No |     List                                         |   Dict                                               |
| ----- |:------------------------------------------------:| ----------------------------------------------------:|
|1      | List is group of a comma sepaarated invidiual    | Dict is a group of comma separated key - value pair  |
|       | objects within square brackets                   | courly bracy `d = {'A': 'APPLE;}`                    |  
|       | eg `l = [10, 20, 30]`                           |                                                      |
| 2     | Insertion order is preserved                     | In dict,all key -value pair will be stored based on  |
|       |                                                  | hashcode of key & hence insertion order is not       |             |       |                                                  | preserved but from 3.7 version onwords the dict      |              |       |                                                  | functionality internally replaced with ordered dict  |
|       |                                                  | functionality. 'Hence from 3.7 version onwords in the|
|       |                                                  | case of normal dict also insertion order can be      |
|       |                                                  | guranted.                                            |

3. - In List,, DUplicate object are allowed
   - In Dict, Duplicate keys are not allowed, but values can be dublicated. if we are trying to add an entry with
   key-value with dublicate key then old value will be replaced with new value

4. - In list we can access objects by using index,which is zero based i.e index of dirst object is zero
   - In dict we can access value by using keys

5. - In list objects need not be hashable
   - but IB DIct, key must be hashable

#### Q9. What is the difference between List and Set?

1. - List is a group of comma seprated individual objects with in square brackets eg `l = [10,20,30]`
   - Set is a group of comma seprated individaul object with in curly brakets eg `l = {10,20,30}`
2. - Duplicate objects are allowed.
   - Duplicate objects are not allowed
3. - Insertion order is presved
   - Insertion order is not presved objects will be inserted based on hashcode.
4. - Object need not hashable.
   - Object should be hashable.
5  - Indexing and slicing concepts are applicable for list.
   - Indexing and slicing concept are not applicable for set

#### Q10. Explain Slice Operator and its syntax?

If we want to access part(piece or slice) of given sequence, then we should go for slice operator. The sequence can be string ot list or touplce etc.

#### Syntax

---------

***s[begin: end: step]***

- Step value can be either postive or negative (but not zero)
- If step value is postive, then we have consider from begin index to end-1 index in forword direction
- If step values is negative, then we have to consider from begin index to end +1 index backword direction.

***NOTE:***

- In forword direction if end value is 0, then the result is always empty.
- In bakword direction if end value is -1, then the result is always empty.
    eg s='abcdefghij'
    s[1:6:2]--> 'bdf'
    s[7:4:-1]--> 'hgf'
s='abcdefghij'
print(s[1:6:2])
s[7:4:-1]

#### Q11 Whar is the diffterent between *args and **kwargs

- *args -> variable length arguments

    `def f1(*args):`<br>
    `pass`<br>
    `f1(*args)`<br>

- If a function with *args argument, then we can call that function by passing any number of values including zero number with all these values tuple will be created.

    `def f1(*args):`<br>
        `print(args)`<br>
     `f1(),f1(10),f1(10,20).....`<br>

- **kwargs -> Variable length keyword arguments
 ` f(**kwargs):

- We can call this function by passing any number of keyword arguments including zero number and with all these keyword arguments a dictionary will be created.
     `def f1(**kwargs)`<br>
         `print(kwargs)`<br>
     `f1('name'='d','roll'=101)`

#### Q12 How to reverse string by using slice opertor?

`s[::-1]`

#### Q What is different between `dir()` and `help()` function?

- dir()
  - dir() function just list out all members module But help() function provides documentation related to that module

        `import math`<br>

        `print(dir(math))`# return list of all member
- help(math)<br>

`print(dir())` # curent module information

***Note:***

- ***dir()*** => Without argument, it will list out all members of specified module.
- ***dir(module_name)*** => With argumetn, it will list out all members of specified module

# eg1

import math

print(dir(math))
print(dir())

#### Q What is lambda function or Anonymous function?

- Sometines we can declare afunction without any name, such type of nameless functions are called anonymous functions or lambda functions.

- The main objective of anonymous dunction is just for instant use

#### ***Normal Function***

---------------------
We can define function by using def keyword.
`def sqareit(n):`<br>
    `return n*n`<br>

#### ***Lamda Function***

---------------------
we can define anonymous function by using lamda keyword.
Syntax of Lambda Function

```python
lambda arguments: expression
lambda → The keyword to define a lambda function.
```

arguments → Inputs to the function (can be multiple, separated by commas).
expression → A single expression evaluated and returned.

Example 1: Basic Lambda Function

```python

square = lambda x: x ** 2
print(square(5))  # Output: 25
```

Equivalent to:

```python
def square(x):
    return x ** 2
```

Example 2: Lambda with Multiple Arguments

```python
add = lambda a, b: a + b
print(add(3, 7))  # Output: 10
```

Example 3: Lambda in Sorting
Sorting a list of tuples by the second element:

```py
data = [(1, 3), (2, 2), (4, 1)]
data.sort(key=lambda x: x[1])
print(data)  # Output: [(4, 1), (2, 2), (1, 3)]
```

Example 4: Using Lambda with map(), filter(), and reduce()

1. Using map() to apply a function to a list

```py
numbers = [1, 2, 3, 4]
squared = list(map(lambda x: x ** 2, numbers))
print(squared)  # Output: [1, 4, 9, 16]
```

2. Using filter() to filter values

```py
nums = [1, 2, 3, 4, 5, 6]
evens = list(filter(lambda x: x % 2 == 0, nums))
print(evens)  # Output: [2, 4, 6]
```

3. Using reduce() from functools

```py
from functools import reduce
nums = [1, 2, 3, 4]
product = reduce(lambda x, y: x * y, nums)
print(product)  # Output: 24
```

When to Use Lambda Functions?
✅ Short and simple operations
✅ Inline usage (e.g., sorting, filtering, mapping)
✅ Avoiding unnecessary function definitions

<https://github.com/learning-zone/python-basics>
