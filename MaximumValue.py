#This program finds the maximum value from the list
arr=[1,5,2,7,3,4]
max=arr[0]
for x in range(1,len(arr)):
    if arr[x]>max:
        max=arr[x]
print("The maximum value from the list is ",max)
