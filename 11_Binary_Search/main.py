from typing import List

arr = [i for i in range(1, 20, 2)]
target = int(input("Enter your number to find in the list: "))


# linear Seach


# if target not in arr:
#     print(f"{target} not found in list")


# for i in arr:
#     if target == i:
#         index = arr.index(i)
#         print(f"You target index is: {index}")


# Binary Seach


def binary_seach(arr: List[int], target: int):
    high = len(arr) - 1
    low = 0

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1


output = binary_seach(arr, target)

if output != -1:
    print(f"Your target index is: {output}")
else:
    print(f"{target} not found in list")
