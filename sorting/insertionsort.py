# Insertion Sort
import time

def insertionsort(lst):
    i = 0
    start = time.time()
    while i < len(lst)-1:
        j = i
        while lst[j] > lst[j+1] and j >= 0:
            lst[j], lst[j+1] = lst[j+1], lst[j]
            j -= 1
        i += 1
    end = time.time()
    et = (end-start)*10**3
    print(f'Execution Time: {et} ms')
    return lst, et

if __name__ == '__main__':
    lst = [21, 43, 12, 23, 1, 3, 65, 0, 2, 3]
    print('----------Insertion Sort-----------')
    print(f'Before:{lst}')
    lst, _ = insertionsort(lst)
    print(f'After: {lst}')

'''
Pseudo Code:
lst: list of unsorted elements
initialize i = 0
# iterate through end of the list
while i < lenght(lst):
    #  iterating backwards until left_element > right_element and j is positive
    initialize j = i
    while lst[i] > lst[i+1] and j >= 0:
        swap lst[i], lst[i+1]
        decrement j
    increment i
'''