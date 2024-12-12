#This program finds the LCM (Lowest Common Multiple) between given numebers
num=int(input("Enter the number of numbers you want to enter: "))
lst=[]
m=1
for x in range(num):
    number=int(input("Enter a number: "))
    lst.append(number)

for x in lst:
    m=m*x

for x in range(2,m):
    lstm=0
    try:
        for o in lst:
            lstm+=x%o
        if lstm==0:
            print(f"The LCM is: ",x)
            break
    except:
        pass