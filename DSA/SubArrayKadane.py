import math
def kadane(arr):
    maxm=0
    currentMax=0
    for x in range(len(arr)):
        currentMax+=arr[x]
        if currentMax<0:
            currentMax=0
        maxm=max(maxm,currentMax)
    return maxm



print(kadane([1,3,-5,6,-2,4,6,2,-3]))
print(kadane([1,-2,3,4,5,6,-3]))