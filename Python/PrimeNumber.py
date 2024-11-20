#This program checks whether the number is prime or composite
num=int(input("Enter a number: "))
div=num
count=0
for x in range(2,num//2+1):
    if num % x ==0:
        count+=1
if count>0:
    print("Its Composite number")
else:
    print("Its Prime")

    
    