class Solution:
    def longestPalindrome(self, s: str) -> str:
        answer = ''
        for i in range(len(s)):
            for j in range(i, len(s)):
                tmp = s[i:j+1]
                if tmp == tmp[::-1] and len(answer) < len(tmp):
                    answer = tmp
        return answer
                    
