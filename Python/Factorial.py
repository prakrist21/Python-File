# Printing factorial of a given number using recursion

def fact(num):
    if num==1:
        return 1
    else:
        return num * fact(num-1)
num=int(input("Enter a number: "))
print(f"The factorial of {num} is {fact(num)}.")