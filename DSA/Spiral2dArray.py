def spiral(arr):
    m=len(arr) #number of rows
    n=len(arr[0]) #number of columns
    startCol=0
    startRow=0
    endRow=m-1
    endCol=n-1

    while(startCol<=endCol and startRow<=endRow):
        # Top Part
        for x in range(startCol,endCol+1):
            print(arr[startRow][x],end=" ")
        
        # Right Part
        for x in range(startRow+1,endRow+1):
            print(arr[x][endCol],end=" ")
        
        # Bottom Part
        for x in range(endCol-1,startCol-1,-1):
            if(startRow==endRow):
                break
            print(arr[endRow][x],end=" ")
        
        # Left Part
        for x in range(endRow-1,startRow,-1):
            if(startCol==endCol):
                break
            print(arr[x][startCol],end=" ")
        
        startCol+=1
        startRow+=1
        endCol-=1
        endRow-=1

    print("\n")

spiral([[1,2,3],[4,5,6],[7,8,9]])
spiral([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])
spiral([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
spiral([[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]])