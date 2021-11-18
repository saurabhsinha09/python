import json
import difflib as dl

#load the json data
data = json.load(open("data.json"))

#function to find out meaning of word
#if you type incorrect spelling of word
#it will give close match option of word with confirmation.
#Y - it will proceed; N - will ask for correct word
def translate(word):
    if word in data:
        return data[word]
    elif word.upper() in data:
        return data[word.upper()]
    else:
        close_match = dl.get_close_matches(word.lower(), data.keys(), n=2, cutoff=0.8)
        if (len(close_match)) > 0:
            #close_match = dl.get_close_matches(word.lower(), data.keys(), n=2, cutoff=0.8)[0]
            print(f"Are you looking for word {close_match[0]}. Type Y to continue or N for new word.")
            confirm = input("Confirmation: ")
            if confirm == "Y":
                return data[close_match[0]]
            else:
                return "Please enter correct word."
        else:
            return "Word does not exist. Please check."

#type word for definition
#"q" for quiting program
while True:
    word = input("Enter Word: ")
    if word != "q":
        output = translate(word.lower())
        index = 1
        if isinstance(output, list):
            for item in output:
                print(index, item)
                index +=1
        else:
            print(output)
    else:
        break