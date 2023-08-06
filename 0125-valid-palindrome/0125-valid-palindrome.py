class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_alp = [i.lower() for i in s if i.isalpha() or i.isdigit()]
        
        if s_alp == s_alp[::-1]:
            return True
        else:
            return False
        