import sqlite3

def create_table():
    conn = sqlite3.connect("lite.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)")
    cur.execute("INSERT INTO store VALUES ('Bat' , 10, 500)")
    conn.commit()
    conn.close()

def insert_table(item, quantity, price):
    conn = sqlite3.connect("lite.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO store VALUES (?, ?, ?)",(item, quantity, price))
    conn.commit()
    conn.close()  

def select_table():
    conn = sqlite3.connect("lite.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM store")
    rows = cur.fetchall()
    conn.close()
    return rows

def delete_table(item):
    conn = sqlite3.connect("lite.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM store WHERE item = ?",(item,))
    conn.commit()
    conn.close() 

def update_table(quantity, price, item):
    conn = sqlite3.connect("lite.db")
    cur = conn.cursor()
    cur.execute("UPDATE store SET quantity = ?, price = ? WHERE item = ?",(quantity, price, item))
    conn.commit()
    conn.close()     

create_table()

insert_table("Wicket", 36, 360)    
insert_table("Ball", 100, 500.75)  
insert_table("Gloves", 50, 399)
print(select_table())

delete_table("Ball")
print(select_table())

update_table(24, 250, "Wicket")
print(select_table())