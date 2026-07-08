class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre=[]
        post=[]
        prefix=1
        postfix=1
        for i in nums:
            pre.append(prefix)
            prefix*=i
        for i in range(len(nums)-1,-1,-1):
            post.append(postfix)
            postfix*=nums[i]
        post=post[::-1]
        print(pre)
        print(post)
        l=[]
        for i in range(len(nums)):
            l.append(pre[i]*post[i])
        return l