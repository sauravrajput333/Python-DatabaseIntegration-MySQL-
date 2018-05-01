'''
Created on 30-Apr-2018

@author: Vijay
'''
import mysql.connector;
connection=mysql.connector.connect(host='localhost',database='a7',user='root',password='Vijay@123')
cur=connection.cursor()
sql = """UPDATE supplier SET
        supplieremailid = 'john@ebats.com'
        where supplierid='S1009'"""
sql1 = """UPDATE supplier SET 
        suppliercontactno = '879-456-398'
        where supplierid='S1009'"""
cur.execute(sql)
cur.execute(sql1)
connection.commit()
connection.close()