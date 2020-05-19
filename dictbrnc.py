import json

data = json.load(open("data.json"))

def translate(word):
    word = word.lower()
    if word in data:
        return data[word]
    else:
        return "word doesn't exist, please double check!"
word = input("Enter a word: ")
print(translate(word))