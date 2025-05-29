def stock(arr):
    buy=arr[0]
    sell=0
    maxProfit=0
    for x in range(len(arr)):
        sell=arr[x]
        if sell>buy:
            profit=sell-buy
            maxProfit=max(profit,maxProfit)
        else:
            buy=arr[x]
        
    return maxProfit

print(stock([7,2,9,5,1,4])) #7
print(stock([1, 2, 3, 4, 5])) #4
print(stock([5, 4, 3, 2, 1])) #0
print(stock([7, 1, 5, 3, 6, 4])) #5
print(stock([2, 4, 1, 7])) #6
print(stock([10, 9, 8, 7, 6])) #0
print(stock([10])) #0
print(stock([2, 1])) #0
print(stock([1, 2])) #1