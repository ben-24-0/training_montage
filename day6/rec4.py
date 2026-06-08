
def rec(i,n):
    if(i>n):
        return n

    if(i%2==0):
        print(i)
        rec(i+2,n)

rec(2,10)