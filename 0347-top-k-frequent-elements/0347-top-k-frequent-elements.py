class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = collections.defaultdict(int)
        for num in nums:
            hashmap[num] += 1
        
        # hashmap의 value를 기준으로 정렬
        sorted_hashmap = sorted(hashmap.items(), key=lambda x: x[1], reverse=True)
        return [k[0] for k in sorted_hashmap[:k]]
        
        
        