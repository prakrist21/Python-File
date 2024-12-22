'''
Print the three most common characters along with their occurrence count.
'''
name=input("Enter any character: ")
sets=set(name)
lst=[]
for x in sets:
    c=name.count(x)
    lst.append([x,c])
def return_location(x):
    return x[1]
lst.sort(key=return_location,reverse=True)
print(f"The most repeating characters are {lst[:3]}")
    
    