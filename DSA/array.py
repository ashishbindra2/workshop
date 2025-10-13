from typing import List

def shift_array(arr: List[int], n: int) -> List[int]:
    for i in range(0,n):
        v = arr.pop()
        arr.insert(0,v)
    return arr


arr = [0, 1, 2, 3, 4, 5]
n = 4
print(shift_array(arr, n))
# assert shift_array(arr, n) == [2, 3, 4, 5, 0, 1]

arr = [1, 2, 3, 4, 5]
n = 2
print(shift_array(arr, n))

arr = [1, 2, 3, 4, 5]
n = 3
print(shift_array(arr, n))
# assert shift_array(arr, n) == [4, 5, 1, 2, 3]