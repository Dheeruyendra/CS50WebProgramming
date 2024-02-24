print in python:

```
printf("Hello World\n");
```
variables:
```
a = 28
b = 1.5
c = "Hello"
d = True
e = None # None is a special type in python
```

input:
```
name = input("Enter your name: ") # input always returns a string
print("Hello, " + name)
```

String concatenation:
```
name = "John"
print("Hello, " + name)

# or using format
print(f"Hello, {name}")
```

Type casting:
```
s = input("Enter an integer: ")
i = int(s)
```

Conditionals:
```
x = 28
if x > 0:
    print("x is positive")
elif x < 0:
    print("x is negative")
else:
    print("x is zero")
```

Lists:
```
names = ["Alice", "Bob", "Charlie"]
names.append("David") # adds to the end
names.pop() # removes the last element
names.sort()
names.remove("Alice")
names.reverse()
```

Sets:
```
s = set()
s.add(1)
s.add(2)
s.add(3)

s.remove(2)
len = len(s)
```

Tuples:
```
coordinates = (10.0, 20.0)
print(coordinates[0])
```

Loops:
```
for i in range(5):
    print(i)

names = ["Alice", "Bob", "Charlie"]
for name in names:
    print(name)
```

Dictionaries:
```
ages = {"Alice": 22, "Bob": 27}
ages["Charlie"] = 30 # adds a new key-value pair
ages["Alice"] = 23 # changes the value

print(ages["Alice"]) #get the value of a key

# iterate over keys
for key in ages:
    print(key)

# iterate over values
for value in ages.values():
    print(value)

# iterate over both
for key, value in ages.items():
    print(key, value)
```

Functions:
```
def square(x):
    return x * x

for i in range(10):
    print(f"The square of {i} is {square(i)}")
```

Modules:
```
from <fileName> import <functionName>
```

Classes:
 ```
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y    

p = Point(3, 5)
print(p.x)
print(p.y)
```

Decorators:
```python
def announce(f):
    def wrapper():
        print("About to run the function...")
        f()
        print("Done running the function.")
    return wrapper

@announce
def hello():
    print("Hello, world!")

hello()
```

lambda functions:
```python

