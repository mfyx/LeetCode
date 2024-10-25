#
# @lc app=leetcode.cn id=3180 lang=python3
#
# [3180] 执行操作可获得的最大总奖励 I
#

# @lc code=start
class Solution:
    def maxTotalReward(self, rewardValues: List[int]) -> int:
        rewardValues.sort()

        dp = [False] * (sum(rewardValues) + 1)
        dp[0] = True

        maxReward = 0

        for i in rewardValues:
            dp[i] = True
            for j in range(0, i):
                if dp[j]:
                    dp[i+j] = True
                    maxReward = max(i+j, maxReward)
        
        return maxReward
        

                    
        
# @lc code=end

