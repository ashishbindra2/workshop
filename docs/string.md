## String

## STRING DATA TYPE
The most commonly used object in any project and in any programming language is String

### How to define multi-line String Literals? 
We can define multi-line String literals by using triple single or double quotes.
```py
multi_line_str = """Any sequence of characters 
within either single quotes 
or double quotes is considered 
as a String."""
print(multi_line_str)
```
### How to Access Characters of a String? 
We can access characters of a string by using the following ways. 

1. By using index 
2. By using slice operator
#### 1) Accessing Characters By using Index: 
* Python supports both +ve and -ve Index.
```py

name = "Ashish Bindra"

print(name[0]) # A
print(name[5]) # h
print(name[-1]) # a
print(name[20])
IndexError: string index out of range

```
#### 2) Accessing Characters by using Slice Operator: 
- ***Syntax:***  name bEginindex:endindex:step]
- ***Begin Index:*** From where we have to consider slice (substring) 
- ***End Index:*** We have to terminate the slice (substring) at endindex-1 
- ***Step:*** Incremented Value.
```py

str1 = "Learning Python is very very easy!!!"

print(str1[1:7:1]) # earnin
print(str1[1:7])   # earnin
print(str1[1:7:2]) # eri
print(str1[:7])    # Learnin
print(str1[7:])    # g Python is very very easy!!!
print(str1[::])    # Learning Python is very very easy!!!
print(str1[:])     # Learning Python is very very easy!!!
print(str1[::-1])  # !!!ysae yrev yrev si nohtyP gninraeL
```

### Mathematical Operators for String:
We can apply the following mathematical operators for Strings. 

1) + operator for concatenation 
2) * operator for repetition

```py
print("Hello" + "World") # HelloWorld
print("Hi"*2)            # HiHi
```
#### Note: 

1) To use + operator for Strings, compulsory both arguments should be str type. 
2) To use * operator for Strings, compulsory one argument should be str and other argument should be int.




## Assignment Question / Answers
### 66. Python Program to Print Output Without a Newline

```py
name = "ashish"
print(name,end="")
```

### 77. Python Program to Trim Whitespace From a String
```py title="strip()"
str1 = " Python Program  "
str1.strip()
```
```py title="ltrip()"
str1= " Python Program "
str1.lstrip()
```
```py title="rtrip()"
str1= "Python Program  "
str1.rstrip()
```

### 71. Python Program to Create a Long Multiline String
```py
# Example 1: Using triple quotes
my_string = '''The only way to
learn to program is
by writing code.'''

print(my_string)
```

```py
# Example 2: Using parentheses and a single/double quotes
my_string = ("The only way to \n"
        	"learn to program is \n"
        	"by writing code.")

print(my_string)
```

### 41. Python Program to Sort Words in Alphabetic Order
```py
# Program to sort alphabetically the words form a string provided by the user

my_str = "Hello this Is an Example With cased letters"

# To take input from the user
#my_str = input("Enter a string: ")

# breakdown the string into a list of words
words = [word.lower() for word in my_str.split()]

# sort the list
words.sort()

# display the sorted words

print("The sorted words are:")
for word in words:
   print(word)
```
```py
s = "v a"
ss = s.split()
ss.sort()
ss

```

#### 91. Python Program to Capitalize the First Character of a String
```py
s = "ashish"

s.capitalize()
```
#### 67. Python Program to Check If a String Is a Number (Float)
```py
def is_float(value):
    try:
        float(value)
        return True
    except ValueError:
        return False

test_string1 = "123.45"

print(f"Is '{test_string1}' a float? {is_float(test_string1)}")


```
```py
type(is_float) == type(3.9)

type(is_float) == type(float())
```
#### 39. Python Program to Check Whether a String is Palindrome or Not
```py
s = "madam"

"palindrome" if ''.join(reversed(s)) == s else "not palindrome"
```
```py
s= "level"

if s==s[::-1]: 
    print('The given string is palindrome') 
else: 
    print('The given string is not palindrome')
```
```py
# Program to check if a string is palindrome or not

my_str = 'aIbohPhoBiA'

# make it suitable for caseless comparison
my_str = my_str.casefold()

# reverse the string
rev_str = reversed(my_str)

# check if the string is equal to its reverse
if list(my_str) == list(rev_str):
   print("The string is a palindrome.")
else:
   print("The string is not a palindrome.")

```
#### 40. Python Program to Remove Punctuations From a String
```py
s = "ashish Bindru"
v="aeiou" 

for w in v:
    print(s.count(w))
# print("The different vowel present in",w,"are",d)
```
```py
w = "ashish Bindru"

s=set(w) 

v={'a','e','i','o','u'} 
d=s.intersection(v) 

print("The different vowel present in",w,"are",d)
```
```py
vowels = { "a":0, "e":0, "i":0, "o":0, "u":0 }

s = "ashish Bindru"

vowels = {word: s.count(word) for word in 'aeiou'}


vowels
```
#### 43. Python Program to Count the Number of Each Vowel
```py
my_string = '''The only way to
learn to program is
by writing code.'''

print(my_string)
```
```py
vowels = { "a":0, "e":0, "i":0, "o":0, "u":0 }

s = "ashish Bindru"

vowels =  {word:s.count(word) for word in s if word in vowels}

vowels
```
```py
vowels = { "a":0, "e":0, "i":0, "o":0, "u":0 }

s = "ashish Bindru"

for word in s:
    if word in vowels:
        vowels[word]+=1

vowels
```
```py
# Program to count the number of each vowels

# string of vowels
vowels = 'aeiou'

ip_str = 'Hello, have you tried our tutorial section yet?'

# make it suitable for caseless comparisions
ip_str = ip_str.casefold()

# make a dictionary with each vowel a key and value 0
count = {}.fromkeys(vowels,0)

# count the vowels
for char in ip_str:
   if char in count:
       count[char] += 1

print(count)

```
```py
# Using a list and a dictionary comprehension
# Using dictionary and list comprehension

ip_str = 'Hello, have you tried our tutorial section yet?'

# make it suitable for caseless comparisions
ip_str = ip_str.casefold()

# count the vowels
count = {x:sum([1 for char in ip_str if char == x]) for x in 'aeiou'}

print(count)
```
#### 47. Python Program to Create Pyramid Patterns
```py
n=7
for i in range(1,n+1):
    print(" "*(n-i),end="")
    
    for j in range(1,i+1):
        print("*",end=" ")
   
    print()
```

```py
k = 0
rows = 7
for i in range(1, rows+1):
    for space in range(1, (rows-i)+1):
        print(end="  ")
   
    while k!=(2*i-1):
        print("* ", end="")
        k += 1
   
    k = 0
    print()
```
#### 61. Python Program to Parse a String to a Float or Int
```py title="Example 1: Parse string into integer"
balance_str = "1500"
balance_int = int(balance_str)

# print the type
print(type(balance_int))

# print the value
print(balance_int)
```

```py title="Example 2: Parse string into float"
balance_str = "1500.4"
balance_float = float(balance_str)

# print the type
print(type(balance_float))

# print the value
print(balance_float)
```

```py title="Example 3: A string float numeral into integer"
balance_str = "1500.34"
balance_int = int(float(balance_str))

# print the type
print(type(balance_int))

# print the value
print(balance_int)

```
#### 63. Python Program to Convert String to Datetime
```py
from datetime import datetime

my_date_string = "Mar 11 2011 11:31AM"

datetime_object = datetime.strptime(my_date_string, '%b %d %Y %I:%M%p')

print(type(datetime_object))
print(datetime_object)
```
```py
from dateutil import parser

date_time = parser.parse("Mar 11 2011 11:31AM")

print(date_time)
print(type(date_time))
```

#### 65. Python Program to Get a Substring of a String
```py
# Using String slicing
my_string = "I love python."

# prints "love"
print(my_string[2:6])

# prints "love python."
print(my_string[2:])

# prints "I love python"
print(my_string[:-1])
```

```py
my_string.find("love")
```

```py
my_string.index("love")
```
#### 68. Python Program to Count the Occurrence of an Item in a List
```py
numbers = [1, 2, 3, 2, 4, 2, 5]
item = 2
count = 0

for element in numbers:
    if element == item:
        count += 1

print(f"{element_to_count} occurs {count} times in the list.")
```

```py
numbers = [1, 2, 3, 2, 4, 2, 5]

count_num = set(numbers)

for n in count_num:
    if numbers.count(n):
        print(f"{n} occures {numbers.count(n)}")
```

```py
numbers = [1, 2, 3, 2, 4, 2, 5]

l1 = []
l2 = []
for num in numbers:
    if num not in l1:
        l1.append(num)
    else:
        l2.append(num)


l1,l2
```

```py
from collections import Counter

my_list = [1, 2, 3, 4, 2, 2, 5, 6, 5, 3]

occurrences = Counter(my_list)
occurrences
```

```py
# Using count() method
freq = ['a', 1, 'a', 4, 3, 2, 'a'].count('a')
print(freq)
```
#### 87. Python Program to Reverse a Number
```py
n = 12345
str(n)[::-1]
```

```py
n = 12345343

new =0
while n:
    r =n%10
    new = new * 10 +r
    n = n//10
new
```
```py
n = 12345

s =''.join(reversed(str(n)))
s
```

#### 90. Python Program to Check If Two Strings are Anagram
Two strings are said to be anagrams iff both are having same content irrespective of characters position.
```py
s1 = "papa"
s2 = "appa"

if sorted(s1) == sorted(s2):
    print("The strings are anagrams.")
else:
    print("The strings aren't anagrams.") 
```

```py
s1 = "".join(sorted(s1))
s2 = "".join(sorted(s2))

if s1 is s2:
    print("The strings are anagrams.")
else:
    print("The strings aren't anagrams.") 
print(s1,s2)
```
```py
from collections import Counter

# Function to check if two strings are anagrams
def are_anagrams(str1, str2):
    # Anagrams must have the same length
    if len(str1) != len(str2):
        return False
    print(Counter(str1))
    # Compare character counts using Counter
    return Counter(str1) == Counter(str2)
are_anagrams("lazy","zaly")
```
### 92. Python Program to Compute all the Permutation of the String
Permutation is the method of selecting elements from a set in different ways.

For example: the number of ways in which characters from yup can be selected are

* yup, ypu, uyp, upy, puy, pyu, and not selecting any
```py
def get_permutation(string, i=0):

    if i == len(string):   	 
        print("".join(string))

    for j in range(i, len(string)):

        words = [c for c in string]
   
        # swap
        words[i], words[j] = words[j], words[i]
   	 
        get_permutation(words, i + 1)

print(get_permutation('yup'))
```

```py
for p in permutations('pro'):
    print(p)
```

```py
from itertools import permutations

words = [''.join(p) for p in permutations('pro')]

print(words)

```
#### 94. Python Program to Count the Number of Occurrence of a Character in String 
```py
count = 0

my_string = "ashish bindra"
my_char = "r"

for i in my_string:
    if i == my_char:
        count += 1

print(count)
```
```py
print(my_string.count(my_char))
```
```py
s = "ashish bindra"
d={}

for x in s: 
    if x in d.keys(): 
        d[x]=d[x]+1 
    else: 
        d[x]=1

for k,v in d.items():
    print(f"{k} = {v} Times")
```
#### 96. Python Program to Convert Bytes to a String
```py
byte_data = b'Hello, World!'
print(type(byte_data))

string_data = byte_data.decode('utf-8')
print(type(string_data))

value = bytes("ashish".encode())

print(value, type(value)
```