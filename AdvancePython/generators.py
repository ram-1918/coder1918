''' Generators
1. These are special kind of functions, they yield values instead of returning them all. 
    1.1 They are converted an iterable object.
2. They can be used for efficient and lazy evaluation.
3. They use yield keyword to yield values.
4. They are efficient in terms of memory consumption
'''
from decorators import CalculateMemory

class GeneratorFromScratch:
    def __init__(self, n):
        self.a = 0
        self.b = 1
        self.n = n
    
    def __next__(self):
        return self.next()
    
    def next(self):
        if self.a < self.n:
            self.a, self.b = self.b, self.a + self.b
            return self.a
        raise "Limit reached"

# With generator
@CalculateMemory
def fibonacci_generator(n):
    a, b = 0, 1
    while a < n:
        yield a
        a, b = b, a + b

# Without generator
@CalculateMemory
def fibonacci_generator_without(n):
    a, b = 0, 1
    lst = []
    while a < n:
        a, b = b, a + b
        lst.append(a)

if __name__ == '__main__':
    val = fibonacci_generator(100000)
    result1 = fibonacci_generator_without(100000)
    print(next(val))
    print(next(val))


