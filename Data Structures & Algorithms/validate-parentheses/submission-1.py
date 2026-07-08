class Solution:
    def isValid(self, s: str) -> bool:
        valid = {")":"(","}":"{","]":"["}
        stack=[]
        for i in s:
            if i in "({[":
                stack.append(i)
            elif i in "}])":
                if len(stack)<1:
                    return False
                elif valid[i]==stack[-1]:
                    stack.pop()
                else:
                    return False
        if len(stack)==0:
            return True
        return False
