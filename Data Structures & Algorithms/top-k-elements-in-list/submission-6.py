class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c={}
        for i in nums:
            if i not in c:
                c[i]=0
            c[i]+=1
        
        print(c)

        n=len(nums)+1
        bucket=[0]*n
        for i in range(len(bucket)):
            bucket[i]=[]
        print(bucket)

        for num, value in c.items():
            bucket[value].append(num)
        
        result=[]
        for i in range(len(bucket)-1,0,-1):
            result.extend(bucket[i])
            if len(result)==k:
                return result
        print(bucket)