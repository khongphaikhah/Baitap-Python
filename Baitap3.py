import pandas as pd
from mysql.connector import MySQLConnection, Error

import mysql.connector
myconn = mysql.connector.connect(host = "localhost", user = "root",
passwd = "", database = "py_db")
cur = myconn.cursor()

# def connect():
#     db_config = {
#         'host': 'localhost',
#         'database': 'py_db',
#         'user': 'root',
#         'password': ''
#     }
    
#     conn = None
 
#     try:
#         conn = MySQLConnection(**db_config)
 
#         if conn.is_connected():
#             return conn
 
#     except Error as error:
#         print(error)
 
#     return conn

# df = pd.read_excel('D:\\Python\\input.xlsx', sheet_name='MAU', usecols='A:H', skiprows=10, nrows=52)
# data = []
# for row in df.iterrows():
#     row_data = []
#     for value in row[1]:
#         row_data.append(value)
#     sql = "insert into students(id, code, first_name, last_name, birthOfDate, math, physics, chemistry) values (%s,%s,%s,%s,%s,%s,%s,%s)"
#     conn = connect()
#     val = (row_data[0],row_data[1],row_data[2],row_data[3],row_data[4],row_data[5],row_data[6],row_data[7])
#     cursor = conn.cursor()
#     cursor.execute(sql, val)
#     conn.commit()
#     data.append(row_data)

#THEM
sql = ("insert into students(id, code, first_name, last_name, birthOfDate, math, physics, chemistry) "
+ "values (%s, %s, %s, %s, %s, %s, %s, %s)")

#giá trị của một row được cung cấp dưới dạng tuple
val = (53, "c200454", "Hoang", "dep try", "18/5/2002",2.22,2.25,2.66)

try:
#inserting the values into the table
    cur.execute(sql,val)
#commit the transaction
    myconn.commit()
except:
    myconn.rollback()
    print(cur.rowcount,"record inserted!")
    myconn.close()


#SUA
try:
# cập nhật name cho bảng students
    cur.execute("update students set last_name = 'Đạt' where id = 53")
    myconn.commit()
except:
    myconn.rollback()
    myconn.close()


#XOA
try:
# # cập nhật name cho bảng students
    cur.execute("delete from students where id = 53")
    myconn.commit()
except:
    myconn.rollback()
    myconn.close()