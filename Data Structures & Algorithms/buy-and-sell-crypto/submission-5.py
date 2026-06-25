class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        """
        # track low, high with pointers

        max_profit = 0
  
        lowest, highest = prices[0], prices[0]
        tidx = 0
        while tidx < len(prices):
            
            price = prices[tidx]

            if price < lowest:
                lowest = price
                highest = lowest

            elif price > highest:
                highest = price
                max_profit = max(max_profit, highest - lowest)

            tidx += 1
            

        return max_profit
            

                        