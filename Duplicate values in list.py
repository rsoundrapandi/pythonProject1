# a=[]
# n=int(input("Enter the no list:"))
# for x in range (0,n):
#     element=int(input("Enter the element"+str(x+1)+":"))
#     a.append(element)
#     print(a)
# b=set()
# unique=[]
#
# for x in a:
#
#     if x not in b:
#         unique.append(x)
#         b.add(x)
# print(unique)

def duplicate(x):
    a=[]
    _size=len(x)

    for i in range(0,_size):

        for j in range(i+1,_size):

            if x[i] == x[j] and x[i] not in a:

                a.append(x[i])
    return a




list1 = [10, 20, 30, 20, 20, 30, 40, 50, -20, 60, 60, -20, -20]
print(duplicate(list1))




