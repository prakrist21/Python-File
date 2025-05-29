def binarySearch(arr,target):
    start=0
    end=len(arr)-1
    while(end>=start):
        mid=(start+end)//2
        if(arr[mid]==target):
            return mid
        elif(arr[mid]>target):
            end=mid-1
        else:
            start=mid+1
    return -1




print(binarySearch([1,2,4,5,7,8,21],3))
print(binarySearch([1,2,4,5,7,8,21],2))
print(binarySearch([1,2,4,5,7,8,21],21))
