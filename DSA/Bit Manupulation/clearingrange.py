def clear(num,i,j):
    bitmask1=(~0)<<j+1
    bitmask2=(1<<i)-1
    bitmask=bitmask1|bitmask2
    return num&bitmask
print(clear(31,0,3))
print(clear(31,1,3))
print(clear(31,2,3))
print(clear(31,3,3))
