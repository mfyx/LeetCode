#
# @lc app=leetcode.cn id=87 lang=python3
#
# [87] 扰乱字符串
#

# @lc code=start
class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        if s1 == s2:
            return True
        
        if len(s1) != len(s2) or sorted(s1) != sorted(s2):
            return False
        
        n = len(s1)
        
        dp = [[[False]*(n+1) for _ in range(n)] for _ in range(n)]

        for i in range(n):
            for j in range(n):
                dp[i][j][1] = (s1[i] == s2[j])
        
        for length in range(2, n+1):
            for i in range(n - length + 1):
                for j in range(n - length + 1):
                    for k in range(1, length):
                        if dp[i][j][k] and dp[i+k][j+k][length-k]:
                            dp[i][j][length] = True
                            break
                        if dp[i+k][j][length-k] and dp[i][j+length-k][k]:
                            dp[i][j][length] = True
                            break
        
        return dp[0][0][n]


        
# @lc code=end

