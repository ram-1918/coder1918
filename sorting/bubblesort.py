# Bubble sort
import time

def bubblesort(lst):
    start = time.time()
    while True:
        i = 0
        flag = 0
        while i < len(lst) - 1:
            if lst[i] > lst[i+1]:
                lst[i], lst[i+1] = lst[i+1], lst[i]
                flag = 1
            i += 1
        if flag == 0:
            break
    end = time.time()
    et = (end-start)*10**3
    print(f'Execution Time: {et}')
    return lst, et

if __name__ == '__main__':
    lst = [21,43,12,23,1,3,65,0,2,3]
    print('----------Bubble Sort-----------')
    print(f'Before:{lst}')
    lst, _ = bubblesort(lst)
    print(f'After: {lst}')

'''
Pseudo Code
lst: list of unsorted elements
while True: # infinate loop
    initialize i = 0
    initailize flag = 0
    while i < length(lst):
        if lst[i] > lst[i+1]:
            swap lst[i], lst[i+1]
        i += 1
    # to check if the elements gone through swapping if not all are sorted so break out
    if flag == 0: break
'''