class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        """
        # track low, high with pointers

        max_profit = 0
  
        lowest, highest = prices[0], prices[0]
        lidx, hidx, tidx = 0, 0, 0
        while tidx < len(prices):
            
            price = prices[tidx]

            if price < lowest:
                lowest = price
                highest = lowest
                lidx = tidx

            elif price > highest:
                highest = price
                hidx = tidx
                max_profit = max(max_profit, highest - lowest)

            tidx += 1
            

        return max_profit
            

                        