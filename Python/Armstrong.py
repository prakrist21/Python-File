num=int(input("Enter any number: "))
check=num
sum=0
while num != 0:
    rem=num%10
    sum=sum+rem**3
    num=num//10
if check==sum:
    print(f"{check} is a armstrong number")
else:
    print(f"{check} is not an armstrong number")