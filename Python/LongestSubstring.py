# Longest Substring Without Repeating Characters

word=input("Enter a word: ")
lst=[]
for x in range(len(word)):
    new=f'{word[x]}'
    for y in word[x+1:]:
        if y in new:
            break
        new=new+y
    lst.append(new)
# print(lst)
# print(max([len(x) for x in lst]))

for x in lst:
    if len(x)==max([len(x) for x in lst]):
        print(f"The longest substring without reapating a character is: {x} with length {max([len(x) for x in lst])}")
