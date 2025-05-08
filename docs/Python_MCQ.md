## Python MCQ

### Q1. Suppose you have a bank account number, what do you think will be its data type?
Example: 0000777888119 
- a. int
- b. string 
- c. float

### Q2. Assume that there are five variables with the values given below: 
```py
num1=10
num2=5 
num3=0 
num4=2 
num5=10 
(num1==num5) and ((num2-num4*num3) == (num2-num3))
```

Which among the expressions provide the same result as the
above expression?
- a)	(num2-num4*num3) <= ((num2-num4)*num3)
- b)	not(num3>=num4) and (num5/num2 == num4) 
- c)	not(num5>num4) or (num4+num2)>num1
- d)	(num1==num5) and (not(num5/num2 == num1/num2))

### Q3 What is the output of the below code snippet?
```py
num1 = 10
num2 = 5
num2 *= num1
print(num2)
```
This is same as num2=num2*num1. Python allows you to do this kind of short circuiting with any arithmetic operator
- a)	50 
- b)	10
- c)	25
- d)	100

### Q4 What is the output of the below code snippet?
```py
num1 = 50
num2 = 2
num3 = 3
num4 = 8
result = num1/num4-num3*num2+num4
print(result)
```

- a)	100
- b)	14.5
- c)	8.25 
- d)	-23.75

### Q5 Identify the below expressions which would result in False?
1. True and True
2. False and True
3. 1==1 and 2==1
4. 1==1 and 2!=1
5. True and 1==1

- a)	2, 3
- b)	1, 3, 5
- c)	3, 4
- d)	4, 5

### Q6 Identify the below expressions which would result in True?
1.	"Yes" == "Ok"
2.	not(True and False)
3.	not("Landed"=="Landed" and "Flight"=="F101")
4.	1==1 and (not(1==1 or 1==0))

- a)	2, 3
- b)	1, 2
- c)	1. 3
- d)	2, 4

### Q7 Given below is a DataFrame df, choose the right option when the given snippet executes:
```py
import pandas as pd
df = pd.DataFrame([[54.2,'a'],[658,'d']],
                  index = list('pq'))
df.columns = df.index
print(df.columns.values)
``` 

* a) [0, 1]
* b) ['p', 'q']
* c) RangeIndex(start=0, stop=2, step=1)
* d) Index(['p', 'q'], dtype='object')

### Q8 State True or False
A pandas dataframe of size(3, 3) can be constructed just by passing 5 values to it.
        
    a)	True
    b)	False

### Q9 State True or False
Pandas dataframe inherit the properties of numpy arrays

    a)	True
    b)	False

### Q10. What is the output of the below code snippet?
for var1,var2 in (1,2),(3,4):
    	print(var1+var2,end=" ")

    a)	4 6
    b)	10
    c)	3 7
    d)	TypeError

### Q11. Find the output of the below Python code.
Note: Assume that necessary imports have been done.
```py
import math 
num_list=[32.5,44.3,66.6,78.4,99.2]
for num in range(0,len(num_list)):
    num_list[num]=math.ceil(num_list[num])
num_list.reverse()
print(num_list)
```

    a)	[33, 45, 67, 79, 100]
    b)	[100, 79, 67, 45, 33]
    c)	[33, 44, 67, 78, 99]
    d)	[99, 78, 67, 44, 33]

### Q12 What is the output of the below code snippet?
```py
list = ["ABC", "DEF", "GHI", 100]
str=""
for item in list:
    str+=str(item)
print(str)
```

    a)	TypeError
    b)	ABCDEFGHI100
    c)	ValueError
    d)	ABCDEFGHI
### Q13 What is the output of the below code snippet?
```py
def remove_odd(list1):
    for index in range(len(list1)):
        if list1[index] % 2 == 0:
            list1.remove(list1[index])
list1 = [1,2,3,4,5]
remove_odd(list1)
print(list1)
```

    a) [1,3,5]
    b) IndexError
    c) [1,2,4,5]
    d) [1,2,3,4,5]

### Q14 What is the output of the below code snippet?
```py
list1 = [10,20,30,40,50,60]
for num in len(list1):
    print(num,end="")
```

    a)	6
    b)	10 20 30 40 50 60
    c)	60
    d)	Error

### Q15 What is the output of the below code snippet?
```py
def average(list1):
    sum, count = 0,0
    for index in range(0, len(list1) -1):
        sum += list1[index]
        count += 1
    return sum/count
print(average([1,2,3,4,5]))
```

    a)	2.5
    b)	2
    c)	3.0
    d)	3

### Q16 What is the output of the below code snippet?
```py
result = 0
list1 = [10,20,30]
list2 = [1,2]
for num in range(len(list1)):
    for num in range(len(list2)):
        result+=list1[num]+list2[num]
print(result)
```

    a)	22
    b)	Error
    c)	129
    d)	99

### Q17 What is the output of the below code snippet?
```py
 def move(list1, list2):
    for num in list1:
        list2.append(num)
        list1.remove(num)
list1 = [1,2,3,4,5]
list2 = [10]
move(list1,list2)
print((list1, list2))
```

    a)	([],[10,1,2,3,4,5])
    b)	([1,2,3,4,5],[10])
    c)	([2, 4], [10, 1, 3, 5])
    d)	ValueError

### Q18 What would be the output of Python code given below?
```py
elements=[2,5,6,0]
try:
    div=elements[4]/elements[3]
except ZeroDivisionError:
    print("Infinity")
except IndexError:
    print("Index Error")
except Exception:
    print("0")
finally:
    print("In finally block")
```

    a. Infinity
        In finally block
    b. 0
        In finally block
    c. Index Error
        In finally block
    d. Index Error

### Q19 Consider the following list of pan card numbers:
```py
pancard_list=["AABGT6715H", "UFFAC4352T", "IFSBD9163K", "JOOEC1225H","RWXAFE187B"] 
What is the output of the below two print statements?
print(pancard_list[3][6], end=" ")
print(pancard_list[4][3:])
```

    a)	9 OEC1225H
    b)	2 AFE187B
    c)	9163K O
    d)	225H A

### Q20 What is the output of the code given below?
```py
message="welcome to Mysore"
word=message[-7:]
if(word=="mysore"):
    print("got it")
else:
    message=message[3:14]
    print(message)
```

    a)	come to Myso
    b)	come to Mys
    c)	lcome to Mys
    d)	lcome to Myso

### Q21 What is the output of the below code?
```py
song="JINGLE Bells jingle Bells Jingle All The Way"
song.upper()
song_words=song.split()
count=0
for word in song_words:
    if(word.startswith("jingle")):
        count=count+1
print(count)
```

    a)	0
    b)	3
    c)	2
    d)	1

### Q22 Which among the following statements are CORRECT with respect to functions?
Choose THREE correct options.

    a)	It is a section of a program that performs a specific task 
    b)	It helps to clearly separate tasks within a program 
    c)	Control can be transferred back and forth between different functions based on need 
    d)	It doesn't help to achieve modularity
    e)	It doesn't support reusability

### Q21 Match the following based on collect_tax() function given below:
```py
def collect_tax(x,y):
    tax=x+y
    return tax
a=5000
b=12000
result=collect_tax(a,b)
print(result)
```

    a)	def collect_tax(x,y): (Function call)
    b)	collect_tax(a,b) (Function signature)
    c)	a,b (Actual arguments)
    d)	x,y (Formal arguments)


### Q22 Choose the most appropriate function call needed at line 4 to get the output as ‘Result: 4’.
```py
def check_value(message,num):
    msg=message[:num]
    return len(msg)
#function call statement
print("Result:", result)
``` 
    a)	result=check_value(‘Infosys’,3)
    b)	result=check_value(4,'Infosys‘)
    c)	result=check_value('Infosys',4) 
    d)	result=check_value('Infosys',len('Infosys'))

### Q23 Predict the output of the following code snippet:
```py
def func1():
    print("Inside Func1")
    return 10

def func2():
    print("Inside Func2")
    num=func1()
    return num

def func3():
    print("Inside Func3")
    num=func2()
    num=num*5
    return num

val=func3()
print(val)
```

    a). Inside Func3
        Inside Func2
        Inside Func1
        50
    b). Inside Func1
        Inside Func2
        Inside Func3
        50
    c). Inside Func3
        Inside Func2
        Inside Func1
        10
    d). Inside Func1
        Inside Func2
        Inside Func3
        10
 
### Q24 What is the output of the following code snippet?
```py
def verify(num1,num2):
    if num1 > num2:
        return num1
    elif num1 == num2:
        return 1
    else:
        return num2

def display(arg1,arg2):
    if(verify(arg1,arg2)==arg1):
        print("A")
    elif(verify(arg1,arg2)==1):
        print("C")
    else:
        print("B")
display(1000,3500)
``` 
    a)	A
    b)	B 
    c)	C

### Q25 How many times "executed" will be printed in the output?
```py
for variable_1 in range(1,5,-1):
    print("executed")
```

    a)	0
    b)	5
    c)	1
    d)	4


### Q26 How many times "TPF" will be printed in the output?
```py
grade_list = ["A+","A-","B","B+","A+","A+","A-"]
for grade in grade_list:
    if grade == "A+":
        print("TPF")
    else:
        print("Not TPF")
``` 
    a)	2
    b)	3
    c)	4

### Q27 Predict the output of the following code snippet.
```py
number=28
for num in range(25,30):
    if(number>num):
        print(num)
    else:
        print(num)
        break
```
    a. 28
    b. 25
        26
        27
        28
    c. 25
        26
        27
    d. 25
        26
        27
        28
        29
### Q28 Predict the output of the following code snippet.
```py
for num in 23, 45, 50, 65, 76, 90:
    if(num%5!=0):
        continue
    if(num%10==0):
        print(num, end=" ")
        continue
    if(num%3==0):
        print(num, end=" ")
``` 
    a)	45 50 90
    b)	45 50 65 90
    c)	45 90
    d)	23 76

### Q29 Predict the output of the following code snippet.
```py
for number in 10,15:
    for counter in range(1,3):
        print(number*counter, end=" ")
```
    a)	10 20 15 30
    b)	10 20 30 15 30 45
    c)	10 15 20 30 30 45
    d)	10 15 20 30

### Q30. What should be the value of the variables num1 and num2 in the code below if the output expected is 4?
```py
num1=?
num2=?
while(num1>=2):
    if(num1>num2):
        num1=num1/2
    else:
        print(num1)
        break
``` 
    a)	12, 5
    b)	8, 2
    c)	16, 6
    d)	16, 2

### Q31 Predict the output of the following code snippet.
 
    1 3 5 7 9
    0 2 4 6 8
    0 1 3 5 7 9
    1 3 5 7

### Q32 What will be printed in the output after the executing the code below?
```py
numbers_list = [98,45,60,71,90]
count = 10
for number in numbers_list:
    if number % 10 == 0:
        count -= 1
        continue
    counter = 0
    while counter < 2:
        last_digit = number % 10
        number = number // 10
        if last_digit > 4:
            count += 1
            break
        count += 1
        counter += 1
print(count)
``` 
    a)	12
    b)	13
    c)	11

### Q33 What is the output of the following code snippet?

```py
sample_dict = {'a':1,'b':2}
sample_dict.update({'b':5, 'c':10 })
print(sample_dict.get('b'), sample_dict.get('c'))
```
    a)	5,10
    b)	2 None
    c)	2 10
    d)	5 None

### Q34 Given the list list1 = ["e","d","u","c","a","t","i","o","n"]
What expression will result in the list ["c", "a", "t"] ?

    a)	list1[2:5]
    b)	list1[3:6] 
    c)	list1[5:2]
    d)	list1[3:5]

### Q35 What is the output of the following code snippet?
``` py
num_list = [100.5,30.465,-1.22,20.15]
num_list.insert(1, -100.5)
num_list.pop(0)
num_list.sort()
print(num_list[0])
```
    a)	100.5
    b)	-100.5 
    c)	30.465

### Q36 Which among the following statements may result in an error?
Assume that the statements are executed in the order in which it is written.
```
a. list1=[5,10,15,20,25]
b. print(len(list1))
c. print(list1[4])
d. print(list1[5])
e. print(list1[4:5])
f. list1[2]=12
g. print(list1)
h. list1=list1+[8,9]
```
    a)	b
    b)	d
    c)	e
    d)	h

### Q37 What is the output of the following code snippet?
 
    [0, 0, 0, 0, 0]
    [10, 20, 30, 40, 50]
    [0, 0, 10, 20, 30]
    [0, 10, 20, 30, 40]

### Q38 How many comparisons will take place before flag becomes 1?
```py 
num_list = [1,33,31,5,26,7,8,92,10]
num = 7
flag = 0
for item in num_list:
    if(item == num):
        flag = 1
    else:
        continue
if(flag == 1):
    print(num, "found in the list")
else:
    print(num, "NOT found in the list")
 ```
    a)	6 
    b)	5
    c)	1
    d)	9

### Q39. Given listA = [1,2,3,4,5,5,6,6,7,7,7,8,8,8,8] 
What will be the output of set(listA)?

    a)	1,2,3,4
    b)	5,6,7,8
    c)	1,2,3,4,5,6,7,8 
    d)	The statement will not return any element

### Q40. What will be the output of the following code?
```py
a = [1, 2, 3]
b = [1, 2, 3]
print(a == b)
print(a is b)
```

    A) True True
    B) True False
    C) False True
    D) False False


