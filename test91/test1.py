rows=5
while rows>=1:
    s,p,s2=5,1,5
    while s>=1 and p<=5:
        print(end=" "*s)
        print("*"*p)
        s-=1
        p+=1
        
    print()
    rows-=1