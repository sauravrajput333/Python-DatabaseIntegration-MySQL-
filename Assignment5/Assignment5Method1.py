'''
Created on 27-Apr-2018

@author: Vijay
'''
import mysql.connector;
connection=mysql.connector.connect(host='localhost',database='a7',user='root',password='Vijay@123')
cur=connection.cursor()
supplierid=input("Enter the Supplier ID")
supplerName=input("Enter the Supplier Name")
suppliercontactno=input("Enter the Supplier Nontact No.")
supplieremailid=input("Enter the Supplier Email ID")
cur.execute('INSERT INTO supplier VALUES (%s,%s,%s,%s)',(supplierid,supplerName,suppliercontactno,supplieremailid))
connection.commit()
connection.close()