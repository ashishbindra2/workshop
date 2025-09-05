import time
def time_deco(func):
    def time_cal():
        st = time.perf_counter()
        result = func()
        end = time.perf_counter()
        print(func.__name__,end-st)
        return result
    return time_cal

@time_deco
def names():
    return ("ashish bindra")
  
names()  
print(names())