def fastExpo(num,power):
    output=1
    while(power>0):

        if((power&1)!=0):
            output*=num
        
        num=num*num
        power=power>>1
    return output

print(fastExpo(4,3))
print(fastExpo(3,4))