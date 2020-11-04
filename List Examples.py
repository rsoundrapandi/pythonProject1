# def sum67(list):
#     answer=0
#     boo=True
#     for i in range(0,len(list)):
#         if(list[i]==6):
#             boo=False
#         if(boo):
#             answer+=list[i]
#             print(answer)
#         if (list[i] == 7):
#             boo = True
#     return answer
# #
# #
# print(sum67([1, 2, 2,6,9,7]))
#
#
# def make_chocolate(small, big, goal):
#
#   if(small+big*5<goal):
#
#     return -1
#
#   elif small<goal%5:
#
#     return -1
#
#   else:
#
#     if(goal<10):
#
#       return goal%5
#
#     return goal-(big*5)
#
# print(make_chocolate(4,1,9))


# def sum67(nums):
#     result = 0
#     inside = False
#     for i in range(len(nums)):
#         if (i != 6 and inside == False):
#             result +=nums[i]
#         else:
#             inside = True
#
#         if i == 7:
#             inside = False
#     return result
#
# print(sum67([1, 2, 2,6,7,8,9]))


def maths(l1):
    sumof=0
    x=True

    for i in range(len(l1)):

        if(l1[i]==6):
            x=False
        if(x):
            sumof +=l1[i]

        if(l1[i]==7):
            x=True
    print(sumof)
(maths([1,5,4,6,5,7,4]))