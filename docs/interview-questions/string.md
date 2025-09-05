# String

## List of Programs

Q1. Write a Program To REVERSE content of the given String by using slice operator?

- input: ashish
- output: hsihsa

```py
s = input('Enter Some String to Reverse:')
output = s[::-1]
print(output)
s ="ashish" #read -ve indexing then do

# print(s[:-7:-1])

print(s[5:1:-1])
```

if step value is zero are you moving forword or backword

Q2. Write a Program To REVERSE content of the given String by using reversed() function?

```py
s = input("Enter Some String to Reverse:")
r = reversed(s)
print(r)

s = input("Enter Some String to Reverse:")
r = reversed(s)
print(r) # we are getting reversed object

output= ''.join(r)
print(output)

s = input("Enter Some String to Reverse:")
r = reversed(s)

for v in r:
    print(v,end='')
```

***Q3. Write a Program to REVERSE content of given String By uing while loop?***

```py
s = input("Enter Some String to Reverse:")
output=''
n = len(s)-1
while(n>-1):
    output = output+s[n]
    n-=1
print(output)
```

***Q4. Write a Program to REVERSE order of words present in the given String?***

```py
s = input("Enter Some String to Reverse:")
l = s.split()
l1=l[::-1]
output = ' '.join(l1)
print(output)
```

***Q5. Write a Program to REVERSE internal contentvof each word?***

```py
s = input("Enter Some String to Reverse:")
l = s.split()
l1 = []
for word in l:
    l1.append(word[::py-1])
output = ' '.join(l1)
print(output)
```

***Q6. Write a Program to REVERSE internal contentv of every second word present int the given string?***

```py

s = input("Enter Some String to Reverse:")
l = s.split()
l1 = []
i=0
while i<len(l):
    if i%2 == 0:
        l1.append(l[i])
    else:
        l1.append(l[i][::-1])
    i+=1
output = ' '.join(l1)
print(output)
```

```py

s = "ashish bindra"
l = s.split()
l1=[]
for i,word in enumerate(l):
    if i%2==1:
        l1.append(l[i][::-1])
    else:
        l1.append(l[i])
print(l1)
```

```py

s = "ashish bindra"
l = s.split()
l1=[l[i][::-1] if i%2==1 else l[i] for i,word in enumerate(l)]
l1
```

***Q7. Write a Program to print the character present at even and odd index seperatly for givern string ?***

# 1 st way

```py

s = input("Enter Some String to Reverse:")
print('Character present at even index:')
i=0
while i<len(s):
    print(s[i])
    i+=2
print('Charater present at Odd Index:')
i=1
while i<len(s):
    print(s[i])
    i+=2
```

```py
# 2nd way
s = input("Enter Some String to Reverse:")
print('Character present at Even Index:',s[0::2])
print('Character present at Even Index:',s[::2])
print('Character present at odd Index:',s[1::2])
```

***Q8. Write a Program to merge charaters of 2 strings inti a single string by taking charater alternatively ?***

```py
# if strings are having same length

s1 = "RAVI"
s2 = "TEJA"
output=''
i,j=0,0
while i<len(s1) or j<len(s2):
    output = output + s1[i]+s2[j]
    i+=1
    j+=1
print(output)
```

Note : The above program can work if the lengths of 2 strings are same.

```py

# if strings are having different length

s1 = input('Enter First String: ')
s2 = input('Enter Second String: ')
output=''
i,j=0,0
while i<len(s1) or j<len(s2):
    if i<len(s1):
        output = output + s1[i]
        i+=1
    if j<len(s2):
        output = output + s2[j]
        j+=1
print(output)
```

***Q9. Write a Program to sort charaters of the strings, first alphabet symbols followed by digits?***

- input: B4A1D3
- output: ABD134

```py

s = 'B4A1D3'
alphabets = []
digits = []
for ch in s:
    if ch.isalpha():
        alphabets.append(ch)
    else:
        digits.append(ch)
output = ''.join(sorted(alphabets) + sorted(digits))
print(output)
```

```py
# -----------------
# alternative way
# -----------------
s = 'B4A1D3'
alphabets = ''
digits = ''
for ch in s:
    if ch.isalpha():
        alphabets+=ch
    else:
        digits+=ch
output = ''
for ch in sorted(alphabets):
    output=output+ch
for ch in sorted(digits):
    output=output + ch
print(output)
```

***Q10. Write a Program for the following requirment?***

- input: a4b3c2
- output: aaaabbbcc

```py

s = input('Enter some string where alphabet symbol should be followed by digit: ')
output = ''
for ch in s:
    if ch.isalpha():
        x = ch
    else:
        d = int(ch)
        output = output + x*d
print(output)
```

***Q11. WAP for the following requirment***

- input: aaaabbbccz
- output: 4a3b2c1z

```py

s = 'aaaabbbccz'
output = ''
previous = s[0]
c=1
i=1
while i<len(s):
    if s[i] == previous:
        c=c+1
    else:
        output = output+str(c)+previous
        previous = s[i]
        c = 1
    if i == len(s) - 1:
        output = output+str(c) + previous
    i = i+1
print(output)
```

```py
# s = 'aaaabbbccz'
# output = ''
# global p
# p =''
# c = 1
# for i in s
# if p == i
# c+=1
# else
# output = output + c
# p = i
# c = 1
```

***Q12. Write a Program for the following requirment?***

- input: a4k3b2
- output: aekndb
In this example the following two functions are required to use

1. ord(): To find unicode value for the given character
    eg:
    - ord('a') --> 97
2. chr(): To find corresponding character for the given unicode value
    - chr(98) --> b

```py

s = 'a4k3b2'
output = ''
for ch in s:
    if ch.isalpha():
        x= ch
        output = output + ch
    else:
        d = int(ch)
        newc = chr(ord(x) + d)
        output = output + newc
print(output)
```

***Q13. Write a program to remove duplicate characters from the given input string?***

- input: aaaavvvhhhjjj
- output: avhj

```py

# 1st way

# --------

s='AAAAZZZZZBCHGGJBBCCBHGFFCSSSFVA'
output=''

for ch in s:
    if ch not in output:
        output = output + ch
print(output)
```

```py

# 2nd way

# --------

s='AAAAZZZZZBCHGGJBBCCBHGFFCSSSFVA'
l=[]
for ch in s:
    if ch not in l:
        l.append(ch)
output = ''.join(l)
print(output)
```

```py
# 3rd way by using set (but no gurantee for the order)

s='AAAAZZZZZBCHGGJBBCCBHGFFCSSSFVA'
s1 = dict.fromkeys(s).keys()
output =''.join(s1)
print(output,type(s1))
```

***Q14. Program to find the number of occurrences of each character present in the given string with count() method***

```py

# By using cout() method and list

s='AAAAZZZZZBCHGGJBBCCBHGFFCSSSFVA'

l = []
for ch in s:
    if ch not in l:
        l.append(ch)
for ch in sorted(l):
    print(f'{ch} occurrs {s.count(ch)} times')
s = input("enter any string ")
s1 = set(s)
for ch in sorted(s1):
    print(f'{ch} occurrs {s.count(ch)} times')
```

***Q15. Program to find the number of occurrences of each character present in the given string without sing count() method***

```py

s='AAAAZZZZZBCHGGJBBCCBHGFFCSSSFVA'
d ={}

for ch in s:
    d[ch] = d.get(ch,0) + 1
for k,v in d.items():
    print(f'{k} occurrs {v} times')
print()
```

```py
# for sorting propose

for k,v in sorted(d.items()):
    print(f'{k} occurrs {v} times')
```

***Q16.Write a Program to find the number of occurrences of each vowel present in the given string?***

```py

s = input('Enter some string to search for vowels:')
v = ['a','e','i','o','u','A','E','I','O','U']
d = {}

for ch in s:
    if ch in v:
        d[ch] = d.get(ch,0) + 1
for k,v in sorted(d.items()):
    print(f'{k} occures {v} times')
```

***Q17.Write a Program to check whether the given two strings are anagrams or not?***
Two strings are said to be anagrams iff both are having same content irrespective of characters position.

e.g

- lazy and zaly
- SILENT and LISTEN
- TRIANGLE and INTEGRAL

```py

s1 = input("Enter first string: ")
s2 = input("Enter second string: ")
if(sorted(s1) == sorted(s2)):
    print("The string are anagrams.")
else:
    print("The strings are't anagrams.")
```

***Q18.Write a Program to check whether the strings is palindrome or not?***

    eg. level, malayalam, eye,..
A string is said to be palindrome iff original string and its reversed strings are equal.

```py

s = input("Enter Some string:")
if s == s[::-1]:
    print('The given string is palindrome')
else:
    print('The given string is not palindrome')
```

***Q19. Program to generate words from the given input strings ny taking characters alternatively?***

    inputs: s1 = 'abcdefg'
            s2 = 'xyz'
            s3 = '12345'
    output: ax1, by2, cz3, d4 ,es, f, g

```py

s1 = 'abcdefg'
s2 = 'xyz'
s3 = '12345'

i=j=k=0
while i< len(s1) or j<len(s2) or k<len(s3):
    output = ''
    if i< len(s1):
        output = output + s1[i]
        i+=1
    if j< len(s2):
        output = output + s2[j]
        j+=1
    if k< len(s3):
        output = output + s3[k]
        k+=1
    print(output)
```

1. First convert the given string to “a11” i.e. write, character along with its frequency.
2. Then, change “a11” to “ab” because 11 is b in hexadecimal.
3. Then, finally reverse the string i.e “ba”.

    `Input: S = “abc”
    Output: 1c1b1a`

```py

input_string = "aabbcc"
frequecy = {}
for i in input_string:
    frequecy[i] = frequecy.get(i,0) + 1
for k,v in reversed(frequecy.items()):
    print(k)
```

```py

input_string = "aabbcc"
frequecy = {}
for i in reversed(input_string):
    frequecy[i] = frequecy.get(i,0) + 1
print(frequecy)
```

```py
import json
input_string = "aabbcc"
frequecy = {}
for i in reversed(input_string):
    frequecy[i] = frequecy.get(i,0) + 1
a = json.dumps(frequecy)
print(a)

# `Input: str = “geEks”`
# `Output: 1`
```

- Either the first 2 characters can be converted to uppercase characters i.e. “GEEks” with 2 operations.
- Or the third character can be converted to a lowercase character i.e. “geeks” with a single operation.

    `Input: str = “geek”`
    `Output: 0`

- The string is already in the specified forma
