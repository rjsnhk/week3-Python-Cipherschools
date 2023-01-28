from functools import wraps
import time
def calculate_time(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        print(f'Executing .... {function.__name__}')
        t1=time.time()
        returned_value = function(*args, **kwargs)
        t2 = time.time()
        total_time = t2-t1
        print(f'This function took {total_time} seconds')
        return returned_value
    return wrapper
    
@calculate_time
def square_finder(n):
    return [i**2 for i in range(1,n+1)]

square_finder(1000)