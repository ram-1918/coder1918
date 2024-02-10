""" Context Managers
1. Memory leak:
    A Kind of issue encounters when external resources like files, network connections are created and opened, 
    but not closed before opening a new one.
2. Context managers are not only useful for resource management but also for reusing of common setup and teardown code
    like 
    open and close connections, 
    start and stop, 
    enter and exit, 
    change and reset, 
    create and delete, 
    lock and release
3. It is like a decorator which doesnt modify the logic but enhances it.
"""


class CustomFileManager:
    def __init__(self, file):
        self.file = file
        self.fileObj = None

    def __enter__(self):
        # create connection
        self.fileObj = open(self.file, 'r')
        print('Connection started')
        # This returned value can be accessed inside the with block from 'as file'
        return self.fileObj

    def __exit__(self, exe_type, exe_value, exe_tb):
        # clear connection
        print('Starting to close the connection')
        if isinstance(exe_value, AttributeError):
            print(f'Attribute {exe_type} not found')
            print(f'Error type: {exe_value}')
            return True  # This helps to handle exception, break, and continue to the next step
        if self.fileObj:
            self.fileObj.close()
            print('Connection stopped')


with CustomFileManager('./decorators.py') as file:
    print('File Reads/Writes are handled here', file.value)
print('Continue Normally')


''' try...finally block to implement threading lock

import threading
balance_lock = threading.Lock()

balance_lock.acquire()
print(balance_lock)
try:
    print('Update Balance here')
finally:
    balance_lock.release()
print(balance_lock)
'''

''' With pattern to implement threading lock

import threading
balance_lock = threading.Lock()

with balance_lock:
    print(balance_lock)
    print('Update balance in With')
    # balance_lock.release()
print(balance_lock)
'''
