# Exception

## examples

### 56. Python Program to Catch Multiple Exceptions in One Line

```py title="Multiple exceptions as a parenthesized tuple" linenums="1"
string = input()

try:
    num = int(input())
    print(string+num)
except (TypeError, ValueError) as e:
    print(e)
```
