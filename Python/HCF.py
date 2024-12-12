num=int(input("Enter the number of numbers you want to enter: "))
lst=[]
m=1
answers=[]
for x in range(num):
    number=int(input("Enter a number: "))
    lst.append(number)
maximum=max(lst)
for x in range(1,maximum//2):
    condition=all(m%x==0 for m in lst)
    if condition==True:
        answers.append(x)
print("The HCF is:",max(answers))
