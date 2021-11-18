#functions of datetime library
#Restrict to use social media and video content websites in office hours
import time
from datetime import datetime as dt

hosts    = "hosts"
redirect = "127.0.0.1"
website_list = ["www.facebook.com", "www.youtube.com"]

while True:
    if dt(dt.now().year, dt.now().month, dt.now().day, 9) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, 18):
        print("Working hours")
        with open(hosts, 'r+') as file:
            content = file.read()
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write(redirect + "  " + website + "\n")
    else:
        print("Fun Hour....")
        with open(hosts, 'r+') as file:
            content = file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line)
            file.truncate()

    time.sleep(60)