class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        c={}
        for i in range(numCourses):
            c[i]=[]
        
        for num, req in prerequisites:
            c[num].append(req)
        
        seen=set()

        def dfs(curr):
            if curr in seen:
                return False
            if c[curr]==[]:
                return True
            seen.add(curr)
            for req in c[curr]:
                if not dfs(req):
                    return False
            seen.remove(curr)
            c[curr]=[]
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True