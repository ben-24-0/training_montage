

n = int(input())
f=1
for i in range (2,n**(0.5)+1,1):
    if(i%n==0):
        f=0
if(f):
    print("prime")
else:
    print("not prime")
