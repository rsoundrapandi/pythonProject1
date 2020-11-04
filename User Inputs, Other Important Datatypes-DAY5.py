#Excersie1
A=[9,8,7,6,5,4,3]

A.insert(5,0)
print(A)

A.pop()
A.pop(0)
A.remove(5)
print(A)
Max_Var=max(A)
Min_Var=min(A)
A.sort()
Asc=sorted(A)
print(Max_Var,Min_Var,Asc)

#Excersie2

Subjects= ("English","Maths","Tamil","Social",1,2.34)

X=reversed(Subjects)
print(tuple(X))

Test=list(Subjects)
print(Test)

