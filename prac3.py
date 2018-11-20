name=input("Enter name: ")

while len(name)<=0:
    print("Name is blank, enter again")
    name=input("Enter name: ")

print(name[::2])

for i in range(o,len(name),2):
    print(name[i],end='')
