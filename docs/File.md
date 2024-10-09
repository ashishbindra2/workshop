
# FILE HANDLING
- As the part of programming requirement, we have to store our data permanently for future purpose. For this requirement we should go for files. 
- Files are very common permanent storage areas to store our data.

## Types of Files:
There are 2 types of files

1. ***Text Files:*** Usually we can use text files to store character data Eg: abc.txt
2. ***Binary Files:*** Usually we can use binary files to store binary data like images,video files, audio files etc...

### Opening a File: 
- Before performing any operation (like read or write) on the file,first we have to open that file.For this we should use Python's inbuilt function open() 
- But at the time of open, we have to specify mode,which represents the purpose of opening file. 
- `f = open(filename, mode)`
- `f = open("abc.txt","w")`
- We are opening abc.txt file for writing data.


***Note:*** All the above modes are applicable for text files. If the above modes suffixed with 'b' then these represents for binary files.
- Eg: rb,wb,ab,r+b,w+b,a+b,xb

### Closing a File: 
After completing our operations on the file, it is highly recommended to close the file.
- For this we have to use close() function. 
- `f.close()`

## The allowed modes in Python are:
1. r: open an existing file for read operation. The file pointer is positioned at the beginning of the file.If the specified file does not exist then we will get FileNotFoundError.This is default mode.
2. w: open an existing file for write operation. If the file already contains some data then it will be overridden. If the specified file is not already avaialble then this mode will create that file.
3. a: open an existing file for append operation. It won't override existing data.If the specified file is not already avaialble then this mode will create a new file.
4. r+: To read and write data into the file. The previous data in the file will not be deleted.The file pointer is placed at the beginning of the file. 5) w+  To write and read data. It will override existing data.
6. a+: To append and read data from the file.It wont override existing data.
7. x: To open a file in exclusive creation mode for write operation. If the file already exists then we will get FileExistsError.


## Various Properties of File Object: 
Once we opend a file and we got file object, we can get various details related to that file by using its properties. 
- name: Name of opened file 
- mode: Mode in which the file is opened
- closed: Returns boolean value indicates that file is closed or not 
- readable(): Retruns boolean value indicates that whether file is readable or not 
- writable(): Returns boolean value indicates that whether file is writable or not.

```py 
f=open("abc.txt",'w') 

print("File Name: ",f.name)  # abc.txt
print("File Mode: ",f.mode)  # w
print("Is File Readable: ",f.readable()) # False
print("Is File Writable: ",f.writable()) # True
print("Is File Closed : ",f.closed)      # False
f.close()
print("Is File Closed : ",f.closed)      # True
```

### Writing Data to Text Files:
We can write character data to the text files by using the following 2 methods. 

1. write(str) 
2. writelines(list of lines)

```py title="write(str)"
f=open("abcd.txt",'w') 

f.write("Durga\n") 
f.write("Software\n") 
f.write("Solutions\n") 

print("Data written to the file successfully") 
f.close()
```

Note: 
In the above program, data present in the file will be overridden everytime if we run the program. Instead of overriding if we want append operation then we should open the file as follows.

```py title="writelines(list)"
f=open("abcd.txt",'w') 

list=["sunny\n","bunny\n","vinny\n","chinny"] 

f.writelines(list) 

print("List of lines written to the file successfully") 

f.close()
```

Note: 
While writing data by using write() methods, compulsory we have to provide line seperator(\n), otherwise total data should be written to a single line.

### Reading Character Data from Text Files:
We can read character data from text file by using the following read methods.
- read(): To read total data from the file 
- read(n): To read 'n' characters from the file 
- readline(): To read only one line 
- readlines(): To read all lines into a list

```py title="To read total data from the file"
f=open("abcd.txt",'r') 

data=f.read()
print(data) 
f.close()
# o/p
# sunny
# bunny
# vinny
# chinny
```

```py title="read(n): Eg 2: To read only first 10 characters:"
f=open("abcd.txt",'r') 

data=f.read(10) 
print(data)
f.close()
# o/p
# sunny
# bunn

```

```py title="Eg 3 readline(): To read data line by line:"
f=open("abcd.txt",'r')

line1=f.readline()
print(line1,end='') # sunny

line2=f.readline() 
print(line2,end='') # bunny

line3=f.readline() 
print(line3,end='') # vinny

f.close()
```

```py title="Eg 4: To read all lines into list:"
f=open("abcd.txt",'r') 

lines=f.readlines()
print(lines,end='')

f.close() # ['sunny\n', 'bunny\n', 'vinny\n', 'chinny']

```

```py title="Eg 5:"
f=open("abcd.txt","r")

print(f.read(3)) 
print(f.readline())
print(f.read(4)) 
print("Remaining data") 
print(f.read())

o/p
sun
ny

bunn
Remaining data
y
vinny
chinny
```

### The with Statement:
- The with statement can be used while opening a file. We can use this to group file operation statements within a block. 
- The advantage of with statement is it will take care closing of file,after completing all operations automatically even in the case of exceptions also, and we are not required to close explicitly.

```py title="with"

with open("abc.txt","w") as f: 
    f.write("Durga\n")
    f.write("Software\n") 
    f.write("Solutions\n") 
    print("Is File Closed: ",f.closed) # False

print("Is File Closed: ",f.closed) # True
```
### Q Program to print the Number of Lines, Words and Characters present in the given File?

```py 
import os
import sys 

fname=input("Enter File Name: ") 

if os.path.isfile(fname): 
    print("File exists:",fname)     
    f=open(fname,"r") 
    
else:
    print("File does not exist:",fname) 
    sys.exit(0) 
    
lcount=wcount=ccount=0 

for line in f: 
    lcount=lcount+1 
    ccount=ccount+len(line) 
    words=line.split() 
    wcount=wcount+len(words) 

print("The number of Lines:",lcount) 
print("The number of Words:",wcount)
print("The number of Characters:",ccount)

o/p
Enter File Name: note.txt
File exists: note.txt
The number of Lines: 12
The number of Words: 98
The number of Characters: 538
```

## Handling Binary Data: 
It is very common requirement to read or write binary data like images,video files,audio files etc.

### Q Program to read Image File and write to a New Image File?
![alt text](R.jpeg){ width="300" }

```py 
f1=open("R.jpeg","rb") 
f2=open("newpic.jpg","wb") 

bytes=f1.read() 
f2.write(bytes) 

print("New Image is available with the name: newpic.jpg")
```

## Handling CSV Files:
⚽ CSV : Comma seperated values 
⚽ Python provides csv module to handle csv files.

```py title="Writing Data to CSV File:"
import csv 

with open("emp.csv","w",newline='') as f: 
    w=csv.writer(f) # returns csv writer object 
    w.writerow(["ENO","ENAME","ESAL","EADDR"]) 
    
    n=int(input("Enter Number of Employees:")) 

    for i in range(n):
        eno=input("Enter Employee No:") 
        ename=input("Enter Employee Name:")
        esal=input("Enter Employee Salary:") 
        eaddr=input("Enter Employee Address:") 
        w.writerow([eno,ename,esal,eaddr]) 
    
print("Total Employees data written to csv file successfully")
```

```py title="Reading Data from CSV File:"

import csv 

f=open("emp.csv",'r') 

csv_reader=csv.reader(f) #returns csv reader object 
for row in csv_reader:
    print(row)

f.close()
o/p
['ENO', 'ENAME', 'ESAL', 'EADDR']
['101', 'ashish', '10000000', 'punjab']
['102', 'sonu', '29999999', 'UP']
['103', 'bindra', '900000000', 'shimla']
['104', 'kumar', '20202020', 'Himachal']
['105', 'sreshti', '1000000000000000', 'GOA']
```


Note:
Observe the difference with newline attribute and without 

- with open("emp.csv","w",newline='') as f: 
- with open("emp.csv","w") as f:

```py 
import csv 

with open("emp.csv",'r') as f:
    csv_reader=csv.DictReader(f) #returns csv reader object 
    for row in csv_reader:
        print(row)

o/p
{'ENO': '101', 'ENAME': 'ashish', 'ESAL': '10000000', 'EADDR': 'punjab'}
{'ENO': '102', 'ENAME': 'sonu', 'ESAL': '29999999', 'EADDR': 'UP'}
{'ENO': '103', 'ENAME': 'bindra', 'ESAL': '900000000', 'EADDR': 'shimla'}
{'ENO': '104', 'ENAME': 'kumar', 'ESAL': '20202020', 'EADDR': 'Himachal'}
{'ENO': '105', 'ENAME': 'sreshti', 'ESAL': '1000000000000000', 'EADDR': 'GOA'}
```

## Zipping and Unzipping Files:

It is very common requirement to zip and unzip files.
The main advantages are:

1. To improve memory utilization 
2. We can reduce transport time 
3. We can improve performance.

To perform zip and unzip operations, Python contains one in-bulit module zip file. This module contains a class: ZipFile

### To Create Zip File:
We have to create ZipFile class object with name of the zip file, mode and constant ZIP_DEFLATED. This constant represents we are creating zip file. 
- `f = ZipFile("files.zip","w","ZIP_DEFLATED")`
- Once we create ZipFile object,we can add files by using write() method.
- `f.write(filename)`

```py
from zipfile import * 

f=ZipFile("files.zip",'w',ZIP_DEFLATED) 

f.write("abc.txt") 
f.write("abcd.txt") 
f.write("note.txt") 

f.close() 
print("files.zip file created successfully")
```

### To perform unzip Operation:

We have to create ZipFile object as follows 
- `f = ZipFile("files.zip","r",ZIP_STORED)`

- ZIP_STORED represents unzip operation. This is default value and hence we are not required to specify. 
- Once we created ZipFile object for unzip operation, we can get all file names present in that zip file by using namelist() method. 
- `names = f.namelist()`

```py
from zipfile import *

f=ZipFile("files.zip",'r',ZIP_STORED) 
names=f.namelist() 

for name in names: 
    print( "File Name: ",name)

o/p
File Name:  abc.txt
File Name:  abcd.txt
File Name:  note.txt
```
## Assignments

### 46. Python Program to Find Hash of File
```py title="Python program to find the SHA-1 message digest of a file"

# importing the hashlib module
import hashlib

def hash_file(filepath):
   """
   This function returns the SHA-1 hash
   of the file passed into it"""

   # make a hash object
   h = hashlib.sha1()

   # open file for reading in binary mode
   with open(filepath,'rb') as file:

       # loop till the end of the file
       chunk = 0
       while chunk != b'':
           # read only 1024 bytes at a time
           chunk = file.read(1024)
           h.update(chunk)

   # return the hex representation of digest
   return h.hexdigest()

message = hash_file("data_file.txt")    # Use path of the file
print(message)
```
### 49. Python Program to Safely Create a Nested Directory
### 45. Python Program to Find the Size (Resolution) of an Image
### 57. Python Program to Copy a File
```py
# Using shutil module
from shutil import copyfile
copyfile("my_dir/a.txt", "my_dir/b.txt")
```
### 66. Python Program Read a File Line by Line Into a List
```py
with open("data_file.txt") as f:
    content_list = f.readlines()
content_list
```
```py
# Example 1: Using readlines()
with open("data_file.txt") as f:
    content_list = f.readlines()

print(content_list)

content_list = [x.strip() for x in content_list]
print(content_list)
```
```py
# Example 2: Using for loop and list comprehension

with open('data_file.txt') as f:
    content_list = [line.rstrip() for line in f]

print(content_list)
```
```py
with open("data_file.txt") as f:
    content_list = f.readline()
content_list
```
```py
with open("data_file.txt") as f:
    content_list = f.read()
content_list
```
### 69. Python Program to Append to a File
```py
with open("my_file.txt", "a") as f:
   f.write("new text")
```
### 72. Python Program to Extract Extension From the File Name
```py
# Example 1: Using splitext() method from os module
import os
file_details = os.path.splitext('/path/file.ext')
print(file_details)
print(file_details[1])
```
```py
# Example 2: Using pathlib module
import pathlib
print(pathlib.Path('/path/file.ext').suffix)

```
```
```
### 78. Python Program to Get the File Name From the File Path
```py
# Example 1: Using os module
import os

# file name with extension
file_name = os.path.basename('/root/file.ext')

# file name without extension
print(os.path.splitext(file_name)[0])
```

```py
import os

print(os.path.splitext(file_name))
```

```py title="sing Path module"
from pathlib import Path

print(Path('/root/file.ext').stem)
```
### 81. Python Program to Get Line Count of a File
```py
with open("data_file.txt") as f:
    for i, l in enumerate(f):
        pass
i + 1

```
```py title="Example 2: Using list comprehension"
num_of_lines = sum(1 for l in open('data_file.txt'))

print(num_of_lines)
```
