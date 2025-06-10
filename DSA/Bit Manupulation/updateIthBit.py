def update(num,i,newbit):
    BitMask1=~(1<<i)
    num=num&BitMask1
    BitMask2=(newbit<<i)
    return num | BitMask2

print(update(15,2,0))
print(update(16,2,1))