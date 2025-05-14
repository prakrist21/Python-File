import random
name=input("Enter your name: ")
print(f"{name}, Welcome to Chatbot. You can ask anything about our college.")
dict={'name':['The name of the college is The Future College'],
      'hi':['Hello, How can I help you', 'Welcome, How may I help you'],
      'principle':['The name of our Principle is Mr.Smith'],
      'admission':['The admission will start from the second week of September. For more details contact us or visit our website www.www.com'],
      'location':['Our college is located in Kathmandu, Nepal'],
      'facilities': ['We have different facilities like sports, cafe, library, VR room, etc'],
      'noreply':[f'Sorry {name} I am not trained for this',f'Hey {name}, I dont have an answer for this',f'Hey {name}, I dont have an reply for this']}
agent=['Alex','John','Jimmy','Ryan','Denis','Roger']
user_agent=random.choice(agent)
print(f"Hello, I am your agent {user_agent}")
choice=input("Ask Chatbot: ").lower()
while choice != 'bye':
    disconnect=random.randint(1,100)
    if disconnect<=10:
        print("Sorry, network disconnected !!!")
        break
    lst=set([x for x in choice.split(' ')])
    keys=set(dict.keys())
    # print(lst.intersection(keys))
    if lst.intersection(keys) != set():
        for x in choice.split(' '):
            if x in dict.keys():
                answer=random.choice(dict[x])
                print(answer)
                break
    else: 
        print(random.choice(dict['noreply']))
    choice=input("Ask another question to Chatbot or use 'bye' to exit: ").lower()
print("Bye! It was nice talking with you")
