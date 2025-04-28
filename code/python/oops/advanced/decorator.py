import time
from functools import wraps

def timing_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args,**kwargs)
        end = time.time()
        print(f"{func.__name__} took {end - start:.2f} seconds to execute")
        return result
    return wrapper

@timing_decorator           #put in the function that need to check time
def slow_function():
    time.sleep(2)
    print("function executed")

@timing_decorator
def fast_function():
    print("function executed")
    
slow_function()
# function executed
# slow_function took 2.00 seconds to execute
fast_function()
# function executed
# fast_function took 0.00 seconds to execute