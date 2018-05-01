'''
Created on 30-Apr-2018

@author: Vijay
'''
import mysql.connector;
connection=mysql.connector.connect(host='localhost',database='a7',user='root',password='Vijay@123')
cur=connection.cursor()
cur.executemany("""UPDATE item SET 
                price = price*%s where itemtype=%s;""",
                [('1.03','FMCG'),
                 ('1.05','Apparels'),
                 ('1.11','Computer')])
connection.commit()
connection.close()