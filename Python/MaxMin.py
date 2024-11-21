def check(lst):
    global checkmax
    global checkmin
    checkmin=lst[0]
    checkmax=lst[0]
    for x in lst:
        if x < checkmin:
            checkmin=x
    for x in lst:
        if x > checkmax:
            checkmax=x
        
    print(checkmin,checkmax)
lst=[10,3,14,2,9,21]
check(lst)

for x in range(checkmin,checkmax+1):
    if x not in lst:
        print(x,end=" ")