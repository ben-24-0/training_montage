n= int(input())
li = list(map(int,input().split(" ")))

police=0
unsolved=0
print(li)
for i in li:
    if i == -1:
        if police > 0:
            police-=1
        else:
            unsolved+=1
    elif i >=1:
        police+=i



print(unsolved)

