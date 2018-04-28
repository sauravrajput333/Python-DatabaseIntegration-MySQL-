'''
Created on 28-Apr-2018

@author: Vijay
'''
import mysql.connector;
connection=mysql.connector.connect(host='localhost',database='a7',user='root',password='Vijay@123')
cur=connection.cursor()
cur.execute("select s.supplierid,suppliername,itemcode,quotedprice,count(s.supplierid) from supplier s,quotation q where  s.supplierid=q.supplierid and quotationstatus = 'Accepted' group by s.supplierid;")
data = cur.fetchall();
for row in data:
    print(row)
connection.commit()
connection.close()