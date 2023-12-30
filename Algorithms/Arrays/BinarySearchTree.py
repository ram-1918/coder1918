"""
Binary Search Tree
1. Array should be sorted, in each iteration we exclude half of the array => n, n/2, n/4 ... => O(logn)
2. Search space needed, it can be - (0, len(array)-1), (1, max(array)), (max(array), sum(array))
3. left < root < right
4. Time complexity - O(logN); space complexity - O(1) - iterative; O(N) - recursive(call stack space)
5. Subset equal partition; koko eating bananas
6. "search," "find," "target," "range," "maximum," "minimum,"
7. 3 types - left <= right; left < right; left + 1 < right
8. Used as an optimization technique and can be integrated with other algorithms, ex: Sliding Window + Binary Seach

reference - https://leetcode.com/explore/learn/card/binary-search/135/template-iii/946/
"""

import math
import heapq

# template 1 - at last both left and right pointers points to the same position
# post-processing is not needed, as there are no elements between left and right pointers
def regularBS(arr, target):
    n = len(arr)
    left, right = 0, n-1
    while left <= right:
        mid = (left + right) // 2
        value = arr[mid]
        if target == value:
            return mid
        elif target > value:
            left = mid + 1
        else:
            right = mid - 1
    return left # if target is not in arr, left index gives the expected position of the target

# template 2
# Good/Bad number based on an API call, Finding minimum in rotated sorted array 
def advancedBS(arr, target):
    n = len(arr)
    left, right = 0, n-1
    while left < right:
        mid = (left + right) // 2
        value = arr[mid]
        if value == target:
            return mid
        if value < target:
            left = mid + 1
        else:
            right = mid
    # post-processing is needed, as termination condition is left < right; at edge cases like last value of the arr is the target
    if arr[left] == target:
        return left
    return -1

# template 3
# It is not useful for finding the expected position, but useful for finding the peak element, k-closest numbers
def regularBS2(arr, target):
    n = len(arr)
    left, right = 0, n-1
    while left + 1 < right:
        mid = (left + right) // 2
        value = arr[mid]
        if value == target:
            return mid
        elif value < target:
            left = mid
        else:
            right = mid
    
    # post-processing is needed, as we are stoping the loop one index ahead (left + 1 < right)
    if arr[left] == target:
        return left
    elif arr[right] == target:
        return right
    return -1

# --------------- USE CASES ------------------
'''
Maximum in rotated sorted array, k-closest points, peak element, koko eating bananas, equal partition subset
'''

# Maximum in rotated sorted array
# for maximum compare mid value with left whereas for minimum compare mid with left
def findMax(arr):
    n = len(arr)
    left, right = 0, n - 1
    while left + 1 < right:
        mid = (left + right) // 2
        value = arr[mid]
        if value > arr[left]:
            left = mid
        else:
            right = mid
    # post-processing
    if arr[left] > arr[right]:
        return arr[left]
    return arr[right]

# ---------------------------------------------------------------------

def helperBS(arr, target):
    n = len(arr)
    left, right = 0, n - 1
    while left + 1 < right:
        mid = (left + right) // 2
        value = arr[mid]
        if value == target:
            return mid
        elif value < target:
            left = mid
        else:
            right = mid
    
    # post-processing
    return left if abs(arr[left] - target) < abs(arr[right]  - target) else right

def helperSW(arr, idx, k, x):
    left = right = idx
    n = len(arr)
    while right - left - 1 < k:
        if left < 0:
            right += 1
            continue
        if right == n or abs(arr[left] - x) <= abs(arr[right] - x):
            left -= 1
        else:
            right += 1
    return left+1, right

# k-closest points to x
def kclosest(arr, k, x):
    # find the closes point to x from the given array
    closest_index = helperBS(arr, x)
    # use sliding window approach, to create the window of size k
    get_points = helperSW(arr, closest_index, k, x)
    return arr[get_points[0]:get_points[1]]

# ---------------------------------------------------------------------

# finding peak - here we are just focusing on just one increasing sequence
# to check if sequence is increasing or a decresing one - 
# if mid <= mid + 1: peak value should lie on the rightside so move left pointer
# else: peak value should be on the left, so move right to mid
def findPeak(arr):
    n = len(arr)
    left, right = 0, n-1
    while left < right:
        mid = (left + right) // 2
        if arr[mid] <= arr[mid + 1]:
            left = mid + 1
        else:
            right = mid
    return left

# ---------------------------------------------------------------------
# koko eating bananas
def helperCalc(piles, speed):
    return sum(math.ceil(pile/speed) for pile in piles)

def koko(arr, h):
    # perform binary search to efficiently search for speed from the search space (1, max(arr))
    n = len(arr)
    _sum = sum(arr)
    left, right = math.ceil(_sum/h), min(max(arr), math.ceil(_sum/(h-n+1))) # search space for finding speed efficiently
    while left < right:
        mid = (left + right) >> 1 # average speed ~ () // 2
        # if total_time is exceeding given time h, koko has to increase her eating speed
        total_time = helperCalc(arr, mid)
        if total_time > h: 
            left = mid + 1
        else:
            right = mid
    return left

# ---------------------------------------------------------------------
# Split array largest sum

# this finds the number of splits
def helperSplits(arr, curr_max_sum):
    n = len(arr)
    splits = total = 0
    for num in arr:
        total += num
        if total > curr_max_sum:
            splits += 1
            total = num
    
    # if no partition is found in the loop, complete array is considered as one split
    # if one split is found then there are 2 partitions [1,2,3,4,5] => [1,2,3], [4,5] => 2 partitions
    return splits + 1  # total partitions

# binary search for curr_max_sum in (0 to sum(arr)) search space
def largestSum(arr, k):
    n = len(arr)
    left, right = max(arr), sum(arr)
    while left <= right: # This template covers all the values because termination condition is left > right
        curr_max_sum = (left + right) // 2
        splits = helperSplits(arr, curr_max_sum)
        if splits > k:
            left = curr_max_sum + 1
        else:
            right = curr_max_sum - 1
            answer = curr_max_sum
    return answer

# ---------------------------------------------------------------------

if __name__ == '__main__':
    lst1 = [1,4,6,10,24,56,68,69,79,96] # sorted array
    result1 = regularBS(lst1, -1)
    result2 = advancedBS(lst1, 96)
    result3 = regularBS2(lst1, -1)
    print(result1, result2, result3)
    # -----------------------------
    lst2 = [56,68,-1,1,2,4,6,10,24] # Rotated sorted array
    lst3 = [0,0,0,1,3,5,6,7,8,8]
    lst4 = [1,2,1,3,5,3,4,13,45,65,23]
    result4 = findMax(lst2)
    result5 = kclosest(lst3, 2, 2)
    result6 = findPeak(lst4)
    result7 = [koko(lst, h) for lst, h in [([312884470], 312884469), ([3,6,7,11], 8), ([30,11,23,4,20], 5), ([30,11,23,4,20], 6)] ]
    result8 = [largestSum(lst, k) for lst, k in [([7,2,5,10,8], 2), ([1,2,3,4,5], 2), ([1,2,3,4,5], 5), ([1,2,3,4,5], 1), ([30,11,23,4,20], 3)] ]
    print(result4, result5, result6, result7, result8)


