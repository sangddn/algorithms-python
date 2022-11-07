"""
INSERTION SORT
* Sang Doan. Nov 7, 2022.
"""

from typing import List

def InsertionSort(arr:List[int]) -> List[int]:
    for j, key in enumerate(arr[1:], 1):
        i = j - 1
        while i >= 0 and arr[i] > key:
            arr[i + 1] = arr[i]
            i -= 1
        arr[i + 1] = key
    return arr

def main():
    from numpy import random
    arr = random.randint(100_000, size=500_000)
    _ = InsertionSort(arr)
    # print(arr)
    # print(InsertionSort(arr))
    return

if __name__ == "__main__":
    main()        