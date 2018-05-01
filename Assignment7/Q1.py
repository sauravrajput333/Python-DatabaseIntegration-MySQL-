'''
Created on 30-Apr-2018

@author: Vijay
'''
import mysql.connector;
connection=mysql.connector.connect(host='localhost',database='a7',user='root',password='Vijay@123')
cur=connection.cursor()
cur.executemany("""INSERT INTO supplier VALUES(%s,%s,%s,%s)""",
                [('S1006','Frank Stores','123-345-456','frankstores@gmail.com'),
                ('S1007','Anshika Stores','456-345-456','anshikastores@gmail.com')])
connection.commit()
connection.close()