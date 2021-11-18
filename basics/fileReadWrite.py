import time
import os

myfile = open("fruits.txt")
#print(myfile.read())

if os.path.exists("fruits.txt"):
    with open("fruits.txt") as myfile:
        content = myfile.read()
        print(content)
else:
    print("file does not exist")
time.sleep(5)

with open("veg.txt", 'w') as newfile:
    newfile.write("Tomato\n")
    newfile.write("Potato\n")

with open("data.txt", "a+") as file:
    file.seek(0)
    content = file.read()
    #file.seek(0)
    file.write(content)
    file.write(content)

