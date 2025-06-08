def check(s):
    isPalindrome=False
    for x in range(0,len(s)//2):
        y=len(s)-x-1
        if(s[x]==s[y]):
            isPalindrome=True
        else:
            isPalindrome=False
    if(isPalindrome):
        print("It is a palindrome")
    else:
        print("It is not a palindrome")
check("pop")
check("nepal")