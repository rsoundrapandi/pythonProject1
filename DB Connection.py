import mysql.connector

mydb = mysql.connector.connect(host="localhost",user="root",password="12345",database="Company")
dbse = mydb.cursor()
# dbse.execute("CREATE TABLE Employee (Employee_name VARCHAR(255), Employee_dep VARCHAR(255),Employee_Number VARCHAR(255))")

sql1="insert into Employee1(LastName,FirstName,Age) VALUES('Teste789','3456898',27)"
dbse.execute(sql1)
mydb.commit()
sql2="select * from employee1"
dbse.execute(sql2)
for i in dbse:
  print(i)




