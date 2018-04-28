'''
Created on 28-Apr-2018

@author: Vijay
'''
import mysql.connector;
connection=mysql.connector.connect(host='localhost',database='a7',user='root',password='Vijay@123')
cur=connection.cursor()
cur.execute("select itemcode,avg(qtyavailable) from retailstock group by itemcode having Avg(qtyavailable) < 75;")
cur.arraysize=3
data = cur.fetchmany();
for a in data:
    print(a)
#connection.commit()
connection.close()