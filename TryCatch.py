#
# try:
#     No=int(input("Enter value"))
#     print(No)
# except NameError as N:
#     print("Invalid",N)
# except Exception as E:
#     print("Test",E)
# finally:
#     print("Bye")


# try:
#     No=int(input("Enter value"))
#     print(No)
# except NameError as N:
#     print("Invalid",N)
# except Exception as E:
#     print("Test",E)
# finally:
#     print("Bye")
#
#
# class School:
#     def __init__(self, students, teachers):
#         self.students = students
#         self.teachers = teachers
#
#     def student(self):
#         print(self.students)
#
#     def teacher(self):
#         print(self.teachers)
#
#
# class Classteacher(School):
#     pass
#
#
# Teacher = Classteacher("gokul", "Ram")
# Teacher.teacher()
# Teacher.student()

i=2
while i>=0:
    print("*")
    i -=2

for i in range (-1,1):
    print("*")

list=[0,1,2,3]
X=1
for element in list:
    X *=element
    print(X)