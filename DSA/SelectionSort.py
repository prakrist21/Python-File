

def sorting(arr):
    print(arr)
    for x in range(0,len(arr)-1):
        index=x
        for y in range(x,len(arr)-1):
            print("index: ",index," y+1: ",y+1," | arr[index]: ",arr[index]," |arr[y+1]: ",arr[y+1]," | arr: ",arr)
            if(arr[index]>arr[y+1]):
                index=y+1
        temp=arr[x]
        arr[x]=arr[index]
        arr[index]=temp
        # print(arr)
        # print("\n")

    print(arr)

sorting([12,5,2,1,19,7,0,3])