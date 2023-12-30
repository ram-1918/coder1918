# Max Heap sort
import time
def max_heapsort(lst, i, n):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2
    # left < n or right < n to check if the newly assigned left is with in the length of the list
    # finds the largest element among parent, left and right childs
    if left < n and lst[left] > lst[largest]:
        largest = left
    if right < n and lst[right] > lst[largest]:
        largest = right
    # Base case: if largest element doesn't change which is equal to i, recurssion breaks
    # when node i is passed to heapify, it checks its left and right childs and continues to the leaf nodes 
    # until the elements are heapified
    if largest != i:
        lst[largest], lst[i] = lst[i], lst[largest]
        max_heapsort(lst, largest, n)

# tip: since lists are mutable and using swap and in-place sorting, there is no need of additional memory (list/array) beyond the original list
lst = [21,42,1,3,3,6,8,32,53,123,647,57,4242,354,3]
print(f'Before: {lst}')
n = len(lst)
start = time.time()

for i in range(n//2 - 1, -1, -1):
    max_heapsort(lst, i, n)
    
for i in range(n-1, -1, -1):
    lst[0], lst[i] = lst[i], lst[0]
    max_heapsort(lst, 0, i)

end = time.time()
print(f'After: {lst}')
print(f'Execution Time: {(end-start)*10**3}')
