'''
Created on 28-Apr-2018

@author: Vijay
'''
import mysql.connector;
connection=mysql.connector.connect(host='localhost',database='a7',user='root',password='Vijay@123')
cur=connection.cursor()
cur.execute("select * from supplier order by supplierid;")
data = cur.fetchmany()
print(cur.arraysize)
cur.arraysize=5
for row in data:
    print(row)
print(cur.arraysize)
#connection.commit()
connection.close()