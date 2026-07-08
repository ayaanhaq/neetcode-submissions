class Solution:
    def isPalindrome(self, s: str) -> bool:
        k=""
        for i in s:
            if i.isalnum():
                k+=i.lower()
        return k==k[::-1]