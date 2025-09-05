# Random module

## EXAMPLES

### 7. Python Program to Generate a Random Number

```py
# Program to generate a random number between 0 and 9

# importing the random module
import random

print(random.randint(0,9))

```

```py
from random import randint,random

randint(1,11)
```

```py
from random import randint,random

randint(1,11)
```

```py
random_float = random()*10
random_float
```

### 66. Python Program to Randomly Select an Element From the List

```py
# Example 1: Using random module
import random

my_list = [1, 'a', 32, 'c', 'd', 31]
print(random.choice(my_list))
```

```py
# Example 2: Using secrets module
import secrets

my_list = [1, 'a', 32, 'c', 'd', 31]
print(secrets.choice(my_list))
```

```py
import random

my_list = [1, 'a', 32, 'c', 'd', 31]
print(random.choices(my_list))
```

```py
import random

my_list = [1, 'a', 32, 'c', 'd', 31]
print(random.choices(my_list,k = 2))
```
