class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        c={}
        maxLen=0
        left=0

        for right in range(len(s)):
            if s[right] not in c:
                c[s[right]]=0
            c[s[right]]+=1

            if (right-left+1)-(max(c.values()))>k:
                c[s[left]]-=1
                left+=1
            maxLen=max(maxLen, right-left+1)
        return maxLen
        