l=[2,3,1,5,2,4,6,7,8,5,2,3]
k=3
i=0
sm=0
while(i<k):
    sm += l[i]
    i+=1

totmax=0
~
for i in range (1,len(l)-k+1):
    sm = sm - l[i-1] + l[i+k]
    # print(sm)
    totmax = max(sm,totmax)
print(totmax)




