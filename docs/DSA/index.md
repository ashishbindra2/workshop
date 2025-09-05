# DSA

## 🔢 **1. Two Sum — Hash Map Approach**

### 🧩 Question

> Given an array of integers `nums` and an integer `target`, return the indices of the **two numbers** such that they **add up to the target**.
>
> ❗ You may assume that each input has **exactly one solution**, and you may not use the same element twice.

---

### 📥 Example

```python
Input: nums = [2, 7, 11, 15], target = 9  
Output: [0, 1]  
Explanation: nums[0] + nums[1] = 2 + 7 = 9
```

---

### 🧠 Why Is This Asked?

* Tests understanding of **hash maps (dictionaries)**.
* Shows your ability to **optimize brute force** to linear time.
* Frequently asked in **Google, Amazon, Microsoft**.

---

### 🧩 Brute Force (NOT Recommended)

```python
for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        if nums[i] + nums[j] == target:
            return [i, j]
```

⏱ Time: O(n²)

---

### ✅ Optimal Solution (Hash Map)

```python
def two_sum(nums, target):
    hash_map = {}  # key: number, value: index

    for i, num in enumerate(nums):
        diff = target - num
        if diff in hash_map:
            return [hash_map[diff], i]
        hash_map[num] = i
```

---

### 🧮 Time and Space Complexity

| Operation | Complexity |
| --------- | ---------- |
| Time      | O(n)       |
| Space     | O(n)       |

---

### 🧰 How It Works (Step-by-step with nums = \[2, 7, 11, 15], target = 9)

| i | num | diff = target - num | hash\_map | result          |
| - | --- | ------------------- | --------- | --------------- |
| 0 | 2   | 7                   | {}        | -               |
|   |     |                     | {2: 0}    | -               |
| 1 | 7   | 2                   | {2: 0}    | ✅ \[0, 1] found |

---

### 🔍 Key Concepts

* Dictionary lookups are O(1).
* One-pass scan with early exit.

---

### 🧪 Real-World Applications

* Finding 2 products whose prices add to a budget.
* Matching pairs in analytics or stock price differences.

```py
def two_sum(lis, target):
    temp_dict = {}

    for i, num in enumerate(lis):

        diff = target - num
        if diff in temp_dict:
            return temp_dict[diff], i
        temp_dict[num] = i
        # print(diff)
    # print(temp_dict)
nums = [2, 7, 11, 15]
target = 9  

result = two_sum(nums,target)   
result
```
