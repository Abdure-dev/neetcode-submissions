class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0

        #iterate through the list
        #if the value of the ith the day is greater than hte ith - 1

        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]:
                max_profit += prices[i] - prices[i-1]
        return max_profit




        