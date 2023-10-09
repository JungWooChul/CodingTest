class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        
        hashmap = self.hashmap_set(jewels)
        return self.find_jewel(hashmap, stones)
        
    def hashmap_set(self, jewels: str) -> dict:
        hashmap = collections.defaultdict(int)
        
        # hashmap 키 설정
        for jewel in jewels:
            hashmap[jewel]
        
        return hashmap
    
    def find_jewel(self, hashmap:dict, stones: str) -> int:
        cnt = 0
        for i in stones:
            if i in hashmap.keys():
                cnt += 1
        return cnt