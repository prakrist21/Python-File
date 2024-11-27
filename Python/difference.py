'''
Write a Python program that finds two numbers x and y, both between 1 and 99, such that the difference of their squares is equal to a target value (in this case, 42). Print the values of x and y when they meet the condition.
'''
target=42
for x in range(1,100):
    for y in range(1,100):
        if x**2 - y**2 == target:
            print("Use square of : ",x,y)
            break
