# OPS

## EXAMPLES

### 74. Python Program to Get the Class Name of an Instance

```py title ="Example 1: Using __class__.__name__"
class Vehicle:
    def name(self, name):
        return name

v = Vehicle()
print(v.__class__.__name__)
```
