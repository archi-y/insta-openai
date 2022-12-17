from instagrapi import Client
import json

username = input("Username : ")
password = input("Password : ")
openai = input("OpenAI API Key : ")
try:
    cl = Client()
    cl.login(username,password)
    json.dump(
        cl.get_settings(),
        open('login.json', 'w')
    )
except:
    print("Can't login to instagram")

f = open("openai.key", "w")
f.write(openai)
f.close()

cl = Client(json.load(open('login.json')))
