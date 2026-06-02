a= int(input())
res=0

org=a
count=0

l=len(str(a))
while(a!=0):
    count+=1
    a=a//10
print(l)
a=org


res=0

while(a!=0):
    rem=a%10
    res = res*10+rem
    a= a//10
sm=0

while(res!=0):
    rem = res % 10
    sm = sm + (rem**count)
    count-=1
    res = res//10

print(sm)