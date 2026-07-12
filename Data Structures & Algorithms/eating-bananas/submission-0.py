class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left=1
        right=max(piles)
        result=right

        while left<=right:
            mid=(left+right)//2
            time=0
            for i in piles:
                time+=math.ceil(i/mid)
            if time>h:
                left=mid+1
            else:
                right=mid-1
                result=mid
        return result