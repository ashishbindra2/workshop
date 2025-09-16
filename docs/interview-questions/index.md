# Python Interview Questions

Common Python questions asked in technical interviews.

## find an element in a sorted list with binary sort

```py
def binary_search(sorted_list, target):
    low = 0
    high = len(sorted_list) - 1

    while low <= high:
        mid = (low + high) // 2
        if sorted_list[mid] == target:
            return mid  # Element found, return its index
        elif sorted_list[mid] < target:
            low = mid + 1  # Target is in the right half
        else:
            high = mid - 1 # Target is in the left half
    return -1  # Element not found

# Example Usage:
my_list = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
target_value = 11
result = binary_search(my_list, target_value)

if result != -1:
    print(f"Element {target_value} found at index {result}")
else:
    print(f"Element {target_value} not found in the list")
```

## Find the Missing Number

<https://www.geeksforgeeks.org/dsa/find-the-missing-number/>

```py
def missingNum(arr):
    n = len(arr) + 1

    # Iterate from 1 to n and check
    # if the current number is present
    for i in range(1, n + 1):
        found = False
        for j in range(n - 1):
            if arr[j] == i:
                found = True
                break

        # If the current number is not present
        if not found:
            return i
    return -1

if __name__ == '__main__':
    arr = [8, 2, 4, 5, 3, 7, 1]
    print(missingNum(arr))
```

## Missing in a Sorted Array of Natural Numbers

1. find the missing elements from the sorted array
<https://takeuforward.org/arrays/find-the-missing-number-in-an-array/>

## Program for Binary To Decimal Conversion

<https://www.geeksforgeeks.org/dsa/program-binary-decimal-conversion/>

## Check whether second string can be formed from characters of first string

## Program to Print Fibonacci Series

```py
# Function to print fibonacci series
def print_fib(n):
    if n < 1:
        print("Invalid Number of terms")
        return

    # When number of terms is greater than 0
    prev1 = 1
    prev2 = 0

    print(prev2, end=" ")

    # If n is 1, then we do not need to
    # proceed further
    if n == 1:
        return

    print(prev1, end=" ")
    
    # Print 3rd number onwards using
    # the recursive formula
    for i in range(3, n + 1):
        curr = prev1 + prev2
        prev2 = prev1
        prev1 = curr
        print(curr, end=" ")

# Driver code
if __name__ == "__main__":
    n = 9
    print_fib(n)
```

## Finding the most frequent character in a string

```py
import collections
s = "helloworld"
print(collections.Counter(s).most_common(1)[0])
```

## Maximum consecutive repeating character in string

```py
# Python program to find the maximum consecutive
# repeating character in given string

# Function to find out the maximum repeating
# character in given string
def maxRepeating(s):
    n = len(s)
    maxCnt = 0
    res = s[0]

    # Find the maximum repeating character
    # starting from s[i]
    for i in range(n):
        cnt = 0
        for j in range(i, n):
            if s[i] != s[j]:
                break
            cnt += 1

        # Update result if required
        if cnt > maxCnt:
            maxCnt = cnt
            res = s[i]

    return res

if __name__ == "__main__":
    s = "aaaabbaaccde"
    print(maxRepeating(s))
```

## Bubble Sort with Python

```py
mylist = [64, 34, 25, 12, 22, 11, 90, 5]

n = len(mylist)
for i in range(n-1):
  for j in range(n-i-1):
    if mylist[j] > mylist[j+1]:
      mylist[j], mylist[j+1] = mylist[j+1], mylist[j]

print(mylist)
```
