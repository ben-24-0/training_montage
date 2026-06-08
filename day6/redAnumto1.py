def fun (n,i=0):
    if n==1:
        x=i
        return x
    elif n%2==0:
        x=fun(n//2,i+1)
    else:
        x=min(fun(n-1,i+1),fun(n+1,i+1))
    return x



print(fun(int(input())))