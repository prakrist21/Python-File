def sorting(arr):
    maxNum=max(arr)
    lst=[0]* (maxNum+1)
    for x in arr:
        lst[x]+=1
    
    y=0
    for x in range(0,len(lst)):
        while lst[x] > 0:
            arr[y]=x
            y+=1
            lst[x]-=1
    print(arr) 

sorting([5,4,3,2,1])