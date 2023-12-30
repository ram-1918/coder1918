# Priority Queue
import time

class PriorityQueue:
    def __init__(self, lst):
        self.lst = lst
    
    def heapify_up(self, idx):
        parent = ( idx - 1 ) //2
        while idx > 0 and self.lst[idx] < self.lst[parent]:
            self.lst[idx], self.lst[parent] = self.lst[parent], self.lst[idx]
            idx = parent
            parent = ( idx - 1 ) // 2
            print('dfew', self.lst)

    def heapify_down(self, i, n):
        largest = i
        left, right = i*2 + 1, i*2 + 2
        print(largest, i, left, right)
        if left < n and self.lst[left] > self.lst[largest]:
            largest = left
        if right < n and self.lst[right] > self.lst[largest]:
            largest = right
        if largest != i:
            self.lst[largest], self.lst[i] = self.lst[i], self.lst[largest]
            self.heapify_down(largest, n)
    
    def heapsort(self):
        n = len(self.lst)
        for i in range(n//2, -1, -1):
            self.heapify(i, n)
        
        for i in range(n-1, -1, -1):
            self.lst[0], self.lst[i] = self.lst[i], self.lst[0]
            self.heapify(0, i)
    
    def insert(self, val):
        # insert at the end of the list
        # heapify
        n = len(self.lst)
        if not n: self.lst.append(val)
        else: 
            self.lst.append(val)
            for i in range((n // 2) - 1, -1, -1):
                self.heapify_down(i, n)

    def pop(self, idx):
        # find the element to be deleted and swap it with right most leaf node
        # heapify
        
        pass

    def peak(self):
        # return the root value
        pass

# lst = [21,42,1,3,3,6,8,32,53,123,647,57,4242,354,3]
pq = PriorityQueue([])
print(pq.lst)
pq.insert(10)
pq.insert(12)
pq.insert(21)
pq.insert(2)
pq.insert(1)
pq.insert(210)
print(pq.lst)

# decorator to find time
# def cal_time(func):
#     start = time.time()
#     func()
#     end = time.time()
#     print((end - start)*10**3)

# @cal_time
# def test():
#     print('fred')

