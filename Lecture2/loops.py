#loops
for i in [0, 1, 2, 3, 4, 5]:
    print(i)

print("another way:")

for i in range(6):
    print(i)    

print("loop in lists:") 

names =["cs50", "web", "programming", "python", "html", "css"]
for i in range(len(names)):
    print(names[i])   

print("print list using for-each loop: ")

for name in names:
    print(name)

print("loop over every character of string: ")

chars = "CS50"
for  c in chars:
    print(c)   