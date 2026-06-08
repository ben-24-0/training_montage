
def rec(i,n):
    if(i>n):
        return n
    print(i)
    rec(i+1,n)

rec(1,5)