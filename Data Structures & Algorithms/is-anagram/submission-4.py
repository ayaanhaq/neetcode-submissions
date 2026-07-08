class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        c={}
        d={}
        for i in s:
            if i not in c:
                c[i]=0
            c[i]+=1
        for j in t:
            if j not in d:
                d[j]=0
            d[j]+=1
        if c==d:
            return True
        else:
            return False