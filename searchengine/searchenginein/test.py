import pymysql

db=pymysql.connect('localhost', 'root', 'python5717', 'pythondatabase')

cursor = db.cursor()
cursor.execute("select version()")
data = cursor.fetchone()

print(data)

cursor.close()
db.close()
