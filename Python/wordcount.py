word="Nepal Premier League 2024 Points Table: Chitwan Rhinos leapfrog Janakpur Bolts to claim the top spot in the NPL Season 1 standings after absolutely annihilating Pokhara Avengers by 87 runs in match 5 of NPL 2024 on Tuesday (December 3) in Kirtipur."
dict={}
count=0
lst=[]
for x in word.split(" "):
    count=count+1
    lst.append(x)
setA=set(lst)
for x in setA:
    dict[x]=word.count(x)
print("The number of each word count is ",dict)
print("The number of words is ",count)
