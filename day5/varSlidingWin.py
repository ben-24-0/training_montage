li=[2,3,1,5,2,4,6,7,8,5,2,3] 
r,m,s,l=0,0,0,0
k=10
while(r<len(li)):
    s+=li[r]
    while s>k:  
        s-=li[l]
        l+=1
    length = r-l+1
    m = max(m,length)
    r+=1
print(m)
    

