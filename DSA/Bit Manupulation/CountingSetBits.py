def count(num):
    # Counting 1 in the given integer(in binary).
    count=0
    while(num>0):
        if((num&1)!=0):
            count+=1
        num=num>>1
    print("The number of set bits are ",count)


count(16)
count(15)