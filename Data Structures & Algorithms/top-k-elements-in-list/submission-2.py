class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c={}
        for i in nums:
            if i not in c:
                c[i]=0
            c[i]+=1
        d= dict(sorted(c.items(), key=lambda item:item[1], reverse=True))
        l=[]
        for key, val in d.items():
            l.append(key)
        r=[]
        for i in range(k):
            r.append(l[i])
        return r