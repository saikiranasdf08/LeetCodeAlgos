'''
121. Best Time to Buy and Sell Stock
https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
'''

def maxProfit(self, prices):
    minval,profit=float('inf'),0
    for p in prices:
        minval=min(minval,p)
        profit=max(p-minval,profit)
    return profit