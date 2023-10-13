class Solution:
    def romanToInt(self, s: str) -> int:
        answer = self.symbolToValue(s[-1])
        for idx in range(len(s)-1):
            tmp = self.symbolToValue(s[idx])
            if self.symbolToValue(s[idx+1]) > tmp:
                tmp *= -1
            answer += tmp
        return answer
    
    def symbolToValue(self, s:str) -> int:
        roman = {
            'I' : 1,
            'V' : 5,
            'X' : 10,
            'L' : 50,
            'C' : 100,
            'D' : 500,
            'M' : 1000
        }
        return roman[s]