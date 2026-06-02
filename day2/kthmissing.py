class Solution(object):
    def findKthPositive(self, arr, k):
        li = []
        i=1
        count=0
        # print(li[k-1])
        if(len(arr)<=1000  and k<=1000):
            while(len(li)<k):
                if i not in arr:
                    li.append(i)
                    # print(li)
                i+=1
                count+=1
            return li[k-1]
        

//optimal 
class Solution(object):
    def findKthPositive(self, arr, k):
        s = set(arr)

        i = 1
        count = 0

        while True:
            if i not in s:
                count += 1

                if count == k:
                    return i

            i += 1