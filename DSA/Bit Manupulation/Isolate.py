def isolate(num):
    # Isolate the rightmost 0 bit of a number.
    print((~num)&(num+1))
    

# isolate(24)
isolate(10)
isolate(13)