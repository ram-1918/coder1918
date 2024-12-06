'''
Data Structures:
1. Hashmaps
2. Arrays
3. Heaps
4. Trees: BST, Segement tree
5. Linkedlist
6. Graphs

Arrays & Strings
    Two pointers
    Sliding window
    String manipulation

Trees & Graphs
    Binary trees, BST
    DFS, BFS
    Trie
    Shortest path algorithms
    Union Find

Dynamic Programming
    Classic problems (knapsack, LCS)
    State transitions
    Memoization vs Tabulation

Common Patterns
    Hash maps/sets
    Stack/Queue applications
    Binary search
    Heaps/Priority Queues

Edge cases to look for:
1. Indexing: Practice picturing indices in brain and practice it until it becomes smooth
2. Consider IndexOutOfBounds, accessing/poping elements from empty arrays

Other concepts to learn:
Computer science fundamentals
> OSI layers
> Memory management
> Networking
> Storage systems
> System design concepts
'''

'''Dutch flag algorithm:
0's, 1's, 2's
use 3 pointers: lo, mid, hi
initialize these pointers: lo = mid = 0, hi = n - 1

lst = [0,1,2,0,1,0,1,1,1]

case 1: curr == 0:
> swap with curr and lo indexed values
> lo += 1
> curr += 1
case 2: curr == 1
> curr += 1
case 3: curr == 2
> swap curr and hi index values
> hi -= 1
> curr += 1

Walk Through:
-------------
until curr < hi:

lo = curr = 0, hi = 8
lst[0] == 0:
> [0,1,2,0,1,0,1,1,1]
> lo = 1; curr = 1; hi = 8
lst[1] == 1
> [0,1,2,0,1,0,1,1,1]
lo = 1; curr = 2; hi = 8
lst[2] == 2
> [0,1,2,0,1,0,1,1,1]
lo = 1; curr = 3; hi = 7
> [0,1,1,0,1,0,1,1,2]
lst[3] == 0
> [0,1,1,0,1,0,1,1,2]
lo = 2; curr = 4; hi = 7
> [0,0,1,1,1,0,1,1,2]
...
lst[5] == 0
> [0,0,1,1,1,0,1,1,2]
lo = 3; curr = 6; hi = 7
> [0,0,0,1,1,1,1,1,2]

end(curr !< hi)(7 < 7)
'''


import math


def sort_three_colors(lst):
    print(f'Before sorting: {lst}')
    n = len(lst)
    lo = curr = 0
    hi = n - 1
    while curr <= hi:
        print(lst)
        if lst[curr] == 0:
            # swap lo and curr
            # increment lo and curr
            lst[lo], lst[curr] = lst[curr], lst[lo]
            lo += 1
            curr += 1
        elif lst[curr] == 1:
            curr += 1
        else:
            # swap curr and hi
            # decrement hi
            lst[curr], lst[hi] = lst[hi], lst[curr]
            hi -= 1
    print(f'After sorting: {lst}')

def cyclic_sort(lst):
    i = 0
    while i < len(lst):
        curr_index = lst[i] - 1
        print(lst, i, curr_index)
        if lst[i] != lst[curr_index]:
            lst[i], lst[curr_index] = lst[curr_index], lst[i]
        else:
            i += 1
    print(lst, curr_index)

def merge_intervals(intervals):
    '''
    [[1,2], [3,10], [5,15], [6,8], [16,20]]
    i = 1:
    > result = [[1,2]]; ps = 3, pe = 10
    i = 2: 10 >= 5
    > result = [[1,2]]; ps = 3, pe = 15
    i = 3; 15 >= 6
    > result = [[1,2]]; ps = 3, pe = 15
    i = 4; 15 >= 16 X
    > result = [[1,2]]; ps = 16, pe = 20
    '''
    # sort intervals + iterate + merge intervals
    if not intervals:
        return []
    print(f'Before merge intervals: {intervals}')
    intervals.sort()    # sorts based on the start times
    result = [intervals[0]]
    for start, end in intervals[1:]:
        last = result[-1]
        if last[1] >= start:
            # if merged, update the end interval of the last interval in the result
            last[1] = max(last[1], end)
        else:
            # if not merged, then add the current interval to result
            result.append([start, end])
    print(f'Merged intervals: {result}')

def maximize_concatenation(lst):
    '''
    [2,5,30,72,8] => 8725302
    1. sort numbers such that the concatenation of numbers form the largest possible number
    '''
    # x = 2, y = 5; (52 > 25) - (52 < 25) => 1 - 0 => 1 => y + x is correct
    
    # # sort() maps to a function that takes only one argument
    # lst.sort(key=lambda x,y: ((int(y + x) > int(x + y)) - int(y + x) < int(x + y)))

    from functools import cmp_to_key

    def compare(x, y):
        return ((int(y + x) > int(x + y)) - (int(y + x) < int(x + y)))
    
    lst = list(map(str, lst))
    lst.sort(key=cmp_to_key(compare))
    res = ''.join(lst).lstrip('0') or '0'
    print(res)

def longest_substring_non_unique_chars(s):
    '''
    abcabcbbac
    left, right = 0, 0
    Move right -> 
        if s[right] in seen:
            left = max(left, seen[left] + 1)
        seen[right] = right
        max_len = max(max_len, right - left + 1)
    '''
    n = len(s)
    left = 0
    seen = {}
    max_len = float('-inf')
    for right in range(n):
        if s[right] in seen:
            left = seen[s[right]] + 1
        seen[s[right]] = right
        max_len = max(max_len, right - left + 1)
    print(max_len)

def rabin_karp(s, l):
    '''
    Sliding window + Rolling hash
    1. Create hash for the first time
    2. From the 2nd iteration, slide the window and find the hash value for the new window
    '''
    def create_hash(s_to_int, window_size):
        hash_value = 0
        for i in range(window_size):
            '''
            the below expression creates this sequence: s[0] * p^(l-1) + s[1] * p^(l-2) ... s[l-1] * p^0
            i = 0: hash_value = 0 * p + s[0]
            i = 1: hash_value = s[0] * p + s[1]
            i = 2: hash_value = (s[0] * p + s[1]) * p + s[2] => s[0] * p^2 + s[1] * p + s[2]
            ...
            i = l: hash_value = s[0] * p^l + s[1] * p^(l-1) + s[2] * p^(l-2) ... s[l]
            '''
            hash_value = hash_value * p + s_to_int[i]
        return hash_value

    def rolling_hash(prev_hash, prev_char, new_char):
        '''
        new_hash = p * (old_hash - first_char_in_window * (p ^ (l - 1))) + new_char
        => multiply by p: because neutralize the multiples of p
        '''
        hash_value = p * (prev_hash - prev_char * math.pow(p, l - 1)) + new_char
        return hash_value
    
    d = {'A': 0, 'C': 1, 'G': 2, 'T': 3}
    s_to_int = [d[i] for i in s]    # Convert the string into list of equilent integers
    n = len(s_to_int)
    p = 7
    q = math.pow(p, 10)
    seen, result = set(), set()
    hash_value = 0
    for i in range(n - l):
        if i == 0:
            # Create hash value for the first window of size l
            hash_value = create_hash(s_to_int, l)
        else:
            # Find the rolling hash for the next windows
            hash_value = rolling_hash(hash_value, s_to_int[i-1], s_to_int[i + l - 1])
        
        # if hash value is found in seen, which means the same string already exists
        if hash_value in seen:
            # add that string to the result
            result.add(s[i:i+l])
        else:
            # Add hash values to seen hashset to keep track of all the strings
            seen.add(hash_value)
        
    print(list(result))

if __name__ == '__main__':
    lst = [2, 2, 2, 2, 0, 2, 1, 2, 1, 2, 1, 1, 0, 0, 0, 0, 0]
    sort_three_colors(lst)

    lst = [3,2,2,4,1,5]
    cyclic_sort(lst)

    intervals = [[3,10], [6,8], [1,2], [5,15], [16,20]]
    merge_intervals(intervals)

    lst = [2,5,30,72,8]
    maximize_concatenation(lst)

    s = "a"
    longest_substring_non_unique_chars(s)

    list_of_strings = [
        "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT",
        "AAAAAAAAAAAAA"
    ]
    for s in list_of_strings:
        rabin_karp(s, 10)

    s = "this is              preetham. this is krishna"
    s += ' '
    # Create a function which takes a sentence
    def process_string(s):
        # Count the number of words
        lst_of_words = []
        curr_word = ''
        for c in s:
            if c.isalpha():
                curr_word += c
            elif c == ' ' and curr_word:
                print(curr_word)
                lst_of_words.append(curr_word)
                curr_word = ''
        print(lst_of_words)
        # Frequency
        counter = {}
        for word in lst_of_words:
            if word not in counter:
                counter[word] = 1
            else:
                counter[word] += 1
        print(counter)

        # print the most frequent word
        most_freq = 0
        most_freq_word = ''
        for word, freq in counter.items():
            if freq >= most_freq:
                most_freq = freq
                most_freq_word = word
        print(most_freq_word)

        # First char uppercase
        lst_of_words = [word.capitalize() for word in lst_of_words]
        print(lst_of_words)

        # Remove extra spaces
        # return ''.join(lst_of_words)
        result = ''
        for word in lst_of_words:
            result = result + ' ' + word
        return result.strip()
    
res = process_string(s)
print(res)

