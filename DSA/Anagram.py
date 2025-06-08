def check(s,s1):
    lst1=sorted(list(s))
    lst2=sorted(list(s1))
    if(lst1==lst2):
        print("They are Anagram")
    else:
        print("They are not anagram")

check("care","race")
check("case","vase")