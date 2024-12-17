def fibo(num):
    if num==1:
        return 1
    elif num==2:
        return 1
    else:
        return fibo(num-1)+fibo(num-2)

a=fibo(10)
print(a)
    