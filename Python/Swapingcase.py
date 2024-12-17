word='This is A test StaTemenT'
newword=''
for x in range(len(word)):
    if word[x].lower()==word[x]:
        newword+=word[x].upper()
    else:
        newword+=word[x].lower()
print("The string after case swapping is: ",newword)
