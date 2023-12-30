# Bucket sort
# Usecase: larger datasets with limited range of values

import time

def bucketsort(lst):
    max_ele_idx = max(lst)//10 + 1
    buckets = [[] for i in range(max_ele_idx)]

    for i in range(len(lst)):
        idx = lst[i]//10
        buckets[idx].append(lst[i])

    for i in range(max_ele_idx):
        buckets[i] = sorted(buckets[i])
    
    res = []

    for i in range(max_ele_idx):
        res.extend(buckets[i])

    return res

if __name__ == '__main__':
    lst = [21,43,12,23,1,3,65,0,2,3]
    print('----------Bubble Sort-----------')
    print(f'Before:{lst}')

    start = time.time()
    lst = bucketsort(lst)
    end = time.time()
    et = (end-start)*10**3
    print(f'Execution Time: {et}')

    print(f'After: {lst}')

'''
Pseudo Code
lst: list of unsorted elements
max_ele_indx: maximum number of buckets based on largest number in lst
Initialize buckets: create a list  with empty sublists of size max_ele_lst
for each element in lst:
    find index for each element with lst[i]//10
    append the element at the appropriate bucket index

for each bucket in buckets:
    replace each bucket with the sorted one

for each bucket in buckets:
    add elements to the resulted_list bucket-wise

'''