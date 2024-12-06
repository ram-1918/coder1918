"""
STACKS
1. LIFO
2. insert, pop, peek
3. Patterns - going back and forth, before adding to the stack check with the top element for maintaing monotonicity
4. Any recursive problem can be implemented iteratively using a stack
"""

class Stack:
    def __init__(self):
        self.stack = []
    
    def insert(self, value):
        if not self.stack:
            self.stack.append((value, value))
        else:
            min_value = self.stack[-1][1]
            self.stack.append((value, min(value, min_value)))
    
    def pop(self):
        if self.stack:
            return self.stack.pop()
        return -1
    
    def peek(self):
        if self.stack:
            return self.stack[-1]
        return -1
    
    def minValue(self):
        if self.stack:
            return self.stack[-1][1]
    
    def clear(self):
        self.stack = []

if __name__ == '__main__':
    s = Stack()
    lst = [3,4,2,4,2,23,10,42,11,5,2,6,1]
    for value in lst:
        s.insert(value)
    print(s.minValue())
    print(s.peek())
    s.pop()
    print(s.minValue())
    print(s.peek())

'''
Enhancements - on top of the above naive implementation
1. Find minimum/maximum element simultanously while adding to the stack
2. Check if data stream follows Monotoic property
'''
