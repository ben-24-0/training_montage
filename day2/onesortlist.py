li = [ 6,4,5,3,2,1]

li.sort() # 1 2 3 4 5 6
res=[]
for i in li:
    if i %2 ==0:
        res.append(i)
    else:
        res.insert(0,i)

print(res)