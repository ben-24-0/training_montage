s = "aaaaabbbbbcccaab"

i=0
j=0
nw=""
while(i<len(s)):
    count=0
    j=i
    while(j<len(s)):
        if(s[i]!=s[j]):
            break
        j+=1
        count+=1
    nw = nw + s[i]+ str(count)
    i+=count
print(nw)


