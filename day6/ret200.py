def rec(n):
    if(n==1):
        print(1)
        t=200
        return t
    t=rec(n-1)
    print(n,end=" ")
    return t
    
x=rec(5)
print(x)