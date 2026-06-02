a= int(input())
res=0

org=a
count=0

l=len(str(a))
while(a!=0):
    count+=1
    a=a//10

a=org
while(a!=0):
    rem = a % 10
    res = res + (rem**count)
    a= a//10


if(res==org):
    print("Armstrong")
else:
    print(" Not Armstrong")
    

