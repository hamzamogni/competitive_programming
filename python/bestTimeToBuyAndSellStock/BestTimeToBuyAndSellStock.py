# Source : https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
# Author : Hamza Mogni
# Date   : 2022-01-20

#####################################################################################################
#
# You are given an array prices where prices[i] is the price of a given stock on the i^th day.
#
# You want to maximize your profit by choosing a single day to buy one stock and choosing a different
# day in the future to sell that stock.
#
# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit,
# return 0.
#
# Example 1:
#
# Input: prices = [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
# Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
#
# Example 2:
#
# Input: prices = [7,6,4,3,1]
# Output: 0
# Explanation: In this case, no transactions are done and the max profit = 0.
#
# Constraints:
#
# 	1 <= prices.length <= 10^5
# 	0 <= prices[i] <= 10^4
#####################################################################################################

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
