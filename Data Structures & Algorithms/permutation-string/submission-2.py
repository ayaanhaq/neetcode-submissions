class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False
        
        count=[0]*26
        for i in s1:
            count[ord(i)-ord("a")]+=1
        for i in range(len(s2)-len(s1)+1):
            count2=[0]*26
            for j in s2[i:i+len(s1)]:
                count2[ord(j)-ord("a")]+=1
            if count2==count:
                return True
        return False