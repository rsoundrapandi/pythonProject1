import pandas as pd
from sqlalchemy import create_engine
import mysql.connector

df=pd.read_excel('C:\\Users\\Soundar\\Desktop\\Student Information.xlsx')
engine= create_engine('mysql+pymysql://root:12345@localhost/hospital')
df.to_sql('employee1',con=engine, if_exists='append',index=False)


# mydb = mysql.connector.connect(host="localhost", user="root", password="12345", database="Hospital")
# dbse = mydb.cursor()
# sql= 'select MIN(Salary) as MinSalary ,MAX(Salary) as MaxSalary from hospital.employee'
# sql2= 'select count(EmployeeID) from hospital.employee'
# sql3= 'select substring(EmployeeName,1,3) from hospital.employee'
# dbse.execute(sql3)
# results=dbse.fetchall()
# for i in results:
#     print(i)