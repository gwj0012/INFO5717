import pymysql

db=pymysql.connect("localhost", "root", "info5717", "pydb")

cursor=db.cursor()
cursor.execute("select version()")
data = cursor.fetchone()

print("Database version:%s" % data)

