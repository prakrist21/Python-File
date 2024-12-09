word=input("Enter any string: ")
for x in range(len(word)):
    if x%2==0:
        print(word[x],end=" ")
print("\n")