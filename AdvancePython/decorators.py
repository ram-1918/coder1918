''' Decorators
Enhance/modify the behavior of a function without altering its functionality
'''
import tracemalloc

class CalculateMemory:
    def __init__(self, func):
        self.function = func
    
    def __call__(self, *args, **kwargs):
        tracemalloc.start()
        val = self.function(*args, **kwargs)
        print(tracemalloc.get_traced_memory())
        tracemalloc.stop()
        return val