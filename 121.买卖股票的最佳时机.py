#
# @lc app=leetcode.cn id=121 lang=python3
#
# [121] 买卖股票的最佳时机
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        ans = 0
        for i in range(1, len(prices)):
            ans = max(prices[i] - min_price, ans)
            min_price = min(prices[i], min_price)
        
        return ans
        
# @lc code=end

