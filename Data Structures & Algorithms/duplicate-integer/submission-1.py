class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        c={}
        for i in nums:
            if i not in c:
                c[i]=0
            c[i]+=1
        for c in c.values():
            if c>1:
                return True
        return False