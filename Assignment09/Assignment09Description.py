'''
Created on 28-Apr-2018

@author: Vijay
'''
import mysql.connector;
connection=mysql.connector.connect(host='localhost',database='a7',user='root',password='Vijay@123')
cur=connection.cursor()
cur.execute("select * from supplier order by supplierid;")
print(cur.description)
cur.execute("delete from supplier where supplierid='S1008';")
print(cur.description)
#connection.commit()
connection.close()