# Details to be modified as per the postgress installation #
# database = either create db1 or use own name             #
# user = create new user or use postgress                  #
# password = installation password                         #
# host = It can be local or any server                     #
import psycopg2 as pgs

def create_table():
    conn = pgs.connect(database="db1", user="test", password="Test1234", host="localhost", port="5432")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)")
    cur.execute("INSERT INTO store VALUES ('Bat' , 10, 500)")
    conn.commit()
    conn.close()

def insert_table(item, quantity, price):
    conn = pgs.connect(database="db1", user="test", password="Test1234", host="localhost", port="5432")
    cur = conn.cursor()
    #cur.execute("INSERT INTO store VALUES ('%s', '%s', '%s')" % (item, quantity, price))
    cur.execute("INSERT INTO store VALUES (%s,%s,%s)", (item, quantity, price))
    conn.commit()
    conn.close() 

def select_table():
    conn = pgs.connect(database="db1", user="test", password="Test1234", host="localhost", port="5432")
    cur = conn.cursor()
    cur.execute("SELECT * FROM store")
    rows = cur.fetchall()
    conn.close()
    return rows

def delete_table(item):
    conn = pgs.connect(database="db1", user="test", password="Test1234", host="localhost", port="5432")
    cur = conn.cursor()
    cur.execute("DELETE FROM store WHERE item = %s",(item,))
    conn.commit()
    conn.close()     

def update_table(quantity, price, item):
    conn = pgs.connect(database="db1", user="test", password="Test1234", host="localhost", port="5432")
    cur = conn.cursor()
    cur.execute("UPDATE store SET quantity = %s, price = %s WHERE item = %s",(quantity, price, item))
    conn.commit()
    conn.close() 

#create_table()

insert_table("Wicket", 36, 360)    
insert_table("Ball", 100, 500.75)  
insert_table("Gloves", 50, 400)
print(select_table())

delete_table("Ball")
print(select_table())

update_table(15, 120, "Gloves")    
update_table(25, 250, "Wicket")
print(select_table())    