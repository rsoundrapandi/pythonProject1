
#
# def Leap(year):
#     if (year % 4) == 0:
#         if (year % 100) == 0:
#             if (year % 400) == 0:
#                 print("leap year")
#             else:
#                 print("Not a leap year")
#         else:
#             print("Not a leap year")
#     else:
#         print("Not a leap year")
#
# Leap(2000)

#
# def find():
#     fruits = ["apple", "orange", "cherry"]
#     for i in fruits:
#         if i =='orange':
#             print(i)
#
#         else:
#             print("Test")
#
#     return i
#
# find()

# for i in range(0,100):
#     if i > 1:
#     # check for factors
#         for n in range(2, i):
#             if i % n == 0:
#                 print(i, "is not a prime number")
#                 print(i, "times", i // i, "is", i)
#                 break
#         else:
#             print(i, "is a prime number")
#
# # if input number is less than
# # or equal to 1, it is not prime
#     else:
#         print(i, "is not a prime number")


# Python program to display all the prime numbers within an interval

# lower = 1
# upper = 100
#
# print("Prime numbers between", lower, "and", upper, "are:")
#
# for num in range(lower, upper + 1):
#    # all prime numbers are greater than 1
#    if num > 1:
#        for i in range(2, num):
#            if (num % i) == 0:
#                break
#        else:
#            print(num)

x= input("Enter your value: " )
if(x%2==0):
    print("even")
else:
    print("odd")