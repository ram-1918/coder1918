"""
Prefix Sum
----------
1. pre-computation comes in handy when dealing with array based operations
2. Cumulative sum, product of array except self, trapping rain water
"""

def prefix_sum(nums):
    n = len(nums)
    prefix = [0] * (n + 1)
    for i in range(n):
        prefix[i + 1] = prefix[i] + nums[i]
    print(prefix)

def max_subarray_sum(nums):
    n = len(nums)
    prefix = [0] * n
    prefix[0] = nums[0]
    # Construct prefixsum array
    for i in range(1, n):
        prefix[i] = prefix[i - 1] + nums[i]
    # Find max_subarray_sum
    min_sum = 0
    max_sum = prefix[0]
    for i in range(n):
        max_sum = max(max_sum, prefix[i] - min_sum)   # find max_sum so far, which gives max subsum
        min_sum = min(min_sum, prefix[i])             # Get minimum prefix so far
    print(max_sum)

def min_subarray_sum(nums):
    n = len(nums)
    prefix = [0] * n
    
    # Create prefix sum
    for i in range(n):
        prefix[i] = prefix[i - 1] + nums[i]
    
    # find min subset sum
    max_sum = 0
    min_sum = nums[0]
    for i in range(n):
        min_sum = min(min_sum, prefix[i] - max_sum)
        max_sum = max(max_sum, prefix[i])
    print(min_sum)

def sum_range(nums, i, j):
    range_sum = 0
    n = len(nums)
    prefix = [0] * n
    prefix[0] = nums[0]
    for k in range(1, n):
        prefix[k] = prefix[k-1] + nums[k]
    range_sum = prefix[j] - prefix[i]
    print(range_sum)

def count_subarray_equals_k(nums, k):
    result = 0
    n = len(nums)
    prefix = 0
    hmap = {0 : 1}
    for i in range(n):
        prefix += nums[i]
        if prefix - k in hmap:
            result += hmap[prefix - k]
        hmap[prefix] = hmap.get(prefix, 0) + 1
    print(result)

def max_len_subarray_equals_k(nums, k):
    n = len(nums)
    prefix = [0] * (n + 1)
    for i in range(n):
        prefix[i + 1] = prefix[i] + nums[i]
    
    seen = {0:1}
    max_len = 0
    for i in range(n):
        # first time subset sum equals k
        if prefix[i] == k:
            max_len = i
        # if any subset sum occurred more than once, calculate max_len
        if prefix[i] - k in seen:
            max_len = max(max_len, i - seen[prefix[i] - k])
        # first occurences of each prefix sum until i
        if prefix[i] not in seen:
            seen[prefix[i]] = i
    print(max_len)

def continous_subarray_sum(nums, k):
    n = len(nums)
    mod_seen = {0: -1}
    prefix_mod = 0
    for i in range(n):
        # prefix_mod gives modulo of k until i
        prefix_mod = (prefix_mod + nums[i]) % k

        # if prefix_mod is already in mod_seen, 
        # then there should be a subset that is modulo k
        if prefix_mod in mod_seen:
            # This makes sure subset size is > 1
            if i - mod_seen[prefix_mod] > 1:
                print("True")
                return True
        else:
            # for the first occurence, map prefix_mod to i
            mod_seen[prefix_mod] = i
    print("False")
    return False

if '__main__' == __name__:
    nums = [23,2,6,4,7] # [ 1, -1, 5, -2, 3] # [-2, 0, 3, -5, 2, -1]
    # prfix[j] - prefix[i]; prefix[3] - prefix[0]; subset_range = (i + 1, j)
    prefix_sum(nums)
    max_subarray_sum(nums)
    min_subarray_sum(nums)
    sum_range(nums, 0, 2)
    count_subarray_equals_k(nums, -2)
    max_len_subarray_equals_k(nums, 3)
    continous_subarray_sum(nums, 13)