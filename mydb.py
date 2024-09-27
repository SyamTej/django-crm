#install the mysql on your computer
#pip install django

import mysql.connector

dateBase = mysql.connector.connect(
	host = 'localhost',
	user = 'root',
	passwd = 'Qwerty@123',

	)


#prepare ac cursor object

cursorObject = dateBase.cursor()

cursorObject.execute("CREATE DATABASE rareco")

print("All done!")