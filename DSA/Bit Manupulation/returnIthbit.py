def returnIth(num,i):
    # Returns the ith bit of any number
    BitMask=1<<i
    val=num&BitMask
    if(val==0):
        return 0
    else:
        return 1



print(returnIth(15,2))
print(returnIth(16,2))