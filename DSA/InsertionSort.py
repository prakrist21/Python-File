def sorting(arr):
    for x in range(1,len(arr)):
        curr=arr[x]
        prev=x-1

        while(prev>=0 and arr[prev]>curr):
            arr[prev+1]=arr[prev]
            print(arr)
            prev-=1
        arr[prev+1]=curr
    print(arr)

sorting([5,4,3,2,1])