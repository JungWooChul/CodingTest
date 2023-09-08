class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        brackets = {
            '(' : ')',
            '[' : ']',
            '{' : '}'
        }
        for i in s:
            if i in brackets.keys():
                stack.append(i)
            else:
                try:
                    if brackets[stack.pop()] == i:
                        continue
                    else:
                        return False
                except:
                    return False
                    
        if len(stack) == 0:
            return True
        else:
            return False
            