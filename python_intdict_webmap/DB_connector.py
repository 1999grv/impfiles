import mysql.connector
import pandas
con = mysql.connector.connect(
user="root",
#password="ardit700_student",
host="127.0.0.1",
database="grv"
)

cursor=con.cursor()
query=cursor.execute("select * from emp")
result=cursor.fetchall()
df12=pandas.DataFrame(result)
print("RUNNING DATABASE....")
print(df12)
print("DB CONNECTION SUCESSFULL!....")