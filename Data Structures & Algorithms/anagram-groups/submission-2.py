class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        c={}
        for i in strs:
            sort="".join(sorted(i))
            if sort not in c:
                c[sort]=[]
            c[sort].append(i)
        return list(c.values())
