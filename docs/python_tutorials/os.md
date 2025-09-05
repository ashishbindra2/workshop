# Os

## Working with Directories

It is very common requirement to perform operations for directories like

1. To know current working directory
2. To create a new directory
3. To remove an existing directory
4. To rename a directory
5. To list contents of the directory etc...

To perform these operations, Python provides inbuilt module os,which contains several functions to perform directory related operations.

## Q1. To Know Current Working Directory

```py
import os 

cwd = os.getcwd() 
print("Current Working Directory:",cwd) # C:\Users\Bindra\Desktop\TODO\python_programing
```

## Q2. To Create a Sub Directory in the Current Working Directory

```py
import os 

os.mkdir("mysub")
print("mysub directory created in cwd")
```

## Q3. To Create a Sub Directory in mysub Directory

- cwd |-mysub |-mysub2

```py
import os

os.mkdir("mysub/mysub2") 
print("mysub2 created inside mysub")
```

## Q4. To Create Multiple Directories like sub1 in that sub2 in that sub3

```py
import os 

os.makedirs("sub1/sub2/sub3") 
print("sub1 and in that sub2 and in that sub3 directories created")
```

## Q5. To Remove a Directory

```py
import os 

os.rmdir("mysub/mysub2") 
print("mysub2 directory deleted")
```

## Q6. To Remove Multiple Directories in the Path

```py
import os 

os.removedirs("sub1/sub2/sub3") 
print("All 3 directories sub1,sub2 and sub3 removed")
```

## Q7. To Rename a Directory

```py
import os 

os.rename("mysub","newdir") 
print("mysub directory renamed to newdir")
```

## Q8. To know Contents of Directory

- OS Module provides listdir() to list out the contents of the specified directory.
- It won't display the contents of sub directory.

```py
import os 
print(os.listdir("."))
```

- The above program display contents of current working directory but not contents of sub directories.
- If we want the contents of a directory including sub directories then we should go for walk() function.

## Q9. To Know Contents of Directory including Sub Directories

-We have to use walk() function

- [Can you please walk in the directory so that we can aware all contents of that directory]
- os.walk(path, topdown = True, onerror = None, followlinks = False)
- It returns an Iterator object whose contents can be displayed by using for loop
- path : Directory Path. cwd means .
-topdown = True : Travel from top to bottom
- onerror = None : On error detected which function has to execute.
- followlinks = True : To visit directories pointed by symbolic links

```py title="Eg: To display all contents of Current working directory including sub directories:"
import os 
for dirpath,dirnames,filenames in os.walk('.'):
    print("Current Directory Path:",dirpath) 
    print("Directories:",dirnames)
    print("Files:",filenames) 
    print()
```

Note:
To display contents of particular directory, we have to provide that directory name as argument to walk() function.

`os.walk("directoryname")`

## Q. What is the difference between listdir() and walk() Functions?

In the case of listdir(), we will get contents of specified directory but not sub directory contents. But in the case of walk() function we will get contents of specified directory and its sub directories also.

## Running Other Programs from Python Program

OS Module contains system() function to run programs and commands. It is exactly same as system() function in C language.

- `os.system("commad string")`
- The argument is any command which is executing from DOS.

```py
import os 

os.system("dir *.py")
os.system("py abc.py")

```

## How to get Information about a File

We can get statistics of a file like size, last accessed time,last modified time etc by using stat() function of os module.

- `stats = os.stat("abc.txt")`

## The statistics of a file includes the following parameters

1. st_mode: Protection Bits
2. st_ino: Inode number
3. st_dev: Device
4. st_nlink: Number of Hard Links
5. st_uid: User id of Owner
6. st_gid: Group id of Owner
7. st_size: Size of File in Bytes
8. st_atime: Time of Most Recent Access
9. st_mtime: Time of Most Recent Modification
10. st_ctime: Time of Most Recent Meta Data Change

Note:
st_atime, st_mtime and st_ctime returns the time as number of milli seconds since Jan 1st 1970, 12:00 AM. By using datetime module from timestamp() function, we can get exact date and time.

## Q. To Print all Statistics of File abc.txt

```py
import os 

stats=os.stat("if.txt") 
print(stats)
```

## Q. To Print specified Properties

```py
import os 
from datetime import * 

stats=os.stat("if.txt")

print("File Size in Bytes:",stats.st_size)
print("File Last Accessed Time:",datetime.fromtimestamp(stats.st_atime)) 

O/P
File Size in Bytes: 90
File Last Accessed Time: 2024-09-11 12:56:36.763284
File Last Modified Time: 2024-04-12 15:26:52.562774
```

## Assignment

### 81. Python Program to Get Line Count of a File

```py
with open("data_file.txt") as f:
    for i, l in enumerate(f):
        pass
i + 1

```

```py
# Example 2: Using list comprehension
num_of_lines = sum(1 for l in open('data_file.txt'))

print(num_of_lines)
```

### 82. Python Program to Find All File with .txt Extension Present Inside a Directory

os.chdir("my_dir") sets the current working directory to /my_dir.

- Using a for loop, you can search for files with .txt extension using glob().

- denotes all files with a given extension

```py
# Example 1: Using glob
import glob, os

os.chdir("my_dir")

for file in glob.glob("*.txt"):
    print(file)
```

```py
# Example 2: Using os
import os

for file in os.listdir("my_dir"):
    if file.endswith(".txt"):
        print(file)
```

```py
# Using os.walk
import os

for root, dirs, files in os.walk("my_dir"):
    for file in files:
        if file.endswith(".txt"):
            print(file)
```

### 83. Python Program to Get File Creation and Modification Date

```py
# Example 1: Using os module
import os.path, time

file = pathlib.Path('data_file.txt')
print("Last modification time: %s" % time.ctime(os.path.getmtime(file)))
print("Last metadata change time or path creation time: %s" % time.ctime(os.path.getctime(file)))
```

#### getmtime() gives the last modification time whereas getctime() gives the last metadata change time in Linux/Unix and path creation time in Windows

```py
# Example 2: Using stat() method
import datetime
import pathlib

fname = pathlib.Path('data_file.txt')
print("Last modification time: %s" % datetime.datetime.fromtimestamp(fname.stat().st_mtime))
print("Last metadata change time or path creation time: %s" % datetime.datetime.fromtimestamp(fname.stat().st_ctime))
```

### 84. Python Program to Get the Full Path of the Current Working Directory

```py
# Example 1: Using pathlib module
import pathlib

# path of the given file
print(pathlib.Path("my_file.txt").parent.absolute())

# current working directory
print(pathlib.Path().absolute())
```

```py
# Example 2: Using os module
import os

# path of the given file
print(os.path.dirname(os.path.abspath("my_file.txt")))

# current working directory
print(os.path.abspath(os.getcwd()))
```

### 86. Python Program to Check the File Size

```py
import os 

filepath = "data_file.txt"
file_size = os.path.getsize(filepath)
file_size
```

```py
# Example 1: Using os module
import os

file_stat = os.stat(filepath)
print(file_stat.st_size)

file_stat
```

```py
# Example 2: Using pathlib module
from pathlib import Path

file = Path(filepath)
print(file.stat().st_size)
```
