class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        c={}
        for i in range(len(nums)):
            complement=target-nums[i]
            if complement in c:
                return [c[complement],i]
            c[nums[i]]=i
        return []