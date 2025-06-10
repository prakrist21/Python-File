def setIthbit(num,i):
    # sets the ith bit to 1; eg: num=10000(16),i=2 ; output=10100(20)
    BitMask=1<<i
    return num|BitMask

print(setIthbit(16,0))
print(setIthbit(16,1))
print(setIthbit(16,2))
print(setIthbit(16,3))