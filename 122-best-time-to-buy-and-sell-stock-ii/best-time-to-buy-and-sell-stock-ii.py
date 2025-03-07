class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        is_buying = True
        profit = 0

        for price_indx in range(1, len(prices)):

            if is_buying and prices[price_indx - 1] < prices[price_indx]:
                profit -= prices[price_indx - 1]
                is_buying = not is_buying
            elif not is_buying and prices[price_indx - 1] > prices[price_indx]:
                profit += prices[price_indx - 1]
                is_buying = not is_buying

        if not is_buying and profit + prices[-1] > 0:
            profit += prices[-1]
        
        return profit

