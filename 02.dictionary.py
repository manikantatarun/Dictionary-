import json
from difflib import get_close_matches

data = json.load(open("data.json"))
def search(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.capitalize() in data:
        return data[word.capitalize()]
    elif len(get_close_matches(word,data.keys()))>0:
        print("did you mean %s insted you typed "%get_close_matches(word, data.keys())[0])
        decide = input("if Yes type 'y' \n if No type 'n' ")

        if decide == "y":
            return data[get_close_matches(word , data.keys())[0]]
        elif decide == "n":
            return("You paw steps on wrong keys")
        else:
            return ("You have entered wrong choice")
    else:
        return ("You paw steps on wrong keys")


word: str = input("enter the word to search")
output = search(word)
if type(output) == list:
    for x in output:
        print("*"+x)
else:
    print(word)

