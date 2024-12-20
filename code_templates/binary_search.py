# 
def fn(arr, target):
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            # do something
            return
        if arr[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    
    # left is the insertion point
    return left

# duplicate elements, left-most insertion point

def fn(arr, target):
    left = 0
    right = len(arr)
    while left < right:
        mid = (left + right) // 2
        if arr[mid] >= target:
            right = mid
        else:
            left = mid + 1

    return left

# duplicate elements, right-most insertion point

def fn(arr, target):
    left = 0
    right = len(arr)
    while left < right:
        mid = (left + right) // 2
        if arr[mid] > target:
            right = mid
        else:
            left = mid + 1

    return left

# for greedy problems
# looking for minimum

def fn(arr):
    def check(x):
        # this function is implemented depending on the problem
        return 'BOOLEAN'

    left = 'MINIMUM_POSSIBLE_ANSWER'
    right = 'MAXIMUM_POSSIBLE_ANSWER'
    while left <= right:
        mid = (left + right) // 2
        if check(mid):
            right = mid - 1
        else:
            left = mid + 1
    
    return left

# For maximum

def fn(arr):
    def check(x):
        # this function is implemented depending on the problem
        return 'BOOLEAN'

    left = 'MINIMUM_POSSIBLE_ANSWER'
    right = 'MAXIMUM_POSSIBLE_ANSWER'
    while left <= right:
        mid = (left + right) // 2
        if check(mid):
            left = mid + 1
        else:
            right = mid - 1
    
    return right

