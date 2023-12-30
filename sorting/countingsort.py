# Counting sort
# Use case: 

import time

def countingsort(lst):
    n = len(lst)
    max_ele = max(lst)
    counters = [0 for _ in range(max_ele+1)]
    result = [0 for _ in range(n)]

    # create a list to keep track of the elements and its count
    for i in range(n):
        counters[lst[i]] += 1
    
    # update the counters list with a cummulative sum
    csum = 0
    for i in range(len(counters)):
        counters[i] += csum
        csum = counters[i]
    
    # create resulatant list with values at counters[lst[i] - 1] index (which is the count of lst[i]th element)
    for i in range(n):
        result[counters[lst[i]] - 1] = lst[i]
        counters[lst[i]] -= 1
    return result

if __name__ == '__main__':
    lst = [21,43,12,23,1,3,65,0,2,3]
    print('----------Bubble Sort-----------')
    print(f'Before:{lst}')

    start = time.time()
    lst = countingsort(lst)
    end = time.time()
    et = (end-start)*10**3
    print(f'Execution Time: {et}')

    print(f'After: {lst}')