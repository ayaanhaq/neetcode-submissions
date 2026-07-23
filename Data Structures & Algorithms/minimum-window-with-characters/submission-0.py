class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t=="":
            return ""
        
        count={}
        window={}

        for i in t:
            if i not in count:
                count[i]=0
            count[i]+=1

        have=0
        need=len(count)
        left=0
        minLen=float('infinity')
        result=[-1,-1]

        for right in range(len(s)):
            if s[right] not in window:
                window[s[right]]=0
            window[s[right]]+=1

            if s[right] in count and window[s[right]]==count[s[right]]:
                have+=1
            
            while have==need:
                if (right-left+1)<minLen:
                    minLen=right-left+1
                    result=[left,right]

                window[s[left]]-=1
                if s[left] in count and window[s[left]]<count[s[left]]:
                    have-=1
                left+=1
        left,right=result
        return s[left:right+1]