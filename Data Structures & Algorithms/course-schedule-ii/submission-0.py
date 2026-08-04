class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        c={}
        for i in range(numCourses):
            c[i]=[]
        for course, req in prerequisites:
            c[course].append(req)
        
        seen=set()
        visited=set()
        output=[]

        def dfs(curr):
            if curr in seen:
                return False
            if curr in visited:
                return True
            
            seen.add(curr)

            for i in c[curr]:
                if not dfs(i):
                    return False
            seen.remove(curr)
            visited.add(curr)
            output.append(curr)
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return []
        return output