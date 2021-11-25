import mysql.connector as msc

#con = msc.connect(user = "test", password = "Test12345", host = "localhost", database = "books")

def connect_db():
    conn = msc.connect(user = "test", password = "Test12345", host = "localhost", database = "books")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER AUTO_INCREMENT PRIMARY KEY, title TEXT, author TEXT, year INTEGER, isbn INTEGER)")
    conn.commit()
    conn.close()

def insert(title,author,year,isbn):
    conn = msc.connect(user = "test", password = "Test12345", host = "localhost", database = "books")
    cur=conn.cursor()
    cur.execute("INSERT INTO book(title, author, year, isbn) VALUES (%s,%s,%s,%s)",(title,author,year,isbn))
    conn.commit()
    conn.close()
    view()

def view():
    conn = msc.connect(user = "test", password = "Test12345", host = "localhost", database = "books")
    cur=conn.cursor()
    cur.execute("SELECT * FROM book")
    rows=cur.fetchall()
    conn.close()
    return rows

def search(title="",author="",year="",isbn=""):
    conn = msc.connect(user = "test", password = "Test12345", host = "localhost", database = "books")
    cur=conn.cursor()
    cur.execute("SELECT * FROM book WHERE title=%s OR author=%s OR year=%s OR isbn=%s", (title,author,year,isbn))
    rows=cur.fetchall()
    conn.close()
    return rows

def delete(id):
    conn = msc.connect(user = "test", password = "Test12345", host = "localhost", database = "books")
    cur=conn.cursor()
    cur.execute("DELETE FROM book WHERE id=%s",(id,))
    conn.commit()
    conn.close()

def update(id,title,author,year,isbn):
    conn = msc.connect(user = "test", password = "Test12345", host = "localhost", database = "books")
    cur=conn.cursor()
    cur.execute("UPDATE book SET title=%s, author=%s, year=%s, isbn=%s WHERE id=%s",(title,author,year,isbn,id))
    conn.commit()
    conn.close()

connect_db()
#insert("The Sun","John Smith",1918,913123132)
#insert("The moon","John Smooth",1917,99999)
#print(view())
#print(search(author="John Smooth"))
#update(2,"The moon","John Smooth",1917,99998)
#print(view())
#delete(1)
#print(view())

