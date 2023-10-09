class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashmap = collections.defaultdict(int)
        hashmap[''] = 0
        for i in range(len(s)):
            key_str = self.nonDupString(i, s)
            hashmap[key_str] = len(key_str)
        print(hashmap)
        return max(hashmap.values())
    
    def nonDupString(self, idx: int, s:str) -> str:
        check = s[idx]
        for j in s[idx+1:]:
            if j in check:
                return check
            else:
                check += j
        return check
