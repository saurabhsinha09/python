import mysql.connector as msc

con = msc.connect(user = "test", password = "Test12345", host = "localhost", database = "db1")

def create_table():
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)")
    cur.execute("INSERT INTO store VALUES ('Bat' , 10, 500)")
    con.commit()
    #con.close()

def insert_table(item, quantity, price):
    cur = con.cursor()
    #cur.execute("INSERT INTO store VALUES ('%s', '%s', '%s')" % (item, quantity, price))
    cur.execute("INSERT INTO store VALUES (%s,%s,%s)", (item, quantity, price))
    con.commit()
    #con.close() 

def select_table():
    cur = con.cursor()
    cur.execute("SELECT * FROM store")
    rows = cur.fetchall()
    #con.close()
    return rows

def delete_table(item):
    cur = con.cursor()
    cur.execute("DELETE FROM store WHERE item = %s",(item,))
    con.commit()
    #con.close()     

def update_table(quantity, price, item):
    cur = con.cursor()
    cur.execute("UPDATE store SET quantity = %s, price = %s WHERE item = %s",(quantity, price, item))
    con.commit()
    #con.close() 

create_table()

insert_table("Wicket", 36, 360)    
insert_table("Ball", 100, 500.75)  
insert_table("Gloves", 50, 400)
print(select_table())

delete_table("Ball")
print(select_table())

update_table(15, 120, "Gloves")    
update_table(25, 250, "Wicket")
print(select_table())   

con.close()