li = list((input()).split())
print(li)

count = 0
mp={}
for i in li:
    if i in mp:
        mp[i]+=1
    else:
        mp[i] =1



l2=[]
for i in mp.keys():
    l2.append(i)

print(l2)


