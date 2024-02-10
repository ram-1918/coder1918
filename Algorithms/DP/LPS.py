"""
Longest Palindromic Substring

1. Use 2 loops and outer loop is for the length of the string and inner loop iterates over the string of that length
2. Use 2-D array Tabulation DP bottom-up
3. Expand from centers
4. Manacher's Algorithm - Outofscope for coding interviews
"""

def isPalindrome(s):
    n = len(s)
    left, right = 0, n - 1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1    
    return True

def bruteForce(s):
    n = len(s)
    for length in range(n, 0, -1): # length of n to 1 => becaz first palindrome is the largest palindrome
        for start in range(n - length + 1):
            curr = s[start: start + length]
            if isPalindrome(curr):
                return curr

def DP(s):
    # 2d Array
    n = len(s)
    dp = [[False]*n for _ in range(n)]
    dp[0][0] = True
    ans = [0, 0] # left and right indices
    
    # Firstly, Mark True where i == j, as it represents a single charecter, which is a palindrome ('s', 'a' ...)
    for i in range(n):
        dp[i][i] = True
    
    # secondly, if any palindromes of size 2 is found mark dp[i][i+1] as True
    for i in range(n-1):
        if s[i] == s[i+1]: # like in, 'aa', 'cc', 'ee'...
            dp[i][i+1] = True
            ans = [i, i + 1]
    
    # thirdly, iterate over the lengths from 2 to n and in each iteration loop over string of size length 
    # and check s[i] == s[j] and dp[i+1][j-1] is True
    for length in range(2, n):
        for start in range(n - length):
            end = start + length
            if s[start] == s[end] and dp[start+1][end-1] is True:
                dp[start][end] = True
                ans = [start, end]

    return s[ans[0]: ans[1]+1]

def expandHelper(s, left, right):
    n = len(s)
    longest = 1
    while left >= 0 and right < n and s[left] == s[right]:
        longest = right - left + 1
        left -= 1
        right += 1
    return longest, left+1, right-1

def expandCenters(s):
    # expand odd length - start from i, i
    # expand even length - start from i, i + 1
    n = len(s)
    longest = 1
    ans = [0, 0]
    for i in range(n):
        odd_length, left, right = expandHelper(s, i, i)
        if odd_length > longest:
            longest = odd_length
            ans = [left, right]

        even_length, left, right = expandHelper(s, i, i + 1)
        if even_length > longest:
            longest = even_length
            ans = [left, right]

    return s[ans[0]: ans[1] + 1]

def Manachers():
    # Need to learn
    pass

if __name__ == '__main__':
    s = ["babad", "cbbd", "fbnekrnbgkjjjjdjsjbgjfbjzmmissisippirotttor", "abbbaaaabbbaaaaaaaaaaaaa", "cccc", "s"]
    result1 = [bruteForce(st) for st in s]
    result2 = [DP(st) for st in s]
    result3 = [expandCenters(st) for st in s]
    print(f'{result1}\n{result2}\n{result3}')