"""Algorithm
1. Read data from the file
2. Sort the keys of the data in ASC order
3. Construct a pyramid and during this process, extract the last element from each line of the pyramid-like structure
4. Map the collected numbers to the words and return it
"""

# This method extracts data from the file
def extract_data(file):
    data = {}
    # use with context manager, as it makes sure the file is closed after its done
    with open(file, 'r') as f:
        for line in f.readlines():
            # for each line strip leading and trailing spaces if any and split the line on the space between them
            idx, word = line.lower().strip().split()
            # Store the data in a hashmap
            data[int(idx)] = word
    return data

# 1 2 3 4 5 6

def decode(message_file):
    # invoke the extract function declared above
    data = extract_data(message_file)
    # Initialize step, result and temp variables
    step = 1
    result, temp = [], []
    # Iterate over the sorted indices
    for idx in sorted(data):
        # if the length of the temp is the step then 
        # add the last element in the pyramid to result re-initialize temp
        # increament step
        if len(temp) == step:
            result.append(temp[-1])
            temp = []
            step += 1
        # otherwise add idx to the temp
        temp.append(idx)

    # append the last element that is created during the last iteration
    if len(temp) == step:
        result.append(temp[-1])

    # Join and return the result
    return ' '.join([data[idx] for idx in result])


if __name__ == '__main__':
    res = decode('test.txt')
    print(res)

