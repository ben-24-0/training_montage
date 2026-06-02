a= int(input())
res=0
while(a!=0):
    rem=a%10
    res = res*10+rem
    a= a//10

print(res)