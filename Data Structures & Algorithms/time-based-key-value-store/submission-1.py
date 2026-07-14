class TimeMap:

    def __init__(self):
       self.timemap={}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.timemap:
            self.timemap[key]=[]
        self.timemap[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.timemap:
            return ""
        arr=self.timemap[key]
        left=0
        right=len(arr)-1
        answer=""

        while left<=right:
            mid=(left+right)//2

            if arr[mid][1]<=timestamp:
                answer=arr[mid][0]
                left=mid+1
            else:
                right=mid-1
        return answer
    

