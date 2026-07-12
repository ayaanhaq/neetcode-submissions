class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c={}
        for i in nums:
            if i not in c:
                c[i]=0
            c[i]+=1
        
        bucket=[]
        for i in range(len(nums)+1):
            bucket.append([])

        result=[]
        for num, freq in c.items():
            bucket[freq].append(num)
        
        print(bucket)
        result=[]
        for i in range(len(bucket)-1,-1,-1):
            result.extend(bucket[i])
            if len(result)==k:
                return result