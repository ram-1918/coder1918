import time

def calcTime(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        res = func(*args, **kwargs)
        end = time.time()
        print(f'{func}: {(end - start) * 10**5}')
        return res
    return wrapper

@calcTime
def Algorithm1(arr):
    if len(arr) == 1:
        return arr[0]
    best = float('-inf')
    n = len(arr)
    for i in range(n):
        for j in range(n):
            total = 0
            for k in range(i, j + 1):
                total += arr[k]
            best = max(best, total)
    return best

@calcTime
def Algorithm2(arr):
    if len(arr) == 1:
        return arr[0]
    best = float('-inf')
    n = len(arr)
    for i in range(n):
        total = 0
        for j in range(i, n):
            total += arr[j]
            best = max(best, total)
    return best

@calcTime
def Kadanes(arr):
    current_sum = best_sum = 0
    for num in arr:
        current_sum = max(num, current_sum + num)
        best_sum = max(best_sum, current_sum)
    return best_sum




if __name__ == '__main__':
    # arr = [-1, 2, 4, -3, 5, 2, -5, 2]
    arr = [-2,1,-3,4,-1,2,1,-5,4]
    result1 = Algorithm1(arr)
    result2 = Algorithm2(arr)
    result_kadane = Kadanes(arr)
    print(result1, result2, result_kadane)