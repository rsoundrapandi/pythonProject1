import mysql.connector

mydb = mysql.connector.connect(host="localhost", user="root", password="12345", database="Hospital")
dbse = mydb.cursor()
# SQL1 = "insert into Inpatient(Doctor_ID,Doctor_Name,Patient_Name) VALUES (%s,%s,%s)"
# val = [('1001', 'Pandian','Ram'),('1001', 'Pandian','Ram2'),('1001', 'Pandian','Ram3')]
# dbse.executemany(SQL1, val)
# mydb.commit()
# print(dbse.rowcount)

sql2="select Doctor_ID,Count(*) from Inpatient WHERE Patient_Name IS NULL GROUP BY Doctor_ID  HAVING count(*)>1"
dbse.execute(sql2)
myresult=dbse.fetchall()
for i in myresult:
    print(i)

