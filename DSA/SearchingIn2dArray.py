def search(arr,target):
    x=0
    y=len(arr[0])-1

    while (x<len(arr) and y>=0):
        key=arr[x][y]

        if(key==target):
            print("Target found at: (",x,",",y,")")
            break
        elif(target>key):
            x+=1

        elif(target<key):
            y-=1
    if(key!=target):
        print("The target is not in the array.")

def search2(arr,target):
    # Method 2: by accessing arr[len(arr)-1][0]
    x=len(arr)-1
    y=0

    while(x>=0 and y<len(arr[0])):
        key=arr[x][y]
        if(key==target):
            print("Target found at: (",x,",",y,")")
            break

        elif(key>target):
            x-=1
        
        elif(key<target):
            y+=1
            
    if(key!=target):
        print("Target not in array")

# Search 1
search([[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]],3)
search([[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]],25)
search([[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]],29)
# Search 2
search2([[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]],3)
search2([[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]],25)
search2([[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]],29)