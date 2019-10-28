import mysql.connector
import json

configFile = open("config.json")
config = json.load(configFile)
configFile.close()

con = mysql.connector.connect(
    user=config["user"],
    password=config["password"],
    host=config["host"],
    database=config["database"]
)


def get_definition(word):
    cursor = con.cursor()
    cursor.execute("SELECT definition FROM Dictionary WHERE expression = %s", (word,))
    return cursor.fetchall()


search = input("Enter a word: ")
definitions = get_definition(search)

if definitions:
    for definition in definitions:
        print(definition[0])
else:
    print("Definition not found.")
