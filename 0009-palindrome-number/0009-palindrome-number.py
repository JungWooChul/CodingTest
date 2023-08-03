class Solution:
    def isPalindrome(self, x: int) -> bool:
        num_lst = list(str(x))
        return True if num_lst == num_lst[::-1] else False