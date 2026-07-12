class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars=[]
        for i in range(len(position)):
            cars.append((position[i],speed[i]))
        

        cars=sorted(cars,reverse=True)
        print(cars)
        stack=[]
        for pos, sp in cars:
            t=(target-pos)/sp
            stack.append(t)
            if len(stack)>=2 and stack[-1]<=stack[-2]:
                stack.pop()
        return len(stack)