'''
Created on 30-Apr-2018

@author: Vijay
'''
import mysql.connector;
connection=mysql.connector.connect(host='localhost',database='a7',user='root',password='Vijay@123')
cur=connection.cursor()
sql = """SELECT description,price 
        FROM item WHERE description LIKE '%Hard disk'"""
cur.execute(sql)
for row in cur.fetchall():
    print(row)
connection.commit()
connection.close()