def update(num,i,newbit):
    # Updates the ith bit into newbit
    # eg: num=1111(15),i=2,newbit=0 | output: num=1011(11)
    BitMask1=~(1<<i)
    num=num&BitMask1
    BitMask2=(newbit<<i)
    return num | BitMask2

print(update(15,2,0))
print(update(16,2,1))