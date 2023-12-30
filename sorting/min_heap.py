# Min Heap Sort
import time
class heapsort():
    def __init__(self, lst):
        self.lst = lst
        self.n = len(lst)
    
    def heapify(self, i, n):
        smallest = i
        left = i * 2 + 1
        right = i * 2 + 2

        if left < n and self.lst[left] < self.lst[smallest]:
            smallest = left
        if right < n and self.lst[right] < self.lst[smallest]:
            smallest = right
        if smallest != i:
            self.lst[smallest], self.lst[i] = self.lst[i], self.lst[smallest]
            self.heapify(smallest, n)

    def sort(self):
        # min-heap is being initilized which means it once heapifies the whole tree making the array ready for sorting
        for i in range(self.n//2 - 1, -1, -1):
            self.heapify(i, self.n)
        
        # the sorting happens here by swapping the root node with the ith node, to make sure elements are positioned correctly
        for i in range(self.n - 1, -1, -1):
            self.lst[0], self.lst[i] = self.lst[i], self.lst[0]

            # makes sure it starts heapifing from the root node
            self.heapify(0, i)

lst = [21,42,1,3,3,6,8,32,53,123,647,57,4242,354,3]
sort_obj = heapsort(lst)
print('Min-Heap Sort')
print(sort_obj.lst)
start = time.time()

sort_obj.sort()

end = time.time()
print(sort_obj.lst)
print(f'Execution Time: {(end - start)*10 ** 3}')


