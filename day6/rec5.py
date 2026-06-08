
def rec(n):
    if(n==0):
        return 1
    print(n)
    rec(n-1)
    print(n+1)

rec(5)