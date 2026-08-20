import heapq
class MedianFinder:

    def __init__(self):
        self.lowerhalf=[]
        self.upperhalf=[]

    def addNum(self, num: int) -> None:
        heapq.heappush(self.lowerhalf, -num)
        heapq.heappush(self.upperhalf, -heapq.heappop(self.lowerhalf))

        if len(self.upperhalf)>len(self.lowerhalf):
            heapq.heappush(self.lowerhalf, -heapq.heappop(self.upperhalf))

    def findMedian(self) -> float:
        
        if len(self.lowerhalf)>len(self.upperhalf):
            return -self.lowerhalf[0]
        return (-self.lowerhalf[0]+self.upperhalf[0])/2.0