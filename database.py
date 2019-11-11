import mysql.connector


mydb = mysql.connector.connect(user='root', password='toor', host='127.0.0.1', database='dos')
print(mydb)
table = "main"
mycursor = mydb.cursor()

sql = "INSERT INTO " + table + " (name, address) VALUES (%s, %s)"
val = ("John", "Highway 21")
mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")

mydb.close()
