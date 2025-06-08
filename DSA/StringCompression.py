def check(s):
    count=1
    newString=""
    for i in range(0,len(s)):
        try:
            if(s[i]==s[i-1]):
                continue
        except:
            pass
        while(i<len(s)-1 and s[i]==s[i+1]):
            count+=1
            i+=1
        newString+=s[i]
        if(count>1):
            newString+=str(count)
        
        count=1
    print(newString)

check("aaaabcdd")
check("abcdef")
