def sentence_maker(phrases):
    caps = phrases.capitalize()
    question_list = ("What", "Why", "How", "Which", "When", "Where")

    if caps.startswith(question_list):
        phrase = f"{caps}?"
    else:
        phrase = f"{caps}."
    
    return phrase

sentence_list = []

while True:
    user_input = input("Enter sentence: ")
    if user_input == "end":
        break
    else:
        sentence_list.append(sentence_maker(user_input))

print(" ".join(sentence_list))