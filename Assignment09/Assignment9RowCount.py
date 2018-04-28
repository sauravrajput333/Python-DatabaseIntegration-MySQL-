'''
Created on 28-Apr-2018

@author: Vijay
'''
import mysql.connector;
connection=mysql.connector.connect(host='localhost',database='a7',user='root',password='Vijay@123')
cur=connection.cursor()
cur.execute("select * from supplier order by supplierid;")
data = cur.fetchall()
print(cur.rowcount)
for row in data:
    print(row)
print(cur.rowcount)
#connection.commit()
connection.close()