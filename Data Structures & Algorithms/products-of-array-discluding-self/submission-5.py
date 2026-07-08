class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix=1
        suffix=1
        pre=[]
        post=[]

        for i in range(len(nums)):
            pre.append(prefix)
            prefix*=nums[i]
        
        for i in range(len(nums)-1,-1,-1):
            post.append(suffix)
            suffix*=nums[i]
        
        post=post[::-1]
        result=[]
        for i in range(len(nums)):
            result.append(pre[i]*post[i])
        return result