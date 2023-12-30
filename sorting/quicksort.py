# Quick Sort
import time

def quicksort(lst, left, right):
    if left >= right: return lst
    piv = partition(lst, left, right)
    quicksort(lst, left, piv - 1)
    quicksort(lst, piv + 1, right)
    return lst

def partition(lst, left, right):
    pivot = right
    i = j = left
    while j < right:
        if lst[j] <= lst[pivot]:
            lst[i], lst[j] = lst[j], lst[i]
            i += 1
        j += 1
    lst[i], lst[pivot] = lst[pivot], lst[i]
    return i

def quicksort_alg(lst):
    start = time.time()
    lst = quicksort(lst, 0, len(lst)-1)
    end = time.time()
    et = (end-start)*10**3
    print(f'Execution Time: {et}')
    print(f'After: {lst}')
    return lst, et

if __name__ == '__main__':
    print('--------------Quick Sort---------------')
    lst = [21, 43, 12, 23, 1, 3, 65, 0, 2, 3, 9]
    print(f'Before: {lst}')
    quicksort_alg(lst)

'''
Pseudo Code
partition the list at pivotal position and sort

recussive function (lst, low, high):
    pivotal_position = partition(lst, low, high)
    recur(lst, low, pivotal_position - 1)
    recur(lst, pivotal_position + 1, high)
    return lst

partition(lst, low, high):
    pivot_element = high
    i = low
    for current_element = low : high
        if lst[current_element] < lst[pivot_element]:
            swap lst[i], lst[current_element]
            i += 1
    swap lst[i], lst[pivot_element]
    return i
'''