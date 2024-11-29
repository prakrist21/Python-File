'''
This a python program which will encrypt the given string and decrypt it.

'''

import random
def check(word):
    global encrp
    global space
    global spaceletter
    letter=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    space=random.randint(2,20)
    new=' '
    spacew=' '*space
    for x in word:
        new=new+x+spacew
    print("The word with space is ",new)
    spaceletter=''
    for x in range(space):
        new_letter=random.choice(letter)
        spaceletter=spaceletter+new_letter
    encrp=' '
    for x in word:
        encrp=encrp+x+spaceletter
    print("The encrypted word is ",encrp)

word=input("Ente the string for encryption: ")
check(word)
encrp=encrp.strip()
print("The decrypted string is ",encrp[::space+1])