def myFun(num):
    num[0] = 20


list = [1, 2, 3, 4, 5]
myFun(list)
print(list)  # list will be changed after the function call


def myFun(num):
    num[0] = 20


list = [1, 2, 3, 4, 5]
list2 = [3, 4, 6, 7]
myFun(list)
myFun(list2)
print(list)  # list will be changed after the function call
print(list2)


def my_function(*team):
    print("The youngest member is " + team[0])


my_function("sam", "tom", "ben")


def my_function(x):
    return 5 * x


print(my_function(3))


def my_function(**players):
    print("His last player is " + players["lplayer"])


my_function(fplayer="Rayudu", lplayer="Deepak")


def marks(maths, english):
    print("Addition of two numbers:", maths + english)
    print("Subtraction of two numbers is :", maths - english)
    print("Division of two numbers :", maths * english)
    print("Multiplication of two numbers is :", maths / english)

marks(50, 90)

def covid(Name,Temp='98'):
    print(Name,Temp)

covid("Soundar",100)


