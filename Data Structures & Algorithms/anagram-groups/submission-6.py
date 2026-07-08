class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        c=defaultdict(list)
        for i in strs:
            count=[0]*26
            for j in i:
                count[ord(j)-ord("a")]+=1

            c[tuple(count)].append(i)
        return list(c.values())