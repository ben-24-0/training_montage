l = [1,2,3,4,5,6,7]
k=3
print(l)
i,j = 0,k
leng=len(l)
temp=0
while(i<k):
    l[i] ,l[j-1] = l[j-1],l[i]
    i+=1
print(l)
i=k
j=leng-1
while(i<j):
    l[i],l[j] = l[j],l[i]
    i+=1
    j-=1

i=0  
print(l)
j=leng-1
while(i<j):
    l[i],l[j] = l[j],l[i]
    i+=1
    j-=1

print(l)