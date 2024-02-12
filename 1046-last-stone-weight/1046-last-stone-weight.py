class Solution:
    import heapq
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        # 최대힙 생성
        for stone in stones:
            heapq.heappush(heap, -stone)
        
        # 게임 진행
        while len(heap) > 1:
            x = heapq.heappop(heap)
            y = heapq.heappop(heap)
            
            if x==y:
                continue
            else:
                heapq.heappush(heap, x-y)
        
        try:
            return (-1)*heapq.heappop(heap)
        except:
            return 0