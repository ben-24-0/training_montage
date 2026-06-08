
# def rec(i,n):
#     if(i>=n):
#         return n
#     print(i)
#     rec(i+1,n)
#     print(i-1)

# rec(1,5)

def fun(n, i=1):
    print(i, end=" ")

    if i < n:
        fun(n, i+1)
        print(i, end=" ")
fun(5)