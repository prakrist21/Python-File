def clear(num,i):
    # Removes the ith bit and converts it into 0
    # For eg: num=1111(15),i=2 ; output=1011(11)
    BitMask=~(1<<i)
    return num&BitMask


print(clear(15,2))