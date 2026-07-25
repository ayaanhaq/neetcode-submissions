class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        maxwindow=[]
        for right in range(k,len(nums)+1):
            window=nums[right-k:right]
            maxwindow.append(max(window))
        return maxwindow