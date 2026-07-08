class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        if len(nums)<2:
            return nums[0]
        m=0
        count=1
        for i in range(len(nums)-1):
            if nums[i]==1 and nums[i+1]==1:
                count+=1
                if count>m:
                    m=count
            else:
                count=1
        if m==0 and 1 in nums:
            return 1
        return m