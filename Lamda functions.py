from functools import reduce

x = lambda m,N: m + N
print(x(5,10))


def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)

print(mydoubler(11))

# # tuple(filter(lambda x:(x%3 == 0),lst))
#
# list(map(lambda x:x**2,[lst]))

nums = [19, 65, 57, 39, 152, 639, 121, 44, 90, 190]
n=2
print("Orginal list:")
print(nums)
result = tuple(map(lambda x: (x*n), nums))
print("\nNumbers of the above list divisible by nineteen or thirteen:")
print(result)
print(' '.join(map(str,result)))


def fibonacci(count):
   listA = [0, 1]

   any(map(lambda _:listA.append(sum(listA[-2:])),
         range(2, count)))

   return listA[:count]

print(fibonacci(8))