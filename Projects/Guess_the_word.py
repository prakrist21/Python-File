import random
wordlst=['nepal','water','watermelon','mango','football','youtube','computer','evening','blue']
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
guesslst=[]
for x in range(len(word)):
    guesslst.append("_")
print("word: "," ".join(guesslst),"\nHint: ",hint)
guess=input("Enter your Guess: ").lower()
while word!=guess:
    for x in range(len(guess)):
        if guess[x] in word:
            if x==word.index(guess[x]):
                guesslst[x]=guess[x]
    print("word: "," ".join(guesslst),"\nHint: ",hint)
    guess=input("Enter your Guess: ").lower()

print("Correct!")

