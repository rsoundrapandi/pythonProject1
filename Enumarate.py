
l1=['ram','soundar','sundar']
a=[]
for i,j in enumerate(l1,2):
    print("index is %d and value is %s"%(i,j))
    print(tuple((i,j)))
    x=a.append((i,j))
    print(a)