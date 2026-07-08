class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c={}
        for i in nums:
            if i not in c:
                c[i]=0
            c[i]+=1
        d= dict(sorted(c.items(), key=lambda items:items[1], reverse=True))
        l1=[]
        l2=[]
        for i in d.keys():
            l1.append(i)
        #print(l1)
        for i in range(k):
            l2.append(l1[i])
        return l2