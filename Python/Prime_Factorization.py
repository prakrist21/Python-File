def prime(num):
    lst=[]
    div=2
    while num!=1:
        if num%div==0:
            lst.append(div)
            num=num/div
        else:
            div=div+1
    print(lst)

prime(120)