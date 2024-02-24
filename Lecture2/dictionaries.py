# dict = { key1 : value1, key2 : value2, key3 : value3, ...}
names = {1 : "Divyansh", 2 : "Geet", 3 : "CS50"}

print(names[1])

names[4] = "Web Programming" #adding new key-value pair
names[5] = "CS50 web"
names[1] = "Divyansh" #modofying key's value
del names[4] #delete key-value pair
names.pop(5) #delete using pop

#iterating over keys
for key in names:
    print(key)

#iterating over values:
for value in names.values():
    print(value)

#iterating over key-value pairs
for key,value in names.items():
    print(key , value);    
