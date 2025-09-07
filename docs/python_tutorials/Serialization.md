# SERIALIZATION

`Employee.py`

Employee Class will look like this

```py
class Employee:
 def __init__(self,eno,ename,esal,eaddr):
  self.eno = eno
  self.ename = ename
  self.esal = esal
  self.eaddr = eaddr
 
 def display(self):
  print(f'eno:{self.eno} ename: {self.ename} esal: {self.esal} eaddr: {self.eaddr}')
 
```

## Deserialization

- loads() --> Converting JSON string to python dict
- load() --> Reading json from a file and conveting that json into python dict

## serialization

- dump() --> from python dict to json and write json to file
- dumps() --> from pyhton dict to json string

```py
import json

employee = {
    'name':'ashish',
    'age':25,
    'salary':25000.00,
    'isMarried':False,
    'girlFriend':True,
    'ex':None
}

# serialization from python dict obj to json_string
json_string = json.dumps(employee,indent=4,sort_keys=True)
print(json_string)

# serialization from python dict object to json file
with open('emp.json','w') as f:
 json.dump(employee,f,indent=4)

# deserialization json_string to python dict
py_dict = json.loads(json_string)
print(py_dict)

with open('emp.json','r') as f:
 emp_dict = json.load(f)
print(emp_dict)
```

## custom object serialization

```py
import json

class Employee:
 def __init__(self,eno,ename,esal,eaddr):
  self.eno = eno
  self.ename = ename
  self.esal = esal
  self.eaddr = eaddr
 
 def display(self):
  print(f'eno:{self.eno} ename: {self.ename} esal: {self.esal} eaddr: {self.eaddr}')
 
e = Employee(100,"Ashish",90000,"patiala")
emp_dict = e.__dict__
print(emp_dict)

# serialization
with open('emp.json','w') as f:
 json.dump(emp_dict,f,indent=4)

# deserialization
with open('emp.json','r') as f:
 d= json.load(f)
print(type(d))

newemp = Employee(d['eno'],d['ename'],d['esal'],d['eaddr'])

newemp.display()
```

## YAML Sweialization

```py
# YAML Ain't Markup Language 
# Yet Another Markup Language
# more readable and ligt weight then json

from pyaml import yaml

emp_dict  = {
    'Person 1': {'age': 20, 'city': 'New York', 'hobbies': ['reading', 'hiking', 'coding']},
    'Person 2': {'age': 21, 'city': 'New York', 'hobbies': ['reading', 'hiking', 'coding']},
    'Person 3': {'age': 22, 'city': 'New York', 'hobbies': ['reading', 'hiking', 'coding']}
}





# serialization from dict object to yaml string
yaml_string = yaml.dump(emp_dict)
print(yaml_string)

# dump() to serialize from python dict object to yaml string/file
# serialization to yaml file
with open('emp.yaml','w') as f:
 yaml.dump(emp_dict,f)

# Deserilaization from yaml string to python dict
ed = yaml.safe_load(yaml_string)
for k,v in ed.items():
 print(f'{k} --> {v}')

# Deserialization from yaml file
with open('emp.yaml','r') as f:
 ed2 = yaml.safe_load(f)
 print(ed2)
print(type(ed2))
print(ed2)

```

## PICKL Serialization

```py
import json
import pickle
from Employee import Employee

e = Employee(100,"ashish",1000.00,"punjab")

# serialaization of employee object
with open('emp.ser','wb') as f:
  pickle.dump(e,f)
  print('Object Serilaization Complete')

# Deserializarion of employee object
with open('emp.ser','rb') as f:
  emp = pickle.load(f)
  print('Oject Deserialization Complete')

print('printing Employee Information')
emp.display()
```

## JSON PICKLE

```py
# encode() -> To convert an object to json_string
# decode() -> To convert json_string to orignal object
# pip install jsonpickle
import json
import jsonpickle
class Employee:
 def __init__(self,eno,ename,esal,eaddr):
  self.eno = eno
  self.ename = ename
  self.esal = esal
  self.eaddr = eaddr
 
 def display(self):
  print(f'eno:{self.eno} ename: {self.ename} esal: {self.esal} eaddr: {self.eaddr}')
 
e = Employee(100,"ashish",100000.00,"patiala")

# serialization
json_string = jsonpickle.encode(e)
print(json_string)

# serialization with file
with open('empkl.json','w') as f:
 f.write(json_string)

# deserialization
newemp = jsonpickle.decode(json_string)
newemp.display()

# deserialization from file
with open('empkl.json','r') as f:
 json_string = f.readline()
newe = jsonpickle.decode(json_string)
newe.display()
```
