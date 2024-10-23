#
# @lc app=leetcode.cn id=1143 lang=python3
#
# [1143] 最长公共子序列
#

# @lc code=start
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        len1 = len(text1)
        len2 = len(text2)
        dp = [[0] * len2 for _ in range(len1)]

        dp[0][0] = int(text1[0] == text2[0])

        for i in range(1, len1):
            if text1[i] == text2[0]:
                dp[i][0] = 1
            else:
                dp[i][0] = max(dp[i-1][0], 0)
        
        for j in range(1, len2):
            if text1[0] == text2[j]:
                dp[0][j] = 1
            else:
                dp[0][j] = max(dp[0][j-1], 0)
        
        for j in range(1, len2):
            for i in range(1, len1):
                if text1[i] == text2[j]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i][j-1], dp[i-1][j])
        
        return dp[len1-1][len2-1]
        
# @lc code=end

