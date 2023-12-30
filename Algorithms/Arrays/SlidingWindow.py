"""
Sliding Window
--------------
1. It uses two pointers to maintain a window of size k based on the problem requirement
2. It also uses a hashmap or hashset as tools to solve a problem
3. It can also be integrated with other algorithms to solve a sub-problem
4. Longest common substring, longest common subsequence, sum of subarrays whose sum is k, maximum window substring
5. Keywords - subarrays, subsets, window
"""
from collections import Counter, deque

# ---------------------------Longest common substring------------------------------------------
def LCSubstring(s):
    left = 0
    n = len(s)
    max_len = 0
    hmap = {} # {charecter: index}
    for right in range(n): # O(n)
        c = s[right]
        if c in hmap:
            left = max(hmap[c], left) # Left pointer moves only if that charecter is in the window
        max_len = max(max_len, right - left + 1)
        hmap[c] = right + 1 # incremting the index of the charecter by 1
    return max_len

# ---------------------------Minimum window substring------------------------------------------

# this algorithm keeps track of if the desired window is formed
def minWindow(s1, s2):
    if not s1 or not s3:
        return ''
    if s1 == s2:
        return s1
    freq1 = Counter()
    freq2 = Counter(s2)
    desired = len(freq2)
    left = formed = 0
    answer = (float('inf'), 0, 0)
    n = len(s1)
    for right in range(n):
        c = s1[right]
        freq1[c] += 1
        # check if formed or not
        if c in freq2 and freq1[c] == freq2[c]:
            formed += 1
        # move left pointer to find the maximum window
        while left <= right and formed == desired:
            c1 = s1[left]
            # update length
            if right - left + 1 < answer[0]:
                answer = (right - left + 1, left, right)
            freq1[c1] -= 1
            if c1 in freq2 and freq1[c1] < freq2[c1]:
                formed -= 1
            left += 1
    return s1[answer[1]: answer[2]+1] if answer[0] != float('inf') else ''

# ---------------------------Sliding Window Maximum------------------------------------------
# Uses Monotonic queue, Maintain a queue such that first element should always be max value in the window
def firstK(lst, k, queue):
    for right in range(k):
        while queue and lst[queue[-1]] < lst[right]: # condition to preserve monotonic property
            queue.pop()
        queue.append(right)

def afterK(lst, k, queue, res):
    n = len(lst)
    for right in range(k, n):
        if queue and right - queue[0] == k: # queue[0] is the first index
            queue.popleft()
        while queue and lst[queue[-1]] < lst[right]: # condition to preserve monotonic property
            queue.pop()
        queue.append(right)
        res.append(lst[queue[0]]) # At this step, first element in the queue contains the maximum value of the window

def maxWindow(lst, k):
    queue = deque()
    res = []
    firstK(lst, k, queue) # after this step queue contains atleast K integers, so after this our task is to just maintain the queue size og 'k'
    res.append(lst[queue[0]])
    afterK(lst, k, queue, res)
    return res



if __name__ == '__main__':
    s2 = "abdbviefbanc"
    s3 = "abc"
    lst = [1,3,-1,-3,5,3,5,8]
    result1 = [LCSubstring(s1) for s1 in ["abcabcbbabcsd", "bbbbb", "pwwkew", "ab", "a", "", "abba"]]
    result2 = minWindow(s2, s3)
    result3 = maxWindow(lst, 3)
    print(result1, result2, result3)