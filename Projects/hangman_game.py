import random
counter=1
def counters(counter):
    if counter==1:
        print("     ---------")
        print("     |       |")
        print("     |       ")
        print("     |       ")
        print("     |       ")
        print("     |       ")
        print("     |       ")
        print("     |       ")
        print("    ---")
        print("\n")
    elif counter==2:
        print("     ---------")
        print("     |       |")
        print("     |       O")
        print("     |       ")
        print("     |       ")
        print("     |       ")
        print("     |       ")
        print("     |       ")
        print("    ---")
        print("\n")
    elif counter==3:
        print("     ---------")
        print("     |       |")
        print("     |       O")
        print("     |       |")
        print("     |       ")
        print("     |       ")
        print("     |       ")
        print("     |       ")
        print("    ---")
        print("\n")
    elif counter==4:
        print("     ---------")
        print("     |       |")
        print("     |       O")
        print("     |      /|")
        print("     |       ")
        print("     |       ")
        print("     |       ")
        print("     |       ")
        print("    ---")
        print("\n")
    elif counter==5: 
        print("     ---------")
        print("     |       |")
        print("     |       O")
        print("     |      /|\\")
        print("     |       ")
        print("     |       ")
        print("     |       ")
        print("     |       ")
        print("    ---")
        print("\n")
    elif counter==6:
        print("     ---------")
        print("     |       |")
        print("     |       O")
        print("     |      /|\\")
        print("     |       |")
        print("     |       ")
        print("     |       ")
        print("     |       ")
        print("    ---")
        print("\n")
    elif counter==7:
        print("     ---------")
        print("     |       |")
        print("     |       O")
        print("     |      /|\\")
        print("     |       |")
        print("     |      /")
        print("     |       ")
        print("     |       ")
        print("    ---")
        print("\n")
    elif counter==8:
        print("     ---------")
        print("     |       |")
        print("     |       O")
        print("     |      /|\\")
        print("     |       |")
        print("     |      / \\")
        print("     |       ")
        print("     |       ")
        print("    ---")
        print("\n")
    elif counter==9:
        print("     ---------")
        print("     |       |")
        print("     |       O")
        print("     |       //\\")
        print("     |        |")
        print("     |       / \\")
        print("     |        ")
        print("     |        ")
        print("    ---")
        print("\n")
        print("Sadly you lost the game:!")
c=1
worddict={'nepal':'A country in south Asia',
          'water':'Tasteless,courless liquid, essential for life',
          'watermelon':'Green outside, red inside Fruit',
          'mango':'King of fruits',
          'football':'Famous sport in the world',
          'youtube':'Platform for watching videos',
          'computer':'electronic device for processing and storing data','evening':'After afternoon, before night',
          'blue':'color of sea, ocean or sky'}
word=random.choice(list(worddict.keys()))
hint=worddict[word]
correct=[]
incorrect=[]
guesslst=[]
for x in range(len(word)):
    guesslst.append("_")
counters(c)
print("Word: "," ".join(guesslst),"\nhint: ",hint)
letter=input("Enter a alphabet: ")

while True:
    if letter in word:
        correct.append(letter)
        for y in range(len(word)):
            if letter==word[y]:
                guesslst[y]=letter
    else:
        incorrect.append(letter)
        c+=1
    counters(c)
    print("Word: "," ".join(guesslst),"\nhint: ",hint)
    print("Correct Letters: ",list(set(correct)))
    print("Incorrect Letters: ",list(set(incorrect)))
    if c==9:
        break
    if guesslst.count('_')==0:
        print("Correct! You guessed it right")
        break
    letter=input("Enter a alphabet: ")