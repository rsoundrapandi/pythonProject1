# dictionary = {<key>: <value>, <key>: <value>,}

SouthStates={"Tamilnadu":"Chennai","Karnataka":"Bangalore","Kerala":"Thiruvananthapuram"}
NorthStates={"Maharastra":"Mumbai","Haryana":"Chandigarh","Odisha":"Bhubaneswar"}
SouthStates['Goa']='Panaji'
SouthStates['Tamilnadu']='CHENNAI'
Sets1={"Tamilnadu","Chennai","Karnataka","Bangalore","Kerala","Thiruvananthapuram"}
Sets2={"Maharastra","Mumbai","Haryana","Bangalore","Chandigarh","Odisha","Bhubaneswar","Tamilnadu","Chennai"}
#Program1
#Method1
India={**SouthStates,**NorthStates}
print(India)
#Method2
India=SouthStates.copy()
India.update(NorthStates)
print(India)

#Program2
del SouthStates['Goa']
print(SouthStates)

#Program3
keys = ['red', 'green', 'blue']
values = ['#FF0000','#008000', '#0000FF']

Colors=dict(zip(keys,values))
print(Colors)

#program4
print(len(Sets1))

#Program5
print(Sets1.difference(Sets2))
print(Sets1-Sets2)


