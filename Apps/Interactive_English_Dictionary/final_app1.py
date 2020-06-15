import mysql.connector
from difflib import get_close_matches

# implement exercise.py with app1.py

def translate(word):
    con = mysql.connector.connect(
        user="ardit700_student",
        password="ardit700_student",
        host="108.167.140.122",
        database="ardit700_pm1database"
    )

    word = word.lower()
    if word in data:
        query = cursor.execute("SELECT * FROM Dictionary WHERE Expression = '%s' " % word)
        results = cursor.fetchall()
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    elif len(get_close_matches(word, data.keys())) > 0:
        yn = input("Did you mean %s instead? Enter Y if yes, N if no: " % get_close_matches(word, data.keys())[0])
        if yn == "Y":
            return data[get_close_matches(word, data.keys())[0]]
        elif yn == "N":
            return "The word doesn't exist. Please double check it."
        else:
            return "We didn't understand your entry."
    else:
        return "The word doesn't exist. Please double check it."




cursor = con.cursor()

word = input("Enter word: ")

output = translate(word)

if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)





if results:
    for result in results:
        print(result[1])
else:
    print("No word found")
