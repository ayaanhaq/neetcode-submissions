class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        maps={
            ')':"(",
            '}':'{',
            "]":"["
        }

        for i in s:
            if i in '[{(':
                stack.append(i)
            elif i in '}])':
                if not stack:
                    return False
                elif stack[-1]==maps[i]:
                    stack.pop()
                else:
                    return False
        return len(stack)==0