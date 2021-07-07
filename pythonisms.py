  
import functools
import time

def slow_down(func):
  
    @functools.wraps(func)
    def wrapper_slow_down(*args, **kwargs):
        time.sleep(1)
        return func(*args, **kwargs)
    return wrapper_slow_down

@slow_down 
def fac2(nums): 
    output = [ ]
    for k in range(1,nums+1):
        if nums % k == 0: output.append(k)
    return output

@slow_down
def fac(nums):  
    for k in range(1,nums+1):
        if nums % k == 0: 
            yield k

print(fac2(100))

for factor in fac(100):
    print(factor)
