def convert(num1,num2):
    # Given two numbers, find the number of bits needed to convert one to the other.
    num=num1^num2
    count=0

    while(num>0):
        if((num&1)!=0):
            count+=1
        num=num>>1

    print("The number of bits needed to convert one to the other is ",count)


convert(19,27)
