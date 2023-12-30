"""
Two pointer variants
--------------------
1. 2 pointers from opposite directions
2. 2 pointers towards the same direction
3. It is useful when arrays are sorted
4. Two sum, Three sum - When arrays are sorted
5. Binary search - It works on top of two pointers
6. Fast and slow pointers - used in detecting cycles, finding duplicate number
7. Palindrome detection, Frequency count in a sorted array
8. Closest pairs
9. Sliding window is also built on top of 2 pointers
10. Three pointers - from the end/start - 2 out of 3 pointers are used to compare and the other one is used to update the appropriate value
11. Moving Zeros to the end, move unique values to the start of the array
12. Dutch flag sorting
"""

# Two sum - arr is sorted
def findTwoNumbers(arr, target):
    left = 0
    right = len(arr) - 1
    while left < right:
        sumOfNumbers = arr[left] + arr[right]
        if sumOfNumbers == target:
            return [arr[left], arr[right]]
        elif sumOfNumbers < target:
            left += 1
        else:
            right -= 1
    return [-1, -1]

# Move zeros to the end
# This algorithm preserves the order of elements
def moveZerosToEnd(arr):
    n = len(arr)
    zeroPointer = 0
    for curr in range(n):
        # Whenever non-zero element is encountered, swap with the element at the zeroPointer index
        if arr[curr] != 0:
            arr[zeroPointer], arr[curr] = arr[curr], arr[zeroPointer]
            zeroPointer += 1
    return arr

# move unique values to the front
def moveUnique(arr):
    n = len(arr)
    start = 1
    for curr in range(1, n):
        if arr[curr - 1] != arr[curr]:
            arr[start] = arr[curr]
            start += 1
    return arr[:start]

def checkPalindrome(s, left, right):
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True

# Valid palindrome after one charecter removal
def validPalindrome(s):
    n = len(s)
    left, right = 0, n - 1
    while left < right:
        if s[left] != s[right]:
            if checkPalindrome(s, left + 1, right) or checkPalindrome(s, left, right - 1):
                return True
            return False
        left += 1
        right -= 1
    return True


if __name__ == '__main__':
    numbers = findTwoNumbers([2,4,7,8,9], 9)
    moved_zeros = moveZerosToEnd([1,2,5,6,4,5,0,1,2,0,0,0,0])
    moved_unique = moveUnique([1,1,1,2,2,2,4,4,5,5,6,6,6])
    isPalindrome = validPalindrome('aabcedbaa')
    print(numbers, moved_zeros, moved_unique, isPalindrome)