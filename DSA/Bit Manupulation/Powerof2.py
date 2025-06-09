def check(num):
    # Check if a number is a power of two using bit manipulation.
    value=num & (num-1)
    if(value==0):
        print("The given number is the power of 2")
    else:
        print("The given number is not the power of 2")



check(10)
check(16)
check(17)