# This program converts all lower case into upper case and uppercase into lower case from the sentence.
word=input("Enter a string: ")
newword=''
for x in range(len(word)):
    if word[x].lower()==word[x]:
        newword+=word[x].upper()
    else:
        newword+=word[x].lower()
print("The string after case swapping is: ",newword)
