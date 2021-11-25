import mysql.connector as msc

con = msc.connect(
user = "test",
password = "Test12345",
host = "localhost",
database = "world"
)

cursor = con.cursor()

query = cursor.execute("SELECT * FROM city;")
results = cursor.fetchall()

print(results[0:20])