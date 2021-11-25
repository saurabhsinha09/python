import configparser

parser = configparser.ConfigParser()
parser.add_section('mysql')

hostname = input("Host Name: ")
parser.set('mysql', 'host', hostname)

username = input("User Name: ")
parser.set('mysql', 'user', username)

password = input("Password: ")
parser.set('mysql', 'passwd', password)

dbname = input("Database: ")
parser.set('mysql', 'db', dbname)

fp=open('db.ini','w')
parser.write(fp)
fp.close()