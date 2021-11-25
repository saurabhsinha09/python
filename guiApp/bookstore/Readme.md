# App for book store

This app is for maintain list of all books read. 
We can add, delete, search, update and view.

Steps to create desktop app.

## Frontend library

Tkinter library used to create GUI of app.

## SQLite DB

Uncomment line 15 and comment line 16 to use sqlite db in "bookshelfFrontend.py"

## Create Exe of app

1. pip install pyinstaller
2. use the command "pyinstaller --onefile --windowed bookshelfFrontend.py" 
3. It will create exe file in dist folder.
4. App can also be directly use by copy the dist folder in PC.

## Mysql DB

* Install local my sql commuity edition.
* Configure user, password and db name in "bookshelfMYsql.py file.
* Comment line 15 and uncomment line 16 to use sqlite db in "bookshelfFrontend.py"