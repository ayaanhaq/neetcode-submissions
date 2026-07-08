class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c={}
        for i in nums:
            if i not in c:
                c[i]=0
            c[i]+=1
        dic=sorted(c.items(), key=lambda x:x[1])
        dic=dic[::-1]
        l=[]
        for i in range(k):
            l.append(dic[i][0])
        return l