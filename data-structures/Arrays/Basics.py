# camelCase for functions and variable names

''' 
Complexities 
> access, inteserting at end, deleting from the end, updating by index: O(1)
> traversing, searching, deleting from start or middle, inserting at start or middle, resizing(internal operation, amortized): O(n)
> slicing, extending: O(k), k is the slice length or size of the extending list
> concatenating: O(m + n)

Algorithms 
> Sorting: Bubble, quick, merge, insertion, selection, bucket, counting, circular, Heap
> Searching: Linear, Binary
> Rotations, Merging, Partitioning
> Circular arrays
'''

''' List Methods
lst.append(), lst.insert(position, element), lst.remove(element), lst.pop(position),
lst.index(element), lst.clear(), lst.extend(newList), lst.reverse(), lst.sort(),
lst.copy(), lst.count(element)
'''

''' lists
Limitations:
> 'array' module to implement arrays: fixed size, single data type
> lists are dynamic and so there will be a memory overhead, so these are not memory efficient
> access time: O(1), insertion and deletion: O(n) because it needs to shift elements

Trade-offs:
> lists are flexible so comes with memory overhead and less performant
> arrays from 'array' module or numpy arrays are less flexible but are more memory efficient and performant

Edge-cases: 
> index-out-of-bounds, accessing elements during iteration, 
> empty lists, lists with one value, all -ve values, all 0's, 
> -ve indices, immutable elements in lists, shallow vs deep copy, resizing(costly operation)
'''

array = [0, 1, 2, 3, 4]
twoDArray = [
    [0,1,2,3],
    [4,5,6,7],
    [8,9,10,11],
    [12,13,14,15],
    ]

''' Indexing 
[1, 2, 3, 4]
0  1. 2. 3                # Forwards
-4 -3 -2 -1               # Backwards
-n -(n-1) -(n-2) -(n-4)   # replace n with length of the array
'''

''' Slicing 
slice: a[start: end: step]

If we need first k elements use [:k], for last k elements: [-k:]

Think of -ve indices as alias for normal indexing; Rest everthing is the same.
'''
deepCopiedArray = array[:]   # deepCopy

# Retrieve all even indexed values: 0, 2, 4...
evenIndexedValues = array[::2]
print(evenIndexedValues)

# Retrieve all odd indexed array values
oddIndexedValues = array[1::2]
print(oddIndexedValues)

# Retrieve every nth element from the list
nthElement = array[::5]
print(f'Nth element: {nthElement}')

# -ve slicing
print(f'-5 == 0; -1 == last element: {array[-5: -1]}')

# Reverse an array
reversedArray = array[::-1]

# Extracting subarrays
# Subarrays: contiguous subsets of an array: [1], [1,2], [1,2,3], [1,2,3,4], [2], [2,3], [2,3,4], [3], [3,4], [4]
# arraySize = 4; possibleSubarrays = 10; formula = (n * (n + 1)) // 2
subArrays = []
n = len(array)
for i in range(n):
    for j in range(i+1, n):
        subArrays.append(array[i:j])
print(f'Total subarrays possible for array size {len(array)} is: {len(subArrays)}\nSubarray list: {subArrays}')

# Extract first 3 elements from all rows
print(twoDArray[1][-3:])

# Flattening a matrix
# [(col, element) for col in zip(*matrix) for element in col]
m, n = len(twoDArray), len(twoDArray[0])
flattenedArray = [element for col in zip(*twoDArray) for element in col]
print(twoDArray)
print(flattenedArray)

# Transpose: array[i][j] = array[j][i]
# Method 1: [[twoDArray[i][j] for i in range(m)] for j in range(n)]
# Method 2: list(zip(*twoDArray)) also gives the same result
transposedArray = [[twoDArray[i][j] for i in range(m)] for j in range(n)]    
print(transposedArray)

# Extract diagonal elements of a matrix
diagonalElements = [twoDArray[i][j] for i in range(m) for j in range(n) if i == j]
print(f'Diagonal elements: {diagonalElements}')

# Extract right diagonal elements of a matrix
rightDiagonalElements = [twoDArray[i][j] for i in range(m) for j in range(n) if i == (n - j - 1)]
print(f'Right Diagonal elements: {rightDiagonalElements}')

# Extract lower triangle elements
lowerTriangle = [twoDArray[i][j] for i in range(m) for j in range(n) if i > n - j - 1]
print(f'Lower Triangle: {lowerTriangle}')

# Extract lower triangle Matrix
lowerTriangleMatrix = [[twoDArray[i][j] if i > n - j - 1 else 0 for j in range(n)] for i in range(m)]
print(f'Lower Triangle Matrix: {lowerTriangleMatrix}')

# Extract upper triangle elements
upperTriangle = [twoDArray[i][j] for i in range(m) for j in range(n) if i < n - j - 1]
print(f'Upper Triangle: {upperTriangle}')

# Extract upper triangle matrix
upperTriangleMatrix = [[twoDArray[i][j] if i < n - j - 1 else 0 for j in range(n)] for i in range(m)]
print(f'Upper Triangle Matrix: {upperTriangleMatrix}')


''' Array Rotations

Rotate list n times RIGHT
2 times right: [0,1,2,3,4] => [4,0,1,2,3] => [3,4,0,1,2]

array of length 5
i = 0, i = 5, i = 10 => i % 5 = 0
i = 1, i = 6, i = 11 => i % 5 = 1
...
rotate 1 time => (i + 1) % 5
rotate 2 times => (i + 2) % 5
i = 0,1,2,3,4
i + 1 => 1, 2, 3, 4, 5 => 1,2,3,4,0
i + 2 => 2, 3, 4, 5, 6 => 2,3,4,0,1
'''
# This method uses extra space
n = len(array)
rotatedArray = [0] * n
for i in range(n):
    rotatedArray[(i+1) % n] = array[i]
print(rotatedArray)

# Or

# This method uses slicing
rotations = 2
rotatedArray = array[-rotations:] + array[:-rotations]    # Last n elements + first n elements
print(rotatedArray)


# Partition array into chunks
n = len(array)
k = 3
kChunks = [array[i:i+k] for i in range(0, n, k)]
print(f'{k}-sized chunks: {kChunks}')

# Check monotonic array

def isMonotonic(array):
    increasing = decreasing = True
    n = len(array)
    for i in range(n - 1):
        if array[i] > array[(i + 1) % n]:
            increasing = False
        if array[i] < array[(i + 1) % n]:
            decreasing = False
    return increasing or decreasing

print(f'is {array} Monotonic? {isMonotonic(array)}')

''' Circular arrays '''
# Circular maximum subarray sum
def kadane(array):
    maximumSum = currentSum = array[0]
    for num in array[1:]:
        currentSum = max(currentSum + num, num)
        maximumSum = max(maximumSum, currentSum)
    return maximumSum

# Maximum subarray sum of the inverted array is indeed the minimum subarray sum of the original array
# By inverting the array we can find the minimum subarray sum of original array
# Non-wrapping case: Compute the total sum and subtract the minimum subarray sum
# Edge case if all the elements are -ve

array = [1, -2, 3, -2]
minSubarraySum = kadane([-x for x in array])
maximumSubarraySum = max(kadane(array), sum(array) - minSubarraySum)
print(maximumSubarraySum, sum(array), minSubarraySum)

# Next greater element in a circular array
def nextGreaterElement(array):
    newarray = array
    n = len(newarray)
    result = [-1] * n
    stack = []
    for i in range(2 * n - 1, -1, -1):
        while stack and newarray[stack[-1]] < newarray[i % n]:
            idx = stack.pop()
            result[idx % n] = newarray[i % n]
        stack.append(i % n)
    return result

print(nextGreaterElement(array))

# Check circular array is the rotation of other
def checkIsRotated(array1, array2):
    if len(array1) != len(array2):
        return False
    
    ''' Method 1
    n = len(array1)
    for k in range(n):
        if array1 == array2[-k:] + array2[:-k]:
            return True
    return False
    '''

    ''' Method 2 '''
    return ''.join(map(str, array1)) in ''.join(map(str, array1 + array2))


print(checkIsRotated([1, 2, 3, 4], [3, 4, 1, 2]))

# Minimum element in a rotated sorted array
def findMinimumElement(array):
    n = len(array)
    left, right = 0, n - 1
    while left < right:
        mid = (left + right) // 2
        if array[mid] > array[right]:
            left = mid + 1
        else:
            right = mid
    return array[left]

array = [4, 5, 6, 7, 0, 1, 2]
print(findMinimumElement(array))

# Maximum element in a rotated sorted array
def findMaximumElement(array):
    n = len(array)
    left, right = 0, n - 1
    while left <= right:
        mid = (left + right) // 2
        if array[mid] > array[left]:
            left = mid
        else:
            right = mid - 1
    return array[left]

array = [4, 5, 6, 7, 8, 9, 10, 0, 1, 2]
print(findMaximumElement(array))