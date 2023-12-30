# Selection Sort
import time

def selectionsort(lst):
    i = 0
    start = time.time()
    while i < len(lst) - 1:
        idx = i + 1
        small_idx = i + 1
        while idx < len(lst):
            if lst[idx] <= lst[small_idx]:
                small_idx = idx
            idx += 1
        lst[small_idx], lst[i] = lst[i], lst[small_idx]
        i += 1
    end = time.time()
    et = (end-start)*10**3
    print(f'Execution Time: {et}')
    return lst, et

if __name__ == '__main__':
    print('---------Selection Sort----------')
    lst = [21, 43, 12, 23, 1, 3, 65, 0, 2, 3]
    print(f'Before: {lst}')
    lst, _ = selectionsort(lst)
    print(f'After: {lst}')

'''
Pseudo Code
initialize lst: list of unsorted elements
initialize i = 0
while i < length(lst) - 1:
    initialize current_index = i + 1
    initialize small_index = i + 1
    while current_index < length(lst):
        if lst[current_index] <= lst[small_index]:
            small_index = current_index
        increment current_index + 1
    swap lst[i], lst[small_index]
    increment i + 1
'''