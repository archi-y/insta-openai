from instagrapi import Client
import json,openai,time,random,signal

#Instagram login from json file
cl = Client(json.load(open('login.json')))

#OpenAI Key from key file
openai.api_key = open("openai.key", "r").read()

print("-----------------------|  InstaGPT v1.1  |-----------------------")

def Read():
    try:
    #Try to get latest messages
        thread = cl.direct_threads(1,selected_filter="unread")[0] 
        msg = cl.direct_messages(thread.id,1)[0].text
        return msg
    except:
        return None

def Send(message):
    thread = cl.direct_threads(1,selected_filter="unread")[0] 
    cl.direct_send(message, thread_ids=[thread.id])

def Wait(random):   
    print("Waiting " + str(random) + "s")
    time.sleep(random)   

def Ai(start):
    fr = open("context_base.txt", "r", encoding='utf-8').read() #fr = file read
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=fr + str(start) + "\nFred:",  #Send Context, the sentence and then ask the ai to complete
        temperature=0.9,
        max_tokens=150,
        top_p=1,
        frequency_penalty=0.0,
        presence_penalty=0.6,
        stop=[" Human:", " Fred:"]
    )
    results = response['choices'][0]['text']
    print(results)
    return results

def handler(signum, frame):
    res = input("Ctrl-c was pressed. Do you really want to exit? y/n ")
    if res == 'y':
        exit(1)

signal.signal(signal.SIGINT, handler)

while True:
    msg = Read()
    if msg != None: #If there is a valid message
        print("Message : ")
        print(msg)
        print("Ai answer : ")
        try: #idk maybe errors could happen
            Send(Ai(msg))
            print("Sent\n")
        except:
            print("Message could not be sent\n")
    else:
        print("No new message\n") 
        #Add delay to avoid potential bans 
        Wait(random.randint(15,200))
