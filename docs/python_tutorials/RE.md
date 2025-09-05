# Regular Expression

- If you want to represent a group of string according to a particular format/pattern, then we should go for Regular Expression.
- i.e Regular Expression is a declaration  mechanism to represent a group of strings according to a perticulat format / pattern.

## EXAMPLES

### Q1. Write a regular expression to represent all mobile numbers

- `[6-9][0-9]{9}`

### Q2. Write a regular expression to represent all mail ids

- ``

## Application areas of Regular Expression

1. Pattern Matching Applications
    - Ctrl+f => In window
    - grep => Linux
2. To perform validations / To develop validation frameworks.
3. To develop translators like complier, interpreter, assembler etc.
    - compiler design
        - lexical Analysis
        - syntax Analysis
        - sematic Analysis
        - Intermediate code Generator
        - code Optimiztion
        - Target code Generator
4. To develop digital circuts like incrementer
5. To develop communicator protocol TCP/IP,UDP,HTTP etc.

re => module ( several functions) (java.util.regex package)

## Methods

### 1. compile()

Returns Module contains compile() Function to compile a Pattern into RegexObject.

`pattern = re.compile("ab")`

### Patteren Matching Application

Search pattern: ab
target string: abaabababa
0,3,5, =>ab
total => 3 times

```py
import re
- Compiler String into pattern object
- Convert string into patteren object

pattern = re.compile('ab')

Return iterator to find pattern in the target
matcher = pattern.finditer('abaabababa') # one by one
matcher

count = 0
for match in matcher:
    print(match.start())
    count+=1

print(f'The Number of occurence: {count}')

# ouput
# 0
# 3
# 5
# 7
```

matcher

- ***Start()*** => returns start index of the match
- **end()** => return end + 1 index of the match
- **group()** => return matched string

### Character classes

We can use character classes to search a group of charaters

- **[abc]** => a or b or c
- **[^abc]** => Expect a and b and c
- **[a-z]** => any lower case alphabet symbol
- **[A-Z]** => Any Uppercase alphabet symbol
- **[a-zA-Z]** => Any alphabet symbol
- **[0-9]** => Any digit
- **[0-9a-zA-Z]** => Any alphanumeric character (Special character)
- **[^0-9a-zA-Z]** = > Except alphanumeric character (Special character)

###

- Any digit 0 to 9
- ('\d) => short cut

### Predifinded character classes

- \d => Any digit 0 to 9 [0-9]
- \D => Any character except digit [^0-9]
- \w => Any Word character [0-9a-zA-Z]
- \W => Any character except alphanumeric character (special character)
- \s => Sppecial character
- \S => Except space character
- . => Any character including special character also

```py title="
import re
matcher = re.finditer(' ','abb7@k 9 yYz')

count= 0
for match in matcher:
    print(f'{match.start()}........{match.group()}')
    count= count+1

print(f"The number of occurences: {count}")
# 6........ 
# 8........ 
# The number of occurences: 2
```

### Quantifiers

We can use quantifiers to specifig the number of occurences to match

- a => exactly one 'a'
- a+ => AtlEAST One 'a'
- a* => rv = r+ U {E} any number of a's including zero number
- a? => Atmost one a
- a{m} => Exactly m number of a
- a{m,n} => minimum m number of a's and maximium n number of a's

### Important function of re module

1. match()
2. fullmatch()
3. search()
4. findall()
5. finditer()
6. sub()
7. subn()
8. split()
9. compile()

#### 1. match()

- We can use match() function to check wheater the given pattern present at beginning of the target string or not?
- If match is available then we will get match object, otherwise we will get None.

```py title=""
import re

p = input("Enter patter to check!!! ")
m = re.match(p,'abcdefgh')

if m is not None:
    print(f"Target string with {m.group()}")
else:
    print(f"Target string not start with {p}")


# Enter patter to check!!!  abc
# Target string with abc
```

```py title=""
import re

p = input("Enter patter to check!!! ")
m = re.match(p,'abcdefgh')

if m:
    print(f"Target string with {m.group()}")
else:
    print(f"Target string not start with {p}")

# Enter patter to check!!! ashish
# Target string not start with ashish
```

```py title=""
import re

p = input("Enter patter to check!!! ")
m = re.match(p,'abcdefgh')

if m:
    print(f"Target string with {m.group()}")
else:
    print(f"Target string not start with {p}")
```

#### 2. Fullmatch()

- We can use fullmatch() function to check wheather total target string matched with given patteren or not
- If matched then we will gett match object otheruse we will get None.
- `m = re.fullmatch(p,"abcdefgh")`

```py title=""
import re

num = input("Enter Mobile Number to validate:!")
# patteren = "[6-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9]"
patteren = "[6-9][0-9]{9}"

match = re.fullmatch(patteren,num)

if match:
    print("valid 10 - digit mobile numder")
else:
    print("Invalid 10 - digit mobile number")


# Enter Mobile Number to validate:! 9815039236
# valid 10 - digit mobile numder

# Enter Mobile Number to validate:! 1234567891
# Invalid 10 - digit mobile number
```

#### 4. findall()

- To find all occurrences of the match
- This function returns list object which contains all occurrences.

```py title=""
import re

l = re.findall('[0-9]', 'a7b9k2@5kmn4')
print(l)

# ['7', '9', '2', '5', '4']
```

#### 5. finditer()

- Return iterator yielding a matching object for each match
- On match object, we can call start(), end(), group() matches()

```py title=""
import re

matcher = re.finditer('[0-9]',"a7b9k2@skmn4")
for match in matcher:
    print(f"{match.start()}.....{match.group()}")

# 1.....7
# 3.....9
# 5.....2
# 11.....4
```

#### 6. sub()

- sub means substitution or replacement.
- `re.sub('pattern, replacement_string, target_string')`

```py
import re

s = re.sub('[0-9]','#','a7b9kz@5kmn4')
s
'a#b#kz@#kmn#'
```

#### 7. subn()

- It is exactly same as sub() except that it can also returns the number of replacements.
- Return type is touple
  - (result string, number of replacements)

```py
import re

t = re.subn('[0-9]','#','a7b9kz@5kmn4')

print(t)
print('The Result string',t[0])
print('The number of replacement',t[1])

# ('a#b#kz@#kmn#', 4)
# The Result string a#b#kz@#kmn#
# The number of replacement 4
```

#### 8. split()

We can use split() function to split target string acc to the pattern

```py title=""
import re

l = re.split('-','27-11-2020')
print(l)

for s in l:
    print(s)


# ['27', '11', '2020']
# 27
# 11
# 2020
```

1. **match()** = > To check wheather the given target string start with specificed pattern or not
2. **fullmatch()** = > To check wheather total string matched patteren or not
3. **Search()** = > To retuen first occurrence of the match
4. **findall()** = > To return all matches
5. **finditer()** = > To return iterator object which yields match object
6. **sub()** = > To replace every occurence of the patteren with provided replacement string
7. **subn()** = > Same as sub() but also returns the number of occurences
8. **split()** = > To split the target string on given patteren

#### ^ symbol and $ symbol

- `^` symbol = start with
- `re.search('[^ab],target string')` ==> not
- `re.search('^ab,target string')` ==> start with

``` py
import re
match = re.search('^learn','learn python is very easy!!')

if match is not None:
    print('Target string start with our pattern')
else:
    print("Taerget string not start with out patteren")
```

#### $ symbol

`$` means end with

```py
import re

match = re.search('easy$',"learn python is very easy")

if match:
    print('Target string end with our pattern')
else:
    print("Taerget string not end with out patteren")
```

```py
import re

match = re.search('Easy$',"learn python is very easy")

if match:
    print('Target string end with our pattern')
else:
    print("Taerget string not end with out patteren")
```

```py
import re

match = re.search('EASY$',"learn python is very easy",re.IGNORECASE)

if match:
    print('Target string end with our pattern')
else:
    print("Taerget string not end with out patteren")
```

#### Write a Regular Expression to represent all YAVA lang identifier?

***Rule:***

1. The allowed charaters are a-z,A-Z,0-9,#
2. The first character should be lowercase alphabet symbol from a to k
3. the scond character shoild be a digit divisible by 3
4. The length of identifier should be atkeast 2
a9cd#3

- `[a-k][0369][a-zA-Z0-9#]*`
- `[a-zA-Z0-9#]*` = > We can take character any number of time including zero times also
- `+=` > We can take character alteast once
- `?` => atmost once (either onetime pr zerotimes)

```py
import re

target = input("Enter any identifier to check ")

pattern = "[a-k][0369][a-zA-Z0-9#]*"
match = re.fullmatch(pattern,target)

if match:
    print("valid identifier ")
    
else:
    print("Invlid identifer ")
```

### 3 Write a regular expression to represent all 10 digit mobile numbers

1. The number should contains exactly 10 digits
2. The first should be from 6 to 9 only.

- `[6-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9]`
- `[6-9][0-9]{9} | 0[6-9][0-9]{9} | 91[6-9][0-9]{9}`
- `(091)? [6-9][0-9]{9}`

### WAP to extract all mobile numbers present in input.txt where numbers are mixed with normal text data?

```py
import re

f1 = open('input.txt', 'r')
f2 = open('mobile_number.txt','w')

pattern = '(0 | 91)?[6-9][0-9]{9}'

for line in f1:
    matcher = re.finditer(pattern,line)
    
    for match in matcher:
        f2.write(match.group() + '\n')
        
        
f1.close()
f2.close()

print("Extraction complete open file to see results")
```

```py title="mobile number"
import re

mobile_regex = r'\b(?:\+?91|0)?[-]?\(?[6789]\d{2}\)?[-]?\d{3}[-]?\d{4}\b'

with open('input.txt', 'r') as file:
    data = file.read()
    # Find all matches of mobile numbers in the data
    mobile_numbers = re.findall(mobile_regex, data)

# Print the extracted mobile numbers
for number in mobile_numbers:
    print(number)

print("Extraction complete. Open file to see results.")
```

#### WAP to check wheather given car registration number is valid Telangana state registration Number or Not?

```py title="Chical registration"
import re

num = input("Enter vehicle Registration no to validate ").upper()

patteren = "TS[012][0-9][A-Z][A-Z][0-4]{4}"

matcher = re.fullmatch(patteren,num)

if matcher:
    print("Valid Vehicale Registration Number")
else:
    print("Invalid Vehicale Registration Number")
```

#### WAP to check wheater the given mail id is valid or not?

```py title="valid mail id code"
import re

num = input("Enter mail ")

patteren = "[a-zA-Z0-9][a-zA-Z0-9._]*@gmail.com"

matcher = re.fullmatch(patteren,num)

if matcher:
    print("valid mail ")
else:
    print("Invalid mail")
```

### Q sort the list using re

file_paths = [
    'static\\pdf\\01 Adsolut initiatie\\page_1.pdf',
    'static\\pdf\\01 Adsolut initiatie\\page_10.pdf',
    'static\\pdf\\01 Adsolut initiatie\\page_11.pdf',
    'static\\pdf\\01 Adsolut initiatie\\page_12.pdf',
    'static\\pdf\\01 Adsolut initiatie\\page_13.pdf',
    'static\\pdf\\01 Adsolut initiatie\\page_14.pdf',
    'static\\pdf\\01 Adsolut initiatie\\page_15.pdf',
    'static\\pdf\\01 Adsolut initiatie\\page_16.pdf',
    'static\\pdf\\01 Adsolut initiatie\\page_17.pdf',
    'static\\pdf\\01 Adsolut initiatie\\page_18.pdf',
    'static\\pdf\\01 Adsolut initiatie\\page_19.pdf',
    'static\\pdf\\01 Adsolut initiatie\\page_2.pdf',
    'static\\pdf\\01 Adsolut initiatie\\page_20.pdf',
    'static\\pdf\\01 Adsolut initiatie\\page_21.pdf',
    'static\\pdf\\01 Adsolut initiatie\\page_22.pdf',
    'static\\pdf\\01 Adsolut initiatie\\page_23.pdf',
    'static\\pdf\\01 Adsolut initiatie\\page_24.pdf',
    'static\\pdf\\01 Adsolut initiatie\\page_25.pdf',
    'static\\pdf\\01 Adsolut initiatie\\page_26.pdf',
    'static\\pdf\\01 Adsolut initiatie\\page_27.pdf',
    'static\\pdf\\01 Adsolut initiatie\\page_28.pdf',
    'static\\pdf\\01 Adsolut initiatie\\page_29.pdf',
    'static\\pdf\\01 Adsolut initiatie\\page_3.pdf',
    'static\\pdf\\01 Adsolut initiatie\\page_30.pdf',
    'static\\pdf\\01 Adsolut initiatie\\page_4.pdf',
    'static\\pdf\\01 Adsolut initiatie\\page_5.pdf',
    'static\\pdf\\01 Adsolut initiatie\\page_6.pdf',
    'static\\pdf\\01 Adsolut initiatie\\page_7.pdf',
    'static\\pdf\\01 Adsolut initiatie\\page_8.pdf',
    'static\\pdf\\01 Adsolut initiatie\\page_9.pdf'
]

```py title="todo shorting"
```

```py title="remove more then one space"
import re

def split_by_spaces(text):
    # Use regex to split by one or more spaces
    split_text = re.split(r'\s+', text.strip())  # Strip leading/trailing whitespace
    return split_text

# Example usage
original_text = "This   is  an example    string with  multiple spaces."
split_result = split_by_spaces(original_text)

print(f"Original Text: '{original_text}'")
print(f"Split Result: {split_result}")

# Original Text: 'This   is  an example    string with  multiple spaces.'
# Split Result: ['This', 'is', 'an', 'example', 'string', 'with', 'multiple', 'spaces.'
```

#### Program to find Only digit Numbers

```py title="Only digit allowed program"
import re

def remove_str_special_char(strings: str):
    l = re.findall(r'\d', strings)
    print(l)

remove_str_special_char("a7b9k2@5kmn4")
def remove_str_special_char_0(strings: str):
    l = re.findall(r'\D', strings)
    print(l)

remove_str_special_char_0("a7b9k2@5kmn4")
def remove_str_special_char_1(strings: str):
    matcher = re.finditer('[0-9]',strings)
    for match in matcher:
        print(f"{match.group()}")

remove_str_special_char_1("a7b9k2@skmn4")


def extract_digits(strings: str):
    # Remove all non-digit characters and keep only the digits
    digits = re.sub(r'\D', '', strings)
    print(digits)

extract_digits("a7b9k2@5kmn4")

```
