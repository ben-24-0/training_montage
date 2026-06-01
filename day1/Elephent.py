x = int(input())

if(x<1):
    print(0)

elif(x%5==0):
    print(x//5)
else:
    print(x//5+1)