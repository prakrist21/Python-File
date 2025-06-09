def count(num):
    # Count the number of set bits in an integer.
    count=0
    while(num>0):
        if((num&1)!=0):
            count+=1
        num=num>>1
    print("The number of set bits are ",count)


count(16)
count(15)