# Write a Python script to merge two Python dictionaries
import string

SouthStates = {"Tamilnaduuuuuuuuuuuuuu": "Chennai", "AAAAA": "Bangalore", "Kerala": "Thiruvananthapuram"}
NorthStates = {"Maharastra": "Mumbai", "Haryana": "Chandigarh", "Odisha": "Bhubaneswar"}
Num = [1, 8, 7, 34, 56, 78, 99]
#
# India = {**SouthStates, **NorthStates}
# print(India)
# Des = sorted(Num)
# print(Des)
# Set2 = set(Des)
# print(Set2)

Values = SouthStates.keys()
print(Values)
Sort2 = sorted(Values)
print(Sort2)

Sort=[6,7,16,10,11,8]

for i in range(0, len(Sort)):

    for j in range(i + 1, len(Sort)):

        if (Sort[i] > Sort[j]):
            print(Sort[i],Sort[j])
            Sort[i], Sort[j] = Sort[j], Sort[i]

print(Sort)


string = input("Please enter your own String : ")
char = input("Please enter your own Character : ")

flag = 0
for i in range(len(string)):
    print(len(string))
    if(string[i] == char):
        flag = 1
        break


if(flag == 0):
    print("Sorry! We haven't found the Search Character in this string ")
else:
    print("The first Occurrence of ", char, " is Found at Position " , i + 1)


print(string.title())

def Repeat(x):
    _size = len(x)
    repeated = []
    for i in range(_size):
        k = i + 1
        for j in range(k, _size):
            if x[i] == x[j] and x[i] not in repeated:
                repeated.append(x[i])
    return repeated


list1 = [10, 20, 30, 20, 20, 30, 40, 50, -20, 60, 60, -20, -20]
print(Repeat(list1))

l2 = list(set(list1))
print(l2)


def duplicate():
    l1 = [10, 20, 30, 20, 20, 30, 40, 50, -20, 60, 60, -20, -20]
    l2 = []
    for i in l1:
        if i not in l2:
            l2.append(i)
    print(l2)


duplicate()

x,y,z=map(int,input("Enter the value ").split())
print(x,y,z)

a=int(input("Enter the value:"))

b=(x+y+z)/a

print(b)
