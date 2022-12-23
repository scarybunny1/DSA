class Solution:
    def calculate(self, day, buy_decision, prices, memo):
        if day >= len(prices):
            return 0
        
        if (day, buy_decision) in memo:
            return memo[(day, buy_decision)]
        
        if buy_decision:
            buy = -prices[day] + self.calculate(day+1, 0, prices, memo)
            dont_buy = self.calculate(day+1, 1, prices, memo)
            memo[(day, buy_decision)] = max(buy, dont_buy)
        else:
            sell = prices[day] + self.calculate(day+2, 1, prices, memo)
            dont_sell = self.calculate(day+1, 0, prices, memo)
            memo[(day, buy_decision)] = max(sell, dont_sell)
            
        return memo[(day, buy_decision)]
        
    def maxProfit(self, prices: List[int]) -> int:
        memo = {}
        return self.calculate(0, 1, prices, memo)