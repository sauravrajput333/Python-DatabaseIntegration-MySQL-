'''
Created on 22-Apr-2018

@author: Vijay
'''
import mysql.connector;
connection=mysql.connector.connect(host='localhost',database='a7',user='root',password='Vijay@123')
cur=connection.cursor()
cur.execute("select suppliername,suppliercontactno from supplier where supplierid='S1002';")
data = cur.fetchall();
for row in data:
    print(row)
connection.commit()
connection.close()