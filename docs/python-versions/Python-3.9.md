# Python 3.9

## Dictionary Unions

**Merge dictionaries**
We now have a merge operator for performing dictionary unions: |. It works the same as a.update(b) or {**a,**b}, with one difference: It works for any instance of the dict subclass

You can merge two dictionaries like so:

```py
user = {'name': 'John', 'surname': 'Doe'}
address = {'street': 'Awesome street 42', 'city': 'Huge city', 'post': '420000'}

user_with_address = user | address

print(user_with_address)
# {'name': 'John', 'surname': 'Doe', 'street': 'Awesome street 42', 'city': 'Huge city', 'post': '420000'}
```

Updating dictionaries

As for updating, you now have the operator |=. This works in place.

You can update the first dictionary with keys and values from the second like so:

```py
grades = {'John': 'A', 'Marry': 'B+'}
grades_second_try = {'Marry': 'A', 'Jane': 'C-', 'James': 'B'}

grades |= grades_second_try

print(grades)
# {'John': 'A', 'Marry': 'A', 'Jane': 'C-', 'James': 'B'}
```

## Generating Random Bytes

The random library can now be used to generate random bytes via randbytes.

For example, to generate ten random bytes:

```py
import random

print(random.Random().randbytes(10))
b'CO\x0e\x0e~\x12\x0c\xa4\xa0p'
```

## String Methods

Two methods were added to the str object:

1. removeprefix
2. removesuffix

### removeprefix

This first method removes the inputted string from the beginning of another string.

For example:

```py
file_name = 'DOCUMENT_001.pdf'

print(file_name.removeprefix('DOCUMENT_'))
#  001.pdf
```

If the string doesn't start with the input string, a copy of the original string will be returned:

```py
file_name = 'DOCUMENT_001.pdf'

print(file_name.removeprefix('DOC_'))
# DOCUMENT_001.pdf
### removesuffix
```

Similarly, we can remove the suffix from the selected string with the second method.

To remove the .pdf file extension from the file name:

```py
file_name = 'DOCUMENT_001.pdf'

print(file_name.removesuffix('.pdf'))
# DOCUMENT_001


file_name = 'DOCUMENT_001.pdf'

print(file_name.removesuffix('.csv'))
# DOCUMENT_001.pdf
## IANA Timezone Support
```

The zoneinfo module has been added to support the IANA time zone database.

For example, to create a time zone–aware timestamp, you can add the tz or tzinfo arguments to the datetime method:

```py
import datetime
from zoneinfo import ZoneInfo

datetime.datetime(2020, 10, 7, 1, tzinfo=ZoneInfo('America/Los_Angeles'))
# datetime.datetime(2020, 10, 7, 1, 0, tzinfo=zoneinfo.ZoneInfo(key='America/Los_Angeles'))
```

You can easily convert between time zones as well:

```py
import datetime
from zoneinfo import ZoneInfo

start = datetime.datetime(2020, 10, 7, 1, tzinfo=ZoneInfo('America/Los_Angeles'))
start.astimezone(ZoneInfo('Europe/London'))
datetime.datetime(2020, 10, 7, 9, 0, tzinfo=zoneinfo.ZoneInfo(key='Europe/London'))
```

## Generic Type Annotations

From now on you can use generic types for type annotations. Instead of having to use typing.List or typing.Dict, you can use the list or dict built-in collection types as generic types

```py
def sort_names(names: list[str]):
    return sorted(names)
```

## String Replace Fix

An issue with string replace for empty strings has been fixed.

In previous versions:

```py
"".replace("", "prefix", 1)
# ''
From now on:

"".replace("", "prefix", 1)
# 'prefix'
```
