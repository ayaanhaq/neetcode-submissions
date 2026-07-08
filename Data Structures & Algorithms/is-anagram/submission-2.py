class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        c={}
        d={}
        for i in s:
            if i not in c:
                c[i]=0
            c[i]+=1
        for i in t:
            if i not in d:
                d[i]=0
            d[i]+=1
        return d==c
        