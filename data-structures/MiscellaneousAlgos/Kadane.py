"""
Kadane's Algorithm
------------------
It is used to find the maximum subset sum in linear time
Let's consider this is the list of integers of size 7, [1,5,-2,-3,-6,7,9]
Now the trick here is to find sum of elements so far and compare the sum with the current element and repeat the process
For this to implement we need to have 2 variables to keep track of current_sum and max_sum

Let's get this into action
    list,           current_sum,     max_sum
1. [1,5,-2,-3,-6,7,9], 1               1
2. [1,5,-2,-3,-6,7,9], 6               6
3. [1,5,-2,-3,-6,7,9], 4               6
4. [1,5,-2,-3,-6,7,9], 1               6
5. [1,5,-2,-3,-6,7,9], -5               6
6. [1,5,-2,-3,-6,7,9], 7               7
7. [1,5,-2,-3,-6,7,9], 16               16
"""

# Algorithm - max() function is not efficient in terms of time complexity, instead use if conditions
def findMaxSubsetSum(arr):
    current_sum = 0
    max_sum = float('-inf')
    n = len(arr)
    for i in range(n):
        current_sum += arr[i]
        if current_sum < arr[i]: # here we are updating the current sum, if current_sum is less than the current element
            current_sum = arr[i]
        if max_sum < current_sum: # At this step, maximum sum is being updated, if current_sum larger than the max_sum
            max_sum = current_sum
    return max_sum

# Find maximum subarray - this time get the maximum sum subarray - idea is to update start and end indices of the subarray
def findMaxSubArray(arr):
    start = end = 0
    current_sum = max_sum = arr[0]
    n = len(arr)
    for idx in range(n):
        current_sum += arr[idx]
        if current_sum < arr[idx]: # each time current_sum changes, update start index
            current_sum = arr[idx]
            start = idx
        if max_sum < current_sum: # each time max_sum changes, update end index
            max_sum = current_sum
            end = idx
    return arr[start: end+1]


if __name__ == '__main__':
    arrs = [[1,5,-2,-3,-6,7,9], [-2, -3, 4, -1, -2, 1, 5, -3], [-2,1,-3,4,-1,2,1,-5,4], [5,4,-1,7,8], [1]]
    result1 = [findMaxSubsetSum(arr) for arr in arrs]
    result2 = [findMaxSubArray(arr) for arr in arrs]
    print(result1)
    print(result2)
