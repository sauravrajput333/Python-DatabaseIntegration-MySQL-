'''
Created on 30-Apr-2018

@author: Vijay
'''
import mysql.connector;
connection=mysql.connector.connect(host='localhost',database='a7',user='root',password='Vijay@123')
cur=connection.cursor()
itemcode = input("Enter ItemCode > ")
itemtype  = input("Enter ItemType > ")
description = input("Enter Description > ")
price =  input("Enter Price > ")
reorderlevel  = input("Enter ReOrderlevel > ")
quantityonhand=input("Enter QuantityOnHand > ")
category = input("Enter Category > ")
cur.execute('INSERT INTO item VALUES(%s,%s,%s,%s,%s,%s,%s)',
            (itemcode,itemtype,description,price,reorderlevel,quantityonhand,category))
connection.commit()
connection.close()