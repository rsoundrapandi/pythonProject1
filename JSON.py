# import json
#
# a Python object (dict):
# x = {
#   "name": "John",
#   "age": 30,
#   "city": "New York"
# }
#
#  convert into JSON:
# y = json.dumps(x)
#
#  the result is a JSON string:
# print(y)
#
# x ='{ "name":"Sachin", "age":18, "city":"Mumbai"}'
#
#  parse x:
# y = json.loads(x)
#
#  the result is a Python dictionary:
# print(y)
#
# import json
# import mysql.connector
# from base64 import urlsafe_b64encode
#

#
# x = {
#     "name": "John",
#     "age": 30,
#     "married": True,
#     "divorced": False,
#     "children": ("Ann", "Billy"),
#     "pets": None,
#     "cars": [
#         {"model": "BMW 230", "mpg": 27.5},
#         {"model": "Ford Edge", "mpg": 24.1}
#     ]
# }
# json_data = json.dumps(x)
# print(json_data)
# # json_data = urlsafe_b64encode(json_data)
# SQL1 = "INSERT INTO json(JSON) VALUES ('" + json_data + "')"
# dbse.execute(SQL1)
# mydb.commit()


import json
from urllib.request import urlopen
import mysql.connector

# with urlopen("http://dummy.restapiexample.com/api/v1/employees") as response:
#     source=response.read()
# data=json.loads(source)
#
# with open('Json_file','w') as f:
#     json.dump(data,f,indent=4)
with open('Json_file','r') as f1:
    data=json.load(f1)
# print(len(data['data']))
test_value = dict()
for x in data['data']:
    value = x['id']
    salary = x['employee_salary']
    test_value[value] = salary
    y = json.dumps(x)
    print(y)
    mydb = mysql.connector.connect(host="localhost", user="root", password="12345", database="company")
    dbse = mydb.cursor()
    SQL1 = "INSERT INTO json(JSON) VALUES ('" + y + "')"
    dbse.execute(SQL1)
    mydb.commit()
mydb.close()
# print(test_value)

