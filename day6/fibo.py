def fibo(n):
    if( n==1 or n==0):
        return 1
    return fibo(n-1)+fibo(n-2)

# 0 1 1 2 3 4

print(fibo(5))

