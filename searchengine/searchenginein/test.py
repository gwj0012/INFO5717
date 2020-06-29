import pymysql

db=pymysql.connect('127.0.0.1', 'root', 'python5717', 'database')

cursor = db.cursor()
cursor.execute("select version()")
data = cursor.fetchone()

print(data)

cursor.close()
db.close()
