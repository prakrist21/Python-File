import random
import json
import datetime

name=input("Enter your name: ")
print(f"{name}, Welcome to Chatbot. You can ask anything about our college.")
with open('Projects\\new\\one.json') as f:
    dict=json.load(f)

f1=open("Projects\\new\\conversation.txt","a")

agent=['Alex','John','Jimmy','Ryan','Denis','Roger']
user_agent=random.choice(agent)
print(f"Hello, I am your agent {user_agent}")

def date():
    time=datetime.datetime.now().strftime("%m-%d-%Y %H:%M:%S")
    return time

choice=input("Ask Chatbot: ").lower()
f1.write(f"{date()} Question: {choice}\n")

while choice != 'bye':
    disconnect=random.randint(1,100)
    if disconnect<=10:
        print("Sorry, network disconnected !!!")
        f1.write(f"{date()} Sorry, network disconnected !!!")

        break

    lst=set([x for x in choice.split(' ')])
    keys=set(dict.keys())
    if lst.intersection(keys) != set():
        for x in choice.split(' '):
            if x in dict.keys():
                answer=random.choice(dict[x])
                f1.write(f"{(date())} Answer: {answer}\n")
                print("Chatbot: ",answer)
                break
    else: 
        answer=random.choice(dict['noreply'])
        print("Chatbot: ",answer)
        f1.write(f"{date()} Answer: {answer}\n")
    choice=input("Ask another question to Chatbot or use 'bye' to exit: ").lower()
    f1.write(f"{date()} Question: {choice}\n")

bye="Bye! It was nice talking with you"
print(bye)
f1.write(f"{date()} Answer: {bye}\n\n")

