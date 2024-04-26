# pip install mysql-connection-pyton #

import mysql.connector

dados_connect = mysql.connector.connect(
    host = "localhost", 
    user = "root", 
    password = "", 
    database = "employees", 
    port = 3307)

cursor = dados_connect.cursor()
cursor.execute('SELECT * FROM salaries')

consulta = cursor.fetchall()
print(consulta)


