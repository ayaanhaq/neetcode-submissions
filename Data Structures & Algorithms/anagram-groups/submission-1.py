class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        l={}
        for i in strs:
            sort="".join(sorted(i))
            if sort not in l:
                l[sort]=[]
            l[sort].append(i)
        return list(l.values())