def transpose(arr):
    x=len(arr)
    y=len(arr[0])
    newArr=[[0 for i in range(x)]  for j in range(y)]
    for i in range(0,x):
        for j in range(0,y):
            newArr[j][i]=arr[i][j]
    print(newArr)


transpose([[10,20,30],[40,50,60]])
