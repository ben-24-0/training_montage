l=[2,3,1,5,2,4,6,7,8,5,2,3]
k=3

i=0
maxsum=0
while(i<len(l)-1):
    sm=0
    j=i
    c=0
    while(c<k and j<len(l)):
        sm =  sm + l[j]
        j+=1
        c+=1
    if(sm>maxsum):
        maxsum=sm
    i+=1
print(maxsum)
