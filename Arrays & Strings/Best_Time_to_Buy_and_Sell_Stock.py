#Best_Time_to_Buy_and_Sell_Stock - You are given an array prices where prices[i] is the price of a given stock on the ith day.
#You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
#Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
#link - https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')
        max_profit = 0

        for price in prices:
            if price < min_price:
                min_price = price # defining what is the min price in the list

            profit = price - min_price # calculating profit on every number in list starting from when we bought

            if profit > max_profit: # checking which profit is the largest one
                max_profit = profit

        return max_profit