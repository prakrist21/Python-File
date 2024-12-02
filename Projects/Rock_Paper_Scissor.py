import random
dict={1:'rock',2:'scissor',3:'paper'}
def rockpaperscissor():
    player=int(input("1.Rock\n2.Scissor\n3.Paper\nEnter your choice: "))
    computer=random.randint(1,3)
    print("You chose: ",dict[player])
    print("Computer chose: ",dict[computer])
    if (computer==1 and player==2) or (computer==2 and player==3) or (computer==3 and player==1):
        print("Sadly you lost!")
    elif (computer==1 and player==3) or (computer==2 and player==1) or (computer==3 and player==2):
        print("Congratulations! you won")
    elif computer==player:
        rockpaperscissor()
rockpaperscissor()
