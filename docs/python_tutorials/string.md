# String

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

#### 1) Accessing Characters By using Index

* Python supports both +ve and -ve Index.

```py

name = "Ashish Bindra"

print(name[0]) # A
print(name[5]) # h
print(name[-1]) # a
print(name[20])
IndexError: string index out of range

```

#### 2) Accessing Characters by using Slice Operator

* ***Syntax:***  name bEginindex:endindex:step]
* ***Begin Index:*** From where we have to consider slice (substring)
* ***End Index:*** We have to terminate the slice (substring) at endindex-1
* ***Step:*** Incremented Value.

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

### Mathematical Operators for String

We can apply the following mathematical operators for Strings.

1) * operator for concatenation
2) * operator for repetition

```py
print("Hello" + "World") # HelloWorld
print("Hi"*2)            # HiHi
```

#### Note

1) To use + operator for Strings, compulsory both arguments should be str type.
2) To use * operator for Strings, compulsory one argument should be str and other argument should be int.

#### Q) Write a Program to access each Character of String in Forward and Backward Direction by using while Loop?

```py linenums="1"
s = "Learning Python is very easy !!!" 
n = len(s) 
i = 0 

print("Forward direction") 

while i<n: 
    print(s[i],end=' ') 
    i +=1 
    
print("\n\nBackward direction") 
i = -1 

while i >= -n: 
    print(s[i],end=' ') 
    i = i-1


# o/p
# Forward direction
# L e a r n i n g   P y t h o n   i s   v e r y   e a s y   ! ! ! 

# Backward direction
# ! ! !   y s a e   y r e v   s i   n o h t y P   g n i n r a e L
```

Alternative ways:

```py linenums="1"
s = "Learning Python is very easy !!!" 

print("Forward direction") 
for i in s[::]: 
    print(i,end=' ') 

print("\nBackward direction")
for i in s[::-1]: 
    print(i,end=' ')
```

### Checking Membership

We can check whether the character or string is the member of another string or not by using in and not in operators.

```py linenums="1"
str1 = 'durga' 

print('d' in str1) # True
print('z' in str1) # False
```

```py linenums="1"

str1 = input("Enter main string: ") 
subs = input("Enter sub string: ") 

if subs in str1: 
    print(f"\"{subs}\" is found in main string") 
else: 
    print(f"\"{subs}\" is not found in main string")
# Enter main string: Ashish Bindra
# Enter sub string: sh
# "sh" is found in main string

```

### Comparison of Strings

* We can use comparison operators (<, <=, >, >=) and equality operators (==, !=) for strings.
* Comparison will be performed based on alphabetical order.

```py linenums="1"
s1=input("Enter first string: ") 
s2=input("Enter Second string: ") 

if s1==s2: 
    print("Both strings are equal") 
elif s1<s2: 
    print("First String is less than Second String") 
else: 
    print("First String is greater than Second String")
```

o/p
Enter first string: durga
Enter Second string: durga Both strings are equal

### Removing Spaces from the String

We can use the following 3 methods

1) rstrip(): To remove spaces at right hand side
2) lstrip(): To remove spaces at left hand side
3) strip(): To remove spaces both sides

```py linenums="1"
city=input("Enter your city Name: ") 
scity=city.strip() 

if scity=='Hyderabad': 
    print("Hello Hyderbadi..Adab") 
elif scity=='Chennai': 
    print("Hello Madrasi...Vanakkam") 
elif scity=="Bangalore": 
    print("Hello Kannadiga...Shubhodaya") 
else: 
    print("your entered city is invalid")
    
# Enter your city Name:Bangalore 
# Hello Kannadiga...Shubhodaya
```

### Finding Substrings

We can use the following 4 methods

For forward direction:

1) find()
2) index()

For backward direction:

1) rfind()
2) rindex()

#### find()

***s.find(substring)***

Returns index of first occurrence of the given substring. If it is not available then we will get -1.

```py linenums="1"
s="Learning Python is very easy" 

print(s.find("Python")) #9 
print(s.find("Java")) # -1 
print(s.find("r"))#3 
print(s.rfind("r"))#21
```

#### s.find(substring,bEgin,end)

It will always search from bEgin index to end-1 index.

```py linenums="1"
s="durgaravipavanshiva" 

print(s.find('a'))#4 
print(s.find('a',7,15))#10
print(s.find('z',7,15))#-1
```

### index()

index() method is exactly same as find() method except that if the specified substring is not available then we will get ValueError.

```py
s=input("Enter main string:") 
subs=input("Enter sub string:") 

try: 
    n=s.index(subs) 
except ValueError: 
    print("substring not found") 
else: 
    print("substring found")
```

o/p
Enter main string:learning python is very easy Enter sub string:python substring found

### Counting substring in the given String

We can find the number of occurrences of substring present in the given string by using count() method.

1. s.count(substring): It will search through out the string.
2. s.count(substring, bEgin, end): It will search from bEgin index to end-1 index.

```py
s="abcabcabcabcaddab" 

print(s.count('a'))     # 6  
print(s.count('ab'))    # 5
print(s.count('abc'))   # 4
print(s.count('a',3,7)) # 2
```

### Replacing a String with another String

s.replace(oldstring, newstring) inside s, every occurrence of old String will be replaced with new String.

```py title="eg 1"
s = "Learning Python is very difficult"

s1 = s.replace("difficult","easy") 
print(s1) # Learning Python is very easy
```

```py title="Eg 2: All occurrences will be replaced"
s = "ababababababab" 

replace_str = s.replace("a","b") 
print(replace_str)
```

### Q) String Objects are Immutable then how we can change the Content by using replace() Method

* Once we creates string object, we cannot change the content.This non changeable behaviour is nothing but immutability.
* If we are trying to change the content by using any method, then with those changes a new object will be created and changes won't be happend in existing object.
* Hence with replace() method also a new object got created but existing object won't be changed.

```py title="we can see new object which was created because of replace() method."  
str1 = "abab" 
str2 = str1.replace("a","b") 

print(str1,"is available at :",id(str1)) 
print(str2,"is available at :",id(str2))
```

o/p

```cmd
abab is available at : 2604224914096<br>
bbbb is available at : 2604225153904
```

### Splitting of Strings

* We can split the given string according to specified seperator by using split() method.
* l = s.split(seperator)
* The default seperator is space. The return type of split() method is List.

```py
s="durga software solutions" 

l=s.split() 
for x in l: 
    print(x)
# o/p
# durga
# software
# solutions
```

```py
date = "22-07-2024" 
date_list = date.split('-') 

for val in date_list: 
    print(val)
# o/p
# 22
# 07
# 2024
```

### Joining of Strings

We can join a Group of Strings (List OR Tuple) wrt the given Seperator.

* s = seperator.join(group of strings)

```py
names = ('sunny', 'bunny', 'chinny') 
list_name = '-'.join(names) 
print(list_name) # sunny-bunny-chinny
```

### Changing Case of a String: We can change case of a string by using the following 4 methods

1. upper(): To convert all characters to upper case
2. lower(): To convert all characters to lower case
3. swapcase(): Converts all lower case characters to upper case and all upper case characters to lower case
4. title(): To convert all character to title case. i.e first character in every word should be upper case and all remaining characters should be in lower case.
5. capitalize(): Only first character will be converted to upper case and all remaining characters can be converted to lower case
6. casefold(): Return a version of the string suitable for caseless comparisons.

```py
line = 'learning Python is very Easy' 

print(line.upper())      # LEARNING PYTHON IS VERY EASY
print(line.lower())      # learning python is very easy
print(line.swapcase())   # LEARNING pYTHON IS VERY eASY
print(line.title())      # Learning Python Is Very Easy
print(line.capitalize()) # Learning python is very easy
print(line.casefold())   # learning python is very easy
```

### Checking Starting and Ending Part of the String

Python contains the following methods for this purpose

1. s.startswith(substring)
2. s.endswith(substring)

```py
line = 'learning Python is very easy' 

print(line.startswith('learning')) # True
print(line.endswith('learning'))   # False
print(line.endswith('easy'))       # True
```

### To Check Type of Characters Present in a String: Python contains the following methods for this purpose

1. isalnum(): Returns True if all characters are alphanumeric( a to z , A to Z ,0 to9 )
2. isalpha(): Returns True if all characters are only alphabet symbols(a to z,A to Z)
3. isdigit(): Returns True if all characters are digits only( 0 to 9)
4. islower(): Returns True if all characters are lower case alphabet symbols
5. isupper(): Returns True if all characters are upper case aplhabet symbols
6. istitle(): Returns True if string is in title case
7. isspace(): Returns True if string contains only spaces

```py linenums="1"

print('Durga786'.isalnum()) # True 
print('durga786'.isalpha()) # False
print('durga'.isalpha()) # True 
print('durga'.isdigit()) # False 
print('786786'.isdigit()) # True 
print('abc'.islower()) # True 
print('Abc'.islower()) # False 
print('abc123'.islower()) # True 
print('ABC'.isupper()) # True 
print('Learning python is Easy'.istitle()) # False 
print('Learning Python Is Easy'.istitle()) # True
print(' '.isspace()) # True
```

```py linenums="1" title="demo.py"

s=input("Enter any character:")

if s.isalnum():
    print("Alpha Numeric Character") 
    if s.isalpha(): 
        print("Alphabet character") 
        if s.islower(): 
            print("Lower case alphabet character") 
        else:
            print("Upper case alphabet character") 
    else: 
        print("it is a digit") 
elif s.isspace():
    print("It is space character") 
elif not s.isalnum():
    print("it is a float")
else:
    print("Non Space Special Character")

```

### Important Programs regarding String Concept

#### Q1) Write a Program to Reverse the given String

* Input: durga
* Output: agrud

```py title="1st way"
str1 = input("Enter Some String: ") # ashish
print(str1[::-1]) # hsihsa
```

```py title="2st way"
str1 = input("Enter Some String: ") # Python
print(''.join(reversed(str1))) # nohtyP
```

```py title="3st way"
str1 = input("Enter Some String: ") # Python

i = len(str1) - 1 
target='' 

while i >= 0: 
    target = target + str1[i] 
    i = i - 1 
    
print(target) # nohtyP
```

"4st way"

```py title="4st way"
s = "hello"
reversed_s = ""

for char in s:
    reversed_s = char + reversed_s

print(reversed_s)  # Output: "olleh"
```

"Using a List Comprehension

```py title="Using a List Comprehension"
s = "hello"
reversed_s = ''.join([s[i] for i in range(len(s)-1, -1, -1)])
print(reversed_s)  # Output: "olleh"

```

```py title="Using Recursion"
def reverse_recursive(s):
    if len(s) == 0:
        return s
    else:
        return reverse_recursive(s[1:]) + s[0]

s = "hello"
reversed_s = reverse_recursive(s)
print(reversed_s)  # Output: "olleh"

```

```py title="Using reduce() from functools"
from functools import reduce

s = "hello"
reversed_s = reduce(lambda acc, char: char + acc, s)
print(reversed_s)  # Output: "olleh"

```

#### Q2) Program to Reverse Order of Words

* Input: Learning Python is very Easy
* Output: Easy Very is Python Learning

```py "

line=input("Enter Some String: ")  # Learning Python is very Easy

list_line = line.split()  
l1 = [] 
i = len(list_line) - 1  

while i >= 0: 
    l1.append(list_line[i]) 
    output = ' '.join(l1) 
    i = i - 1 
    
print(output) # Easy very is Python Learning
```

```py
line=input("Enter Some String: ")  # Learning Python is very Easy

list_line = line.split()  
list_line.reverse()

print(" ".join(list_line)) # Easy very is Python Learning
```

#### Write a Program to find the Number of Occurrences of each Character present in the given String?

* Input: ABCABCABBCDE
* Output: A-3,B-4,C-3,D-1,E-1

```py

str1 = input("Enter the Some String: ") 

d = {} 
for x in str1: 
    if x in d.keys(): 
        d[x] = d[x] + 1  
    else: 
        d[x] = 1

for k, v in d.items(): 
        print(f"{k} = {v} Times")
```

```commandLine
Enter the Some String: Ashsih
A = 1 Times
s = 2 Times
h = 2 Times
i = 1 Times
```

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

```py title="way1"
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

```py title="way 2"
s = "v a"
ss = s.split()
ss.sort()
ss

```

```py title="way2"
names = "jashan himanshu ashish"
list_names = names.split(" ")

names = " ".join(sorted(list_names))

print(names)
```

### 91. Python Program to Capitalize the First Character of a String

```py
s = "ashish"

s.capitalize()
```

### 67. Python Program to Check If a String Is a Number (Float)

```py title="way 1"
def is_float(value):
    try:
        float(value)
        return True
    except ValueError:
        return False

test_string1 = "123.45"

print(f"Is '{test_string1}' a float? {is_float(test_string1)}")


```

```py title="way 2"
type(is_float) == type(3.9)

type(is_float) == type(float())
```

```py title="way 3"
input_str = input("Enter somthing!! ").strip()

if input_str.isalpha():
    print("you enter alphabet which is string!!")
elif input_str.isdigit():
    print("String is a int!!")
else:
    print("String is float or punctuation!!")
```

``` py title="way 4"
input_str = input("Enter somthing!! ").strip()

try:
    input_str =  eval(input_str)
    if isinstance(input_str,int):
        print("you entered int")
    elif isinstance(input_str,float):
        print("you entered float")
except (NameError,SyntaxError):
    print("this is string ")
```

``` py title="way 5"
input_str = input("Enter some string ")

try:
    input_str = eval(input_str)
    
    if  type(input_str) == type(int()):
        print("You entered an int")
    
    elif type(input_str) == type(float()):
        print("You entered a float")
except (NameError,SyntaxError):
    print("This is string ")
```

### 39. Python Program to Check Whether a String is Palindrome or Not

```py title="way 1"
s = "madam"

"palindrome" if ''.join(reversed(s)) == s else "not palindrome"
```

```py title="way 2"
s= "level"

if s==s[::-1]: 
    print('The given string is palindrome') 
else: 
    print('The given string is not palindrome')
```

```py  title="way 3"
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

```py  title="way 4"

my_str = 'aIbohPhoBiA'.lower()
rev_str = ""

for s in my_str:
    rev_str=s + rev_str
print(my_str,id(my_str))
print(rev_str,id(rev_str))

if rev_str == my_str:
    print("The string is a palindrome.")
else: 
    print("The string is not a palindrome.")
```

```py  title="way 5"

my_str = 'pabap'.lower()

if len(my_str)==1 :
    print("The string is a palindrome.")
else:
    for i in range(0,len(my_str)//2):
        if my_str[i] != my_str[-1-i]:
            print("The string not is a palindrome.",my_str[-1-i])
            break    
    else:
         print("The string is a palindrome.")
```

### 40. Python Program to Remove Punctuations From a String

```py
# define punctuation
punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

my_str = "Hello!!!, he said ---and went."

# To take input from the user
# my_str = input("Enter a string: ")

# remove punctuation from the string
no_punct = ""
for char in my_str:
   if char not in punctuations:
       no_punct = no_punct + char

# display the unpunctuated string
print(no_punct)

```

``` py title="Using str.translate() with string.punctuation"
import string

def remove_punctuation(text):
    return text.translate(str.maketrans('', '', string.punctuation))

# Example usage
text = "Hello, World! How's everything?"
cleaned_text = remove_punctuation(text)
print(cleaned_text)  # Output: Hello World Hows everything

```

``` py title="Using str.replace()"
def remove_punctuation(text):
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    for char in punctuations:
        text = text.replace(char, "")
    return text

# Example usage
text = "Hello, World! How's everything?"
print(remove_punctuation(text))

```

``` py title="Using Regular Expressions"

import re

def remove_punctuation(text):
    return re.sub(r'[^\w\s]', '', text)

# Example usage
text = "Hello, World! How's everything?"
print(remove_punctuation(text))

```

### 43. Python Program to Count the Number of Each Vowel

```py title="way-1"
s = "ashish Bindru"
v="aeiou" 

for w in v:
    print(s.count(w))
# print("The different vowel present in",w,"are",d)
```

```py title="way-2"
w = "ashish Bindru"

s=set(w) 

v={'a','e','i','o','u'} 
d=s.intersection(v) 

print("The different vowel present in",w,"are",d)
```

```py title="way-3"
vowels = { "a":0, "e":0, "i":0, "o":0, "u":0 }
s = "ashish Bindru"

vowels = {word: s.count(word) for word in 'aeiou'}
print(vowels)
```

```py title="way-4"
vowels = { "a":0, "e":0, "i":0, "o":0, "u":0 }

s = "ashish Bindru"

vowels =  {word:s.count(word) for word in s if word in vowels}

print(vowels)
```

```py title="way-5"
vowels = { "a":0, "e":0, "i":0, "o":0, "u":0 }

s = "ashish Bindru"

for word in s:
    if word in vowels:
        vowels[word]+=1

print(vowels)
```

```py title="way-6"
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

```py title="way-7"
# Using a list and a dictionary comprehension
# Using dictionary and list comprehension

ip_str = 'Hello, have you tried our tutorial section yet?'

# make it suitable for caseless comparisions
ip_str = ip_str.casefold()

# count the vowels
count = {x:sum([1 for char in ip_str if char == x]) for x in 'aeiou'}

print(count)
```

### 47. Python Program to Create Pyramid Patterns

```py title="way-1"
n=7
for i in range(1,n+1):
    print(" "*(n-i),end="")
    
    for j in range(1,i+1):
        print("*",end=" ")
   
    print()
```

```py title="way-2"
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

### 61. Python Program to Parse a String to a Float or Int

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

### 63. Python Program to Convert String to Datetime

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

### 65. Python Program to Get a Substring of a String

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

### 68. Python Program to Count the Occurrence of an Item in a List

```py title="way-1"
numbers = [1, 2, 3, 2, 4, 2, 5]
item = 2
count = 0

for element in numbers:
    if element == item:
        count += 1

print(f"{element_to_count} occurs {count} times in the list.")
```

```py title="way-2"
numbers = [1, 2, 3, 2, 4, 2, 5]

count_num = set(numbers)

for n in count_num:
    if numbers.count(n):
        print(f"{n} occures {numbers.count(n)}")
```

```py title="way-3"
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

```py title="way-4"
from collections import Counter

my_list = [1, 2, 3, 4, 2, 2, 5, 6, 5, 3]

occurrences = Counter(my_list)
occurrences
```

```py title="way-5"
# Using count() method
freq = ['a', 1, 'a', 4, 3, 2, 'a'].count('a')
print(freq)
```

### 87. Python Program to Reverse a Number

```py title="way-1"
n = 12345
str(n)[::-1]
```

```py title="way-2"
n = 12345343

new =0
while n:
    r =n%10
    new = new * 10 +r
    n = n//10
new
```

```py title="way-3"
n = 12345

s =''.join(reversed(str(n)))
s
```

### 90. Python Program to Check If Two Strings are Anagram

Two strings are said to be anagrams iff both are having same content irrespective of characters position.

```py title="way-1"
s1 = "papa"
s2 = "appa"

if sorted(s1) == sorted(s2):
    print("The strings are anagrams.")
else:
    print("The strings aren't anagrams.") 
```

```py title="way-2"
s1 = "".join(sorted(s1))
s2 = "".join(sorted(s2))

if s1 is s2:
    print("The strings are anagrams.")
else:
    print("The strings aren't anagrams.") 
print(s1,s2)
```

```py title="way-3"
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

```py title="way-1"
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

```py title="way-2"
for p in permutations('pro'):
    print(p)
```

```py title="way-3"
from itertools import permutations

words = [''.join(p) for p in permutations('pro')]

print(words)

```

### 94. Python Program to Count the Number of Occurrence of a Character in String

```py title="way-1"
count = 0 

my_string = "ashish bindra"
my_char = "r"

for i in my_string:
    if i == my_char:
        count += 1

print(count)
```

```py title="way-2"
print(my_string.count(my_char))
```

```py title="way-3"
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

### 96. Python Program to Convert Bytes to a String

```py
byte_data = b'Hello, World!'
print(type(byte_data))

string_data = byte_data.decode('utf-8')
print(type(string_data))

value = bytes("ashish".encode())

print(value, type(value))
```
