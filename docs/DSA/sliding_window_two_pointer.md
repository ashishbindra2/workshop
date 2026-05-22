# Two pointer / Sliding Window

1. Constant Window
2. Longest subarray / subsring wehere <condion>

---

1. Constant Window

arr = [-1, 2, 3, 3, 4, 5, -1]
k=4

consicutativly without kisping index

```py
l=0
r=k-1

sum = 7

while r < n:
    sum = sum arr[l]
    l+=1
    r+=1
    sum = sum + arrr[r]
    maxsum = max(maxsum,sum)
```

2. Longest substring

arr = [2,5,1,7,10]
---

1. brrute force -> Generate all the subarray

```py
maxlen = 0
for i in range(n):
    sum = 0
    for j in range(i,n):
        sum = sum + arr[j]
        if sum <=k:
            maxlen = max(maxlen , j-i+1)
        elif sum > k:
            break

prin(maxlen) 
```

2. better
3. optimal

---
