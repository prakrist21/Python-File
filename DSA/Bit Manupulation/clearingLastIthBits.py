def clear(num,i):
    # Deletes the last ith bit from the num
    # eg: num=1111(15),i=2 ; output: num=1100(12)
    BitMask=~(0)<<i
    return num & BitMask

print(clear(15,2))
print(clear(31,1))