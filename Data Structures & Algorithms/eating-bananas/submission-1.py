class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        rate=max(piles)
        left=1
        right=rate

        while left<=right:
            mid=(left+right)//2
            time=0
            for i in piles:
                time+=math.ceil(i/mid)
            if time<=h:
                right=mid-1
                rate=mid
            else:
                left=mid+1
        return rate