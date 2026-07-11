class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        data=[]
        for i in range(len(position)):
            data.append([position[i],speed[i]])

        data=sorted(data, reverse=True)
        print(data)
        stack=[]
        for pos,sp in data:
            t=(target-pos)/sp
            stack.append(t)
            if len(stack)>=2 and stack[-1]<=stack[-2]:
                stack.pop()
        return len(stack)