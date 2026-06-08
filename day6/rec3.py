
def rec(n):
    if(n==0):
        return 1
    if(n%2==0):
        print(n)
        rec(n-2)

rec(10)