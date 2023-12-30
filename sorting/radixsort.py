# Radix sort
# Use case: 

import time
def countingsort(lst, place):
    n = len(lst)
    result = [0] * n

    # counter of size 10 as digit exist only between 0 - 9
    counter = [0] * 10 
    
    # setup counter list
    for i in range(n):
        idx = lst[i]//place
        counter[idx % 10] += 1
    
    # find commulative
    for i in range(1, len(counter)-1):
        counter[i] += counter[i - 1]

    # sort the list based on the counter in the reverse order
    for i in range(n-1, -1, -1):
        idx = lst[i]//place
        result[counter[idx % 10] - 1] = lst[i]
        counter[idx % 10] -= 1

    for i in range(n):
        lst[i] = result[i]

def radixsort(lst):
    place = 1
    max_ele = max(lst)
    while max_ele//place:
        countingsort(lst, place)
        place *= 10
    return lst

if __name__ == '__main__':
    lst = [21,43,12,23,1,3,65,0,2,3]
    print('----------Radix Sort-----------')
    print(f'Before:{lst}')

    start = time.time()
    lst = radixsort(lst)
    end = time.time()
    et = (end-start)*10**3
    print(f'Execution Time: {et}')

    print(f'After: {lst}')