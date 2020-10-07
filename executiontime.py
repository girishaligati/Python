'''Functions for checking the execution time of a program using the With statments'''

import time

class ExecutionTime(object):
    def __init__(self):
        pass
    def __enter__(self):
        self.time_started = time.time()
    
    def __exit__(self,exception_type, exception_value, traceback):
        self.time_ended = time.time()
        print("Time taken to execute the with block - "+str(self.time_ended - self.time_started))

with ExecutionTime():
    for i in range(10):
        print(i)
        time.sleep(0.1)
    