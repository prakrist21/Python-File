# Compares particular element to sort 
def sorting(arr):
    for x in range(0,len(arr)-1):
        for y in range(0,len(arr)-1-x):
            if arr[y]>arr[y+1]:
                temp=arr[y]
                arr[y]=arr[y+1]
                arr[y+1]=temp
            # print(arr)
    print("The sorted array is: ",arr)

sorting([5,3,1,4,9,0])