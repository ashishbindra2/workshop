# import struct

# # pack integers into bytes (C-style struct)
# data = struct.pack('i f', 10, 3.14)
# print(data)

# # unpack back to Python values
# unpacked = struct.unpack('i f', data)
# print(unpacked)

from dataclasses import dataclass

@dataclass
class Person:
    name: str
    age: int
p1 = Person("Alice", 30)
p2 = Person("Alice", 30)
p3 = Person("Bob", 25)

print(p1 == p2)  # True
print(p1 == p3)  # False