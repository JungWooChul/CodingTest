class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        answer = [i[0] for i in collections.Counter(nums).most_common(k)]
        return answer
        
        
        