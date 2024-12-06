def fib(num):
    # Base case
    if num <= 0:
        return 1
    if num in cache:
        return cache[num]
    breakpoint()
    
    val1 = fib(num - 1)
    val2 = fib(num - 2)

    cache[num] = val1 + val2
    return cache[num]

cache = {}
fib(4) # 1, 1, 2, 3, 5, 8

# n -> next line, c -> next breakpoint, s -> go inside