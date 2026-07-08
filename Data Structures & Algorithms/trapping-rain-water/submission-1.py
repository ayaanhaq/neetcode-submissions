class Solution:
    def trap(self, height: List[int]) -> int:
        left=0
        right=len(height)-1
        l_max=height[left]
        r_max=height[right]
        water=0

        while left<right:
            if l_max<r_max:
                left+=1
                l_max=max(l_max, height[left])
                water+=l_max-height[left]
            else:
                right-=1
                r_max=max(r_max, height[right])
                water+=r_max-height[right]
        return water