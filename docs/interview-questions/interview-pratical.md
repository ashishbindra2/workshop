# INTERVIEW QUESTION

## Coding Questions

### 1. Generate an infinite Fibonacci series using a generator

```py
def fib():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

f = fib()
for i in range(1, 10):
    print(next(f))
```

for upto given number then use this

```py
def fib(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

for num in fib(10):
    print(num)
```

### 2. Sort a list without using the keyword Sort

### 🧩 Code 1 — Your First Example

```python
l = [6,5,4,3,32,1]
for i in range(len(l)):
    for j in range(i+1, len(l)):
        if l[i] > l[j]:
            l[i], l[j] = l[j], l[i]
print(l)
```

🔍 What it does

This is basically a **Selection Sort** implementation (you select the smallest element and put it at the front).

### 🕒 Time Complexity

| Case    | Complexity |
| :------ | :--------- |
| Best    | **O(n²)**  |
| Average | **O(n²)**  |
| Worst   | **O(n²)**  |

### 💾 Space Complexity

* **O(1)** (in-place)
💡 Reason

For every element `i`, it compares with all elements after it (`j`), hence about `n*(n-1)/2` comparisons → **O(n²)**.

---

### 🧼 Code 2 — Bubble Sort

```python
def bubble_sort(lst):
    n = len(lst)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
    return lst
```

### 🔍 How it works

It “bubbles” the largest element to the end in each iteration.

### 🕒 Time Complexity

| Case    | Complexity                                  |
| :------ | :------------------------------------------ |
| Best    | **O(n)** (if optimized with a swapped flag) |
| Average | **O(n²)**                                   |
| Worst   | **O(n²)**                                   |

### 💾 Space Complexity

* **O(1)** (in-place)

### 💡 Reason

Each element may need to be compared with every other, so ~n² comparisons.

---

### 🧮 Code 3 — Selection Sort (While Loop)

```python
def selection_sort(lst):
    sorted_list = []
    while lst:
        min_val = min(lst)
        sorted_list.append(min_val)
        lst.remove(min_val)
    return sorted_list
```

### 🔍 How it works

Repeatedly finds the minimum and appends it to a new list.

### 🕒 Time Complexity

| Case    | Complexity |
| :------ | :--------- |
| Best    | **O(n²)**  |
| Average | **O(n²)**  |
| Worst   | **O(n²)**  |

### 💾 Space Complexity

* **O(n)** (creates a new list)

### 💡 Reason

Each `min(lst)` takes O(n), and you do it n times → **n × n = n²**.

---

### ⚡ Code 4 — Quick Sort (Recursive)

```python
def quick_sort(lst):
    if len(lst) <= 1:
        return lst
    pivot = lst[0]
    left = [x for x in lst[1:] if x < pivot]
    right = [x for x in lst[1:] if x >= pivot]
    return quick_sort(left) + [pivot] + quick_sort(right)
```

### 🔍 How it works

Divide and conquer — pick a pivot, partition the list, recursively sort both sides.

### 🕒 Time Complexity

| Case    | Complexity                                                |
| :------ | :-------------------------------------------------------- |
| Best    | **O(n log n)**                                            |
| Average | **O(n log n)**                                            |
| Worst   | **O(n²)** (when pivot is always smallest/largest element) |

### 💾 Space Complexity

* **O(log n)** (recursion stack)

### 💡 Reason

Splitting into two roughly equal halves gives log n levels of recursion, each doing O(n) work.

---

### ⚙️ Code 5 — Heap Sort (Using `heapq`)

```python
import heapq

nums = [4, 1, 7, 3, 8, 5]
heapq.heapify(nums)
sorted_nums = [heapq.heappop(nums) for _ in range(len(nums))]
print(sorted_nums)
```

### 🔍 How it works

* Converts list into a **heap** in O(n)
* Pops elements one by one (each pop = O(log n))

### 🕒 Time Complexity

| Case    | Complexity     |
| :------ | :------------- |
| Best    | **O(n log n)** |
| Average | **O(n log n)** |
| Worst   | **O(n log n)** |

### 💾 Space Complexity

* **O(n)** (creates a new list for result)

---

### 🧠 Summary Table

| Algorithm                       |    Best    |   Average  |    Worst   |   Space  | Stable? | In-place? |     Technique    |
| :------------------------------ | :--------: | :--------: | :--------: | :------: | :-----: | :-------: | :--------------: |
| **Selection Sort (Your first)** |    O(n²)   |    O(n²)   |    O(n²)   |   O(1)   |    ❌    |     ✅     |    Comparison    |
| **Bubble Sort**                 |    O(n)    |    O(n²)   |    O(n²)   |   O(1)   |    ✅    |     ✅     |    Comparison    |
| **Selection Sort (while)**      |    O(n²)   |    O(n²)   |    O(n²)   |   O(n)   |    ❌    |     ❌     |    Comparison    |
| **Quick Sort**                  | O(n log n) | O(n log n) |    O(n²)   | O(log n) |    ❌    |     ✅     | Divide & Conquer |
| **Heap Sort**                   | O(n log n) | O(n log n) | O(n log n) |   O(n)   |    ❌    |     ❌     |    Heap-based    |
| **Merge Sort**                  | O(n log n) | O(n log n) | O(n log n) |   O(n)   |    ✅    |     ❌     | Divide & Conquer |

---

### 🏆 Which One is Best?

| Situation                                          | Best Choice                                     | Reason                |
| :------------------------------------------------- | :---------------------------------------------- | :-------------------- |
| Small dataset (learning purpose)                   | **Bubble / Selection**                          | Simple to understand  |
| Large, random dataset                              | **Quick Sort**                                  | Fast average case     |
| Guaranteed performance (no worst-case risk)        | **Heap Sort**                                   | O(n log n) always     |
| Stability required (preserve equal elements order) | **Merge Sort** *(not listed but best for this)* | Stable and O(n log n) |

---

| Scenario                               | Recommended Algorithm       | Why                                     |
| :------------------------------------- | :-------------------------- | :-------------------------------------- |
| **General purpose sorting (balanced)** | **Merge Sort**              | Always O(n log n), stable               |
| **Performance critical, random data**  | **Quick Sort**              | Fastest average case (best cache usage) |
| **Guaranteed worst-case performance**  | **Heap Sort**               | Always O(n log n), no recursion         |
| **Simple learning / small data**       | **Bubble / Selection Sort** | Easy to understand                      |

### 📘 Quick Summary of “How to Find Complexity”

1. **Count nested loops:**

   * 2 nested → O(n²)
2. **Divide & conquer (recursion):**

   * Splits list → O(n log n)
3. **Loop inside recursion:**

   * Multiply work per level by number of levels.
4. **Constant extra memory?**

   * → O(1)
     Otherwise, count new lists → O(n)

---

### 3. Check whether a string is palindrome or not?

```py
s = "ashihsa"

print("Is a Palindrome") if(s == s[::-1]) else print("No")

s = "ashihsaa"

# Alternative way
flag = True
for  i,w in enumerate(s,start=1):
    if w != s[len(s) - i]:
        print("No")
        flag = False
        break

if flag:
    print("Is a Palindrome")
```

Using a Loop (Manual Check)

```py
s = "racecar"
is_palindrome = True

for i in range(len(s)//2):
    if s[i] != s[-(i+1)]:
        is_palindrome = False
        break

print("Palindrome" if is_palindrome else "Not Palindrome")
```

Using Recursion

```py
def is_palindrome(s):
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    return is_palindrome(s[1:-1])

s = "level"
print("Palindrome" if is_palindrome(s) else "Not Palindrome")
```

Ignore Case & Spaces (Clean Input First)

```py
def clean_string(s):
    return ''.join(ch.lower() for ch in s if ch.isalnum())

def is_palindrome(s):
    s = clean_string(s)
    return s == s[::-1]

s = "A man, a plan, a canal: Panama"
print("Palindrome" if is_palindrome(s) else "Not Palindrome")
```

### 4. Sort a dictionary/ dict comprehension

```py
d = {4:"asd",3:"sd",2:"sds",1:"sd"}
data = {'apple': 3, 'banana': 1, 'cherry': 2}

d2 = {}
for i in sorted(d):
    d2[i] = d[i]

print(d2)

# comprehension 
sorted_dict = {k: d[k] for k in sorted(d)}
print(sorted_dict)
```

Sort by Values (Ascending Order)

```py
sorted_dict = {k: v for k, v in sorted(data.items(), key=lambda item: item[1])}
print(sorted_dict)
```

### 5. Find the pair with a given number in a list. two elements sum to the given number

```py
list1 = [1,2,3,4,5,6,7,8,9]
k = 10

for i in range(len(list1)):
    for j in range(i+1,len(list1)):
        if list1[i] + list1[j] == k:
            print(list1[i],list1[j])
```

### 6. Create a Fibonacci series using recursion

```py
def fib(n):
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)


print(fib(10))
```

### 7. String manipulation. "The Sky is Blue" to "Blue is The Sky"

```py
s = "The Sky is Blue"
o = "Blue is The Sky"

v = ""
for i in s.split():
    v = i + "_" + v
print(v[: len(v) - 1])

# 2nd Way
l = s.split()
l = l[::-1]
l = " ".join(l)
print(l)
```

'/*apples are & found% only @red & green'

```py
s = ''

for i in v:
    if((i>='A' and i <='Z') | (i>='a' and i <= 'z') | (i==' ')):
        s = s + i
print(s)
```

### 8. Find the maximum repeated character in a string without having o(n2) complexity

```py
s = "asdafdfbvnonwvjsdnvosdnvdsnoidn"

ch = {}
for i in s:
    ch[i] = ch.get(i,0) + 1

print(ch)

print(max(ch,key=ch.get))
```

### 9. Find a maximum and minimum value in a List without using any predefined function

```py

l = [111, 22, 44, 5, 6, 23, 45, 56, 67]

maxi: int = l[0]
mini: int = l[0]
for i in l:
    if i > maxi:
        maxi = i
    if mini > i:
        mini = i

print(maxi, mini)
```

### 10. Write a code to raise an exception

```py
l = [1,2,3,4,5,6]
sum = 0

for i in l:
    if i==3:
        raise Exception("Exception: 0 is found")
    else:
        sum+=1
```

1.Palindrome
2.Fibonacci Series
3.Compress String
4.FizzBuzz
5.Character Occurrence
6.Prime Number

### 7.Modify String Format

```
Input = I_Am_Coder
Output = i.aM.cODER

_ = .
```

```py
s = 'I_Am_Coder'

print(s.swapcase().replace("_","."))
```

```py
s = 'I_Am_Coder'

# print(s.swapcase().replace("_","."))
l = []
for i in s.split('_'):
    l.append(i.capitalize().swapcase()) # l.append(i[0].lower() + i[1:].upper())
print(".".join(l))
    
```

8.Second Largest Number
9.Armstrong Number
10.Factorial

### FizzBuzz

```
If number divisible by 3 - print Fizz
If number divisible by 5 - print Buzz
If number divisible by 15 - print FizzBuzz

else print number

o/p
1 2 fizz 4 5 Buzz 15 FizzBuzz
 
```

## Write a Python program to check whether the given input is an Armstrong number

## Write a Python program to print a list of primes in a given range

## Write a program to reverse a list using Enumerate in Python

## Write a program in Python to execute the Bubble sort algorithm

## . Write an async function that fetches data from multiple URLs concurrently

## Write a Python program to count the total number of lines in a text file

## Write a program in Python to check if a number is prime

## Write a program in Python to produce a Star triangle

## Write a program to produce the Fibonacci series in Python

## Write a program in Python to find the largest and second-largest element in a list using Python

## How to remove values from a Python array?

## Write a program to check even and odd numbers using shorthand if-else statements

## Write a Python program that will reverse a string without using the slicing operation or reverse() function

```py
# Defining the function
def reverseString(x):
    # Declaring an empty string
    NewString = ""
    # Traversing through individual characters in the string
    for i in x:
        # Add the character to the beginning of the new string
        NewString = i + NewString
    # Return the new string
    return NewString

# Sample string
string = "Intellipaat"

# Function call
ReversedString = reverseString(string)

# Printing output
print("Reversed String:", ReversedString)

```

## What is the easiest way to calculate percentiles when using Python?

```py
import numpy as np

a = np.array([1, 2, 3, 4, 5, 6, 7])
p = np.percentile(a, 50) # Returns the 50th percentile, which is also the median
print(p)

```

## basically checks if both are in the same mood (both angry or both not angry)

```py
def friends_in_trouble(j_angry, s_angry):
    return j_angry == s_angry
```

2. Using XOR (exclusive or)

```py
def friends_in_trouble(j_angry, s_angry):
    return not (j_angry ^ s_angry)
```

## convert list to pandas dataframe

```py
import pandas as pd

# Example 1: List of values
data = [10, 20, 30, 40]

df = pd.DataFrame(data, columns=['Numbers'])
print(df)



## Write a program to find the greater of the two numbers

## **1. Count Unique Words in Sentences**  

**Problem:**  
Given a list of sentences, return a dictionary where each key is a sentence, and the value is the number of unique words in that sentence.  

**Example Input:**  

```python
sentences = [
    "hello world hello",
    "python is fun",
    "fastapi is fast and efficient"
]
```  

**Expected Output:**  

```python
{
    "hello world hello": 2,
    "python is fun": 3,
    "fastapi is fast and efficient": 5
}
```

sol

```py
sentences = [
    "hello world hello",
    "python is fun",
    "fastapi is fast and efficient"
]

d = {}
for sen in sentences:
    temp_word = []
    for word in sen.split():
        if word not in temp_word:
            temp_word.append(word)
            d[sen] = d.get(sen,0)+1
    print(temp_word)
print(d)
```

    ['hello', 'world']
    ['python', 'is', 'fun']
    ['fastapi', 'is', 'fast', 'and', 'efficient']
    {'hello world hello': 2,
    'python is fun': 3,
    'fastapi is fast and efficient': 5}

---

## **2. Extract Domains from Emails**  

**Problem:**  
Given a list of email addresses, return a set containing only the unique domains.  

**Example Input:**  

```python
emails = ["alice@example.com", "bob@gmail.com", "charlie@example.com", "dave@yahoo.com"]
```  

**Expected Output:**  

```python
{"example.com", "gmail.com", "yahoo.com"}
```

---

```py
emails = ["alice@example.com", "bob@gmail.com", "charlie@example.com", "dave@yahoo.com"]
set(emails)
```

---

## **3. Group Words by First Letter**  

**Problem:**  
Given a list of words, return a dictionary where each key is the first letter of a word, and the value is a list of words that start with that letter.  

**Example Input:**  

```python
words = ["apple", "banana", "cherry", "avocado", "blueberry", "carrot"]
```  

**Expected Output:**  

```python
{
    "a": ["apple", "avocado"],
    "b": ["banana", "blueberry"],
    "c": ["cherry", "carrot"]
}
```

```py
words = ["apple", "banana", "cherry", "avocado", "blueberry", "carrot"]

dict_letter = {}
for word in words:
    a = word[0]
    dsave:list =  dict_letter.get(a,[])
    dsave.append(word) 
    dict_letter[a] =dsave
dict_letter
```

```yaml
{
 'a': ['apple', 'avocado'],
 'b': ['banana', 'blueberry'],
 'c': ['cherry', 'carrot']
}
```

```py
from collections import defaultdict

dict_letter = defaultdict(list)  # Initialize with list as default value type
for word in words:
    dict_letter[word[0).append(word)

dict_letter
```

## **4. Count Occurrences of Digits in Numbers**  

**Problem:**  
Given a list of integers, return a dictionary where each key is a digit (0-9), and the value is how many times that digit appears across all numbers.  

**Example Input:**  

```python
numbers = [101, 232, 345, 566, 789]
```  

**Expected Output:**  

```python
{
    "0": 1,
    "1": 2,
    "2": 2,
    "3": 2,
    "4": 1,
    "5": 2,
    "6": 2,
    "7": 1,
    "8": 1,
    "9": 1
}
```

```py
numbers = [101, 232, 345, 566, 789]
from collections import Counter

c =Counter(numbers)
c
```

```py
numbers = [101, 232, 345, 566, 789]
number_counter: dict = {}

type(number_counter)
```

```py
for number in numbers:
    number_counter[number] = number_counter.get(number, 0) + 1

number_counter
```

## **5. Filter Names by Length**  

**Problem:**  
Given a list of names and an integer `n`, return a list of names that have more than `n` characters.  

**Example Input:**  

```python
names = ["Alice", "Bob", "Catherine", "David"]
n = 4
```  

**Expected Output:**  

```python
["Alice", "Catherine", "David"]
```

---

```py
names = ["Alice", "Bob", "Catherine", "David"]
n = int(input("enter number"))
new_names  = []
for name in names:
    if len(name) >= n:
        new_names.append(name)
new_names
```

['Alice', 'Catherine', 'David']

## **6. Group Numbers by Even and Odd**  

**Problem:**  
Given a list of numbers, return a dictionary with two keys: `"even"` and `"odd"`, where the values are lists containing the respective numbers.  

**Example Input:**  

```python
numbers = [1, 2, 3, 4, 5, 6]
```  

**Expected Output:**  

```python
{
    "even": [2, 4, 6],
    "odd": [1, 3, 5]
}
```

```py
numbers = [1, 2, 3, 4, 5, 6]

odd_even = {"even":[],"odd":[]}

for number in numbers:
    if number % 2 ==0:
        odd_even["even"].append(number)
    else:
        odd_even["odd"].append(number)
odd_even
```

```
{
    "even": numbers%2==0,
    "odd": [1, 3, 5]
}
```

---

---

### **7. Reverse Key-Value Pairs in a Dictionary**  

**Problem:**  
Given a dictionary, return a new dictionary where keys become values and values become keys. Assume values are unique.  

**Example Input:**  

```python
data = {"apple": "fruit", "carrot": "vegetable", "salmon": "fish"}
```  

**Expected Output:**  

```python
{
    "fruit": "apple",
    "vegetable": "carrot",
    "fish": "salmon"
}
```

---

### **8. Find the Most Frequent Character in a String**  

**Problem:**  
Given a string, return the character that appears the most times. If multiple characters have the same frequency, return any of them.  

**Example Input:**  

```python
text = "banana"
```  

**Expected Output:**  

```python
"a"
```

or  

```python
"n"
```

---

### **9. Convert a List of Tuples into a Dictionary**  

**Problem:**  
Given a list of tuples, where each tuple contains two elements `(key, value)`, return a dictionary mapping keys to values.  

**Example Input:**  

```python
pairs = [("a", 1), ("b", 2), ("c", 3)]
```  

**Expected Output:**  

```python
{
    "a": 1,
    "b": 2,
    "c": 3
}
```

---

## **10. Merge Two Dictionaries with Summed Values**  

**Problem:**  
Given two dictionaries with integer values, merge them into a single dictionary where the values for duplicate keys are summed.  

**Example Input:**  

```python
dict1 = {"a": 1, "b": 2, "c": 3}
dict2 = {"b": 3, "c": 4, "d": 5}
```  

**Expected Output:**  

```python
{
    "a": 1,
    "b": 5,
    "c": 7,
    "d": 5
}
```

---

---

## Here are the solutions for each problem  

### 1. Count Unique Words in Sentences

```python
def count_unique_words(sentences):
    return {s: len(set(s.split())) for s in sentences}

sentences = [
    "hello world hello",
    "python is fun",
    "fastapi is fast and efficient"
]
print(count_unique_words(sentences))
```

---

### **2. Extract Domains from Emails**

```python
def extract_domains(emails):
    return {email.split('@')[1] for email in emails}

emails = ["alice@example.com", "bob@gmail.com", "charlie@example.com", "dave@yahoo.com"]
print(extract_domains(emails))
```

---

### **3. Group Words by First Letter**

```python
from collections import defaultdict

def group_words_by_first_letter(words):
    result = defaultdict(list)
    for word in words:
        result[word[0]].append(word)
    return dict(result)

words = ["apple", "banana", "cherry", "avocado", "blueberry", "carrot"]
print(group_words_by_first_letter(words))
```

---

### **4. Count Occurrences of Digits in Numbers**

```python
from collections import Counter

def count_digit_occurrences(numbers):
    all_digits = ''.join(map(str, numbers))
    return dict(Counter(all_digits))

numbers = [101, 232, 345, 566, 789]
print(count_digit_occurrences(numbers))
```

---

### **5. Filter Names by Length**

```python
def filter_names_by_length(names, n):
    return [name for name in names if len(name) > n]

names = ["Alice", "Bob", "Catherine", "David"]
n = 4
print(filter_names_by_length(names, n))
```

---

### **6. Group Numbers by Even and Odd**

```python
def group_even_odd(numbers):
    return {
        "even": [num for num in numbers if num % 2 == 0],
        "odd": [num for num in numbers if num % 2 != 0]
    }

numbers = [1, 2, 3, 4, 5, 6]
print(group_even_odd(numbers))
```

---

### **7. Reverse Key-Value Pairs in a Dictionary**

```python
def reverse_dict(d):
    return {v: k for k, v in d.items()}

data = {"apple": "fruit", "carrot": "vegetable", "salmon": "fish"}
print(reverse_dict(data))
```

---

### **8. Find the Most Frequent Character in a String**

```python
from collections import Counter

def most_frequent_char(text):
    return Counter(text).most_common(1)[0][0]

text = "banana"
print(most_frequent_char(text))
```

---

### **9. Convert a List of Tuples into a Dictionary**

```python
def convert_to_dict(pairs):
    return dict(pairs)

pairs = [("a", 1), ("b", 2), ("c", 3)]
print(convert_to_dict(pairs))
```

---

### **10. Merge Two Dictionaries with Summed Values**

```python
from collections import Counter

def merge_dicts(dict1, dict2):
    return dict(Counter(dict1) + Counter(dict2))

dict1 = {"a": 1, "b": 2, "c": 3}
dict2 = {"b": 3, "c": 4, "d": 5}
print(merge_dicts(dict1, dict2))
```

---

Let me know if you need explanations or modifications! 🚀
