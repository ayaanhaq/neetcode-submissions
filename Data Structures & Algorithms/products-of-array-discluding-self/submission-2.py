class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre=[]
        post=[]
        prefix=1
        postfix=1
        for i in range(len(nums)):
            pre.append(prefix)
            prefix*=nums[i]
        print(pre)
        for i in range(len(nums)-1,-1,-1):
            post.append(postfix)
            postfix*=nums[i]
        post=post[::-1]
        print(post)
        l=[]
        for i in range(len(pre)):
            l.append(pre[i]*post[i])
        return l