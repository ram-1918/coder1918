"""
Queues
1. FIFO
2. Process elements in order
3. enqueue, dequeue, pop, peekFront, peekRear
4. Priority queues, Heap Queues
"""

class Queue:
    def __init__(self, k):
        self.queue = []
        self.k = k
    
    def enqueue(self, value):
        self.queue.append(value)
        if len(self.queue) > self.k:
            self.dequeue()
    
    def dequeue(self):
        if self.queue:
            return self.queue.pop(0)
        return -1
    
    def peekFront(self):
        if self.queue:
            return self.queue[0]
        return -1
    
    def peekRear(self):
        if self.queue:
            return self.queue[-1]
        return -1
    
    def clear(self):
        self.queue = []

if __name__ == '__main__':
    k = 3
    q = Queue(k)
    lst = [3,4,2,4,2,23,10,42,11,5,2,6,1]
    for value in lst:
        q.enqueue(value)
        print(q.queue)
    

'''
Enhancements - on top of the above naive implementation
1. BFS - Uses a queue behind scenes
2. Maintain queue size of k
'''
