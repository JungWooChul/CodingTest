class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        min_point = prices[0]
        for i in range(len(prices)-1):
            # 하한가보다 큰 값이라면 건너뛰기
            if min_point < prices[i] or prices[i-1] == prices[i]:
                continue
                
            tmp_prices = max(set(prices[i+1:]))
            if profit < tmp_prices - prices[i]:
                profit = tmp_prices - prices[i]
                # 하한가 초기화
                min_point = prices[i]
        return profit