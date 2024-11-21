import random
dic={'pani':'water',
     'khutta':'leg',
     'bhat':'rice',
     'luga':'clothes',
     'rati':'night',
     'bihana':'morning',
     'seto':'white',
     'ghar':'house',
     'bato':'road'}
pair_word=random.choice(list(dic.items()))
guess_dic={}
print("-------Guess the english word from nepali word-------")
print("The nepali word is: ",pair_word[0])
final_ans=pair_word[1]
x=1
guess=input('Enter your answer: ')
guess_dic[x]=guess
while guess.upper() != final_ans.upper():
  if guess.upper()==final_ans.upper():
    print("success")
  else:
    hint_guess=final_ans[:x]
    if hint_guess.upper()==final_ans.upper():
        print("you failed, correct answer was ",final_ans)
        break
    Choice=int(input("The answer is incorrect. Do you want to quit or take a hint\n1.Quit\n2.Hint\nEnter: "))
    if Choice==1:
      print("You remained unsuccessful")
      print(f"The correct word is {final_ans}")
      break
    elif Choice==2:
      print("Incorrect\n-----------------------\nYour hint is: ",hint_guess)
      guess=input('Enter your answer: ')
      if guess.upper()==final_ans.upper():
        print("success!!")
      guess_dic[x+1]=guess
      x=x+1
    else:
      print("Invalid!")
print("Your guess history was ",guess_dic)
