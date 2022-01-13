"""
121. Best Time to Buy and Sell Stock

You are given an array prices where prices[i] is the price
of a given stock on the ith day.

You want to maximize your profit by choosing a single day 
to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. 
If you cannot achieve any profit, return 0.
"""

from typing import List


class Solution:
    # Time: o(n)
    # Space: o(1)
    def maxProfit(self, prices: List[int]) -> int:
        """
            We loop over the array in one pass,
            we update the minimum each time we found one,
            and update the profit each time we fine a higher profit
        """
        minimum = prices[0]

        profit = 0

        for price in prices:
            if price < minimum:
                minimum = price

            current_profit = price - minimum
            if current_profit > profit:
                profit = current_profit

        return profit


s = Solution()
test1 = s.maxProfit([7, 1, 5, 3, 6, 4])
test2 = s.maxProfit([7, 6, 4, 3, 1])

assert test1 == 5
assert test2 == 0
