# TIME

## EXAMPLES

### 73. Python Program to Measure the Elapsed Time in Python

```py
# Example 1: Using time module
import time

# Save timestamp
start = time.time()

print(23*2.3)

# Save timestamp
end = time.time()

print(end - start)
```

```py
# Example 2: Using timeit module
from timeit import default_timer as timer

start = timer()

print(23*2.3)

end = timer()
print(end - start)
```

### 93. Python Program to Create a Countdown Timer

```py
import time

def countdown(time_sec):
    while time_sec:
        mins, secs = divmod(time_sec, 60)
#         print(mins,secs)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        print(timeformat, end='\r')
        time.sleep(1)
        time_sec -= 1

    print("stop")

countdown(5)
```

```py
import time

n = 5
while n:
    
    print(n,end="\r")
    time.sleep(1)
    n-=1
print("0")
```
