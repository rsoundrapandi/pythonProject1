# We double all numbers using map()
numbers = (1, 2, 3, 4)
result = map(lambda a: a + a, numbers)
print(list(result))

# List of strings
l = ['sat', 'bat', 'cat', 'mat']

# map() can listify the list of strings individually
test = list(map(list, l))
print(test)


def fun(variable):
    letters = ['a', 'e', 'i', 'o', 'u']
    if (variable in letters):
        return True

    else:
        return False


# sequence
sequence = ['g', 'e', 'e', 'j', 'k', 's', 'p', 'r']

# using filter function
filtered = filter(fun, sequence)

print('The filtered letters are:')
for s in filtered:
    print(s)

a = ("John", "Charles", "Mike")
b = ("Jenny", "Christy", "Monica")
print(list(zip(a, b)))

import functools

lis = [3, 1, 5, 6, 2, ]

print("The sum of the list elements is : ", end="")
print(functools.reduce(lambda a, b: a + b, lis))

print("The maximum element of the list is :< ", end="")
print(functools.reduce(lambda a, b: a if a < b else b, lis))

l1 = ['test', 'test1', 'test2', 'test3', 'test4', 'test5', 'test6', 'test7']
l2 = [0, 1, 2, 3, 4, 5, 6, 7]
l3 = [5, 8, 7, 3, 6, 1, 2]

print(tuple(zip(l1, l2)))
print(list(zip(l1, l2)))
print(sorted(l2, reverse=True))


def merge(list1, list2):
    merged_list = [(list1[i], list2[i]) for i in range(0, len(list1))]
    return merged_list


# Driver code
list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
print(merge(list1, list2))

Number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def numbers(num):
    if (num % 2 != 0):
        return True
    else:
        return False


function = filter(numbers, Number)

print(list(function))