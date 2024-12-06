"""
Heap Queue or priority queue
1. It returns value which has the top priority
2. Min-heap - returns minimum value in O(1) time and vice versa for max-heap
3. popping min/max element will cost O(logN) time, 
    1. As the min/max element swaps with last element in O(1) time
    2. Rearranging all the elements again to satisfy the min/max-heap property takes O(logN) time
4. Used in Dijkstras algorithm, to retrieve shortest distance in O(1) time
5. It is a Complete tree - meaning, tree is constructed from left to right - all the nodes will have 2 children except for the nodes in the last level
6. When Heap tree is in the form of array, we can access left and right elements of a node as (2*i + 1, 2*i + 2) for 0-indexed
7. Heap sort is not stable because it changes the relative order of the equivalent keys
8. Scheduling periodic tasks, merging logging files
"""

class Heapq:
    
    def heapSort(self): # O(NlogN)
        N = len(self.array)
        for i in range(N//2 - 1, -1, -1): # O(N/2 * log(N/2))
            self.heapify(i, N)
        
        for i in range(N-1, 0, -1): # This is where sorting happens, which is similar to seletion sort
            self.array[i], self.array[0] = self.array[0], self.array[i]
            self.heapify(0, i)

    # This function makes sure all the elements follows min-heap property
    def rearrange(self, array, i, N): # O(logN)
        smallest = i
        left = 2*i + 1
        right = 2*i + 2
        if left < N and array[smallest] > array[left]:
            smallest = left
        if right < N and array[smallest] > array[right]: # we compare the original smallest index or value at left
            smallest = right
        if smallest != i: # if smallest index at this point changes, then heap tree got distrubed
            array[smallest], array[i] = array[i], array[smallest]
            self.rearrange(array, smallest, N)
        
    def heapify(self, array):
        n = len(array)
        for i in range(n//2, -1, -1):
            self.rearrange(array, i, n)

    def heappush(self, array, value):
        array.append(value) # O(1)
        self.heapify(array)

    def heappop(self, array):
        if array:
            value = array.pop(0)
            self.heapify(array) # O(logN)
            return value
        return -1
    
    def peek(self, array):
        self.heapify(array)
        return array[0]

    def nsmallest(self, array, k): # O(k)
        if not array:
            return []
        res = []
        for _ in range(k):
            val = self.heappop(array)
            res.append(val)

        for ele in res:
            self.heappush(array, ele) # O(k.logN)
        return res

if __name__ == '__main__':
    lst = [4,45,32,3,5,1,5,3,2]
    print(f'Before heap sort: {lst}')
    heapq1 = Heapq()
    heapq1.heapify(lst)
    heapq1.heappush(lst, -10)
    p = heapq1.heappop(lst)
    print(p)
    print(lst)
    print(heapq1.peek(lst))
    print(heapq1.nsmallest(lst, 10))