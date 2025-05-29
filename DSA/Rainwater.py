def trappingRainwater(arr):
    left=[0]* (len(arr)-1)
    right=[0]* (len(arr)-1)

    left.insert(0,arr[0])
    right.insert(len(arr)-1,arr[len(arr)-1])
    for x in range(1,len(arr)):
        left[x]=max(left[x-1],arr[x])
    
    for y in range(len(arr)-2,-1,-1):
        # print(y)
        right[y]=max(arr[y],right[y+1])
    trappedWater=0
    for z in range(len(arr)):
        side=min(left[z],right[z])
        currentWater=side-arr[z]
        trappedWater+=currentWater
    return trappedWater



print(trappingRainwater([4,0,9,3,2,5,1,6]))


