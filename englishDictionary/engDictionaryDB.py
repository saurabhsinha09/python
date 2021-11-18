#Referring online database from Udemy Course 
#"Python Mega Course 2022: Build 10 Real-World Programs"
#Thanks to instructor Ardit Sulce
#pip install mysql-connector-python
import mysql.connector
import difflib as dl

con = mysql.connector.connect(
user = "ardit700_student",
password = "ardit700_student",
host = "108.167.140.122",
database = "ardit700_pm1database"
)

cursor = con.cursor()
query = cursor.execute("SELECT Expression,Definition FROM Dictionary")
word_index = dict(cursor.fetchall())

def translate(word):
    if word in word_index:
        query = cursor.execute("SELECT Definition FROM Dictionary WHERE Expression = '%s'" % word)
        results = cursor.fetchall()
        return results
    elif word.upper() in word_index:
        query = cursor.execute("SELECT Definition FROM Dictionary WHERE Expression = '%s'" % word.upper())
        results = cursor.fetchall()
        return results
    else:
        close_match = dl.get_close_matches(word.lower(), word_index.keys(), n=2, cutoff=0.8)
        if (len(close_match)) > 0:
            #close_match = dl.get_close_matches(word.lower(), data.keys(), n=2, cutoff=0.8)[0]
            print(f"Are you looking for word {close_match[0]}. Type Y to continue or N for new word.")
            confirm = input("Type: ")
            if confirm == "Y":
                query = cursor.execute("SELECT Definition FROM Dictionary WHERE Expression = '%s'" % close_match[0])
                results = cursor.fetchall()
                return results
            else:
                return "Please enter correct word."	
        else:
            return "Word does not exist. Please check."    

while True:
    word = input("Enter Word: ")
    if word != "q":
        output = translate(word.lower())
        index = 1
        if isinstance(output, list):
            for item in output:
                print(index, item[0])
                index +=1
        else:
            print(output)
    else:
        break