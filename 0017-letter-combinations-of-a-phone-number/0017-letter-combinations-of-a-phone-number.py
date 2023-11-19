class Solution:
    def __init__(self):
        self.phone_number = {
            '2' : ['a', 'b', 'c'],
            '3' : ['d', 'e', 'f'],
            '4' : ['g', 'h', 'i'],
            '5' : ['j', 'k', 'l'],
            '6' : ['m', 'n', 'o'],
            '7' : ['p', 'q', 'r', 's'],
            '8' : ['t', 'u', 'v'],
            '9' : ['w', 'x', 'y', 'z']
        }
    def letterCombinations(self, digits: str) -> List[str]:
        answer = []
        for digit in digits:
            if len(answer):
                tmp = []
                for let in answer:
                    tmp.extend([let+alp for alp in self.phone_number[digit]])
                answer = tmp
            else:
                answer = self.phone_number[digit]
        return answer
                        
        