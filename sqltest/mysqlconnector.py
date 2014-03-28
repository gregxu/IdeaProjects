__author__ = 'gregxu'

import mysql.connector

#cnx = mysql.connector.connect(user='mysqluser', host='localhost', database='test')

cnx = mysql.connector.connect(user='gregxu', host='localhost', database='test')

#mysqluser:@localhost:3306:

cursor = cnx.cursor()

add_client_firms = ("insert into client_firms (id, name) values (4, 'client4')")

cursor.execute(add_client_firms)

cnx.commit()
cursor.close()

cnx.close()