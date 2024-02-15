import heapq

class Solution:
    def nthUglyNumber(self, n: int) -> int:
        ugly_num = []
        heapq.heappush(ugly_num, 1)
        
        L1, L2, L3 = 0, 0, 0
        while len(ugly_num) < n:
            tmp = min(ugly_num[L1]*2, ugly_num[L2]*3, ugly_num[L3]*5)
            heapq.heappush(ugly_num, tmp)
            
            if tmp == ugly_num[L1]*2:
                L1 += 1
            if tmp == ugly_num[L2]*3:
                L2 += 1
            if tmp == ugly_num[L3]*5:
                L3 += 1
                
        return ugly_num[-1]