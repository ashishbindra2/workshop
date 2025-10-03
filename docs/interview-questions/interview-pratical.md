# INTERVIEW QUESTION

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
