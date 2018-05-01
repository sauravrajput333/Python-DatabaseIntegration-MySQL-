'''
Created on 30-Apr-2018

@author: Vijay
'''
import mysql.connector;
connection=mysql.connector.connect(host='localhost',database='a7',user='root',password='Vijay@123')
cur=connection.cursor()
sql = """UPDATE supplier SET 
        suppliercontactno = '303-537-9127'
        where supplierid='S1009'"""
cur.execute(sql)
connection.commit()
connection.close()