class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix=1
        postfix=1
        pre=[]
        post=[]

        for i in range(len(nums)):
            pre.append(prefix)
            prefix*=nums[i]

        for i in range(len(nums)-1,-1,-1):
            post.append(postfix)
            postfix*=nums[i]

        print(pre)
        post=post[::-1]
        result=[]
        for i in range(len(nums)):
            result.append(pre[i]*post[i])
        return result