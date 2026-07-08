class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        c={}
        for i in range(len(nums)):
            s=target-nums[i]
            if s in c:
                return [c[s],i]
            c[nums[i]]=i
        return []