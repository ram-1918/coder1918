# Merge Sort - Divide and conquor
import time

def divide(lst):
    if len(lst) <= 1: return lst
    mid = len(lst)//2
    left, right = lst[ : mid], lst[mid : ]
    divide(left)
    divide(right)
    # print('Before ', lst)
    conquor(left, right, lst)
    # print('After ', lst)
    return lst

def conquor(l1, l2, lst):
    i = j = k = 0
    while i < len(l1) and j < len(l2):
        if l1[i] >= l2[j]:
            lst[k] = l2[j]
            j += 1
        else:
            lst[k] = l1[i]
            i += 1
        k += 1
    while i < len(l1):
        lst[k] = l1[i]
        i += 1
        k += 1
    while j < len(l2):
        lst[k] = l2[j]
        j += 1
        k += 1

def mergesort_alg(lst):
    start = time.time()
    lst = divide(lst)
    end = time.time()
    et = (end-start)*10**3
    print(f'Execution Time: {et}')
    print(f'After: {lst}')
    return lst, et

if __name__ == '__main__':
    print('--------------Merge Sort---------------')
    lst = [21, 43, 12, 23, 1, 3, 65, 0, 2, 3]
    print(f'Before: {lst}')
    mergesort_alg(lst)



'''
Pseudo Code
recursively divide the list at the mid index and conquor elements by comparing and merging elements

recursive_function(lst):
    if len(lst) == 1: return lst
    mid = len(lst)//2
    left_half, right_half = lst[ : mid], lst[mid : ]
    recursive_function(left_half)
    recursive_function(right_half)
    conquor(lst, left_half, right_half)
    return lst

conquor(lst, left_half, right_half):
    i = j = k = 0
    while i less than length(left_half) and j less than length(right_half):
        if left_element is greater than right_elenent:
            assign lst[k] = left_element
            increment left_element
        else:
            assign lst[k] = right_element
            increment right_element
    
    # handling remaining elements of each halfs

    while i is still less than length(left_half):
        assign lst[k] = left_element
        increment left_element
    while j is still less than length(right_half):
        assign lst[k] = right_element
        increment right_element
'''