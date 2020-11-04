import re

# def is_allowed_specific_char(string):
#     charRe = re.compile(r'[^a-zA-Z0-9.]')
#     string = charRe.search(string)
#     return not bool(string)
#
# print(is_allowed_specific_char("ABCDEFabcdef123450"))
# print(is_allowed_specific_char("*&%@#!}{"))


# def is_allowe(string):
#     charRe = re.findall('\w',string)
#     print(charRe)
#
# is_allowe('2342342342')


# def is_allowed(string):
#     charRe = re.finditer(r"([0-9]{1,3})",string)
#     print(charRe)
#     for n in charRe:
#         print(n.group(0))
#
# is_allowed('Exercises number 1, 12, 13, and 345 are important')


# def is_allowed(string):
#     pattern='ab$'
#     test=re.search(pattern, string)
#     if
#         print(test)
#     else:
#         print("Testab,Ramesh")
# is_allowed('RAMESH')


# str = 'foo635bar4125mango2apple21orange'
# #split with regular expression
# chunks = re.m('\dS\w+',str)
# print(chunks)




# def is_allowed1(string):
#     pattern=re.compile('\w*ab')
#     test=re.findall(pattern, string)
#     test.group(0)
#
# is_allowed1('Sureshab,Ramueb,asdasdab')


str = 'purple alice-b@google.com monkey dishwasher'
match = re.search(r'([\w.-]+)@([\w.-]+)', str)
if match:
    print(match.group(0))  ## 'alice-b@google.com' (the whole match)
    print(match.group(1))  ## 'alice-b' (the username, group 1)
    print(match.group(2))  ## 'google.com' (the host, group 2)