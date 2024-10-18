#
# @lc app=leetcode.cn id=70 lang=python3
#
# [70] 爬楼梯
#

# @lc code=start
class Solution:
    def climbStairs(self, n: int) -> int:
        ret = [1, 1]
        while len(ret) < n+1:
            ret.append(ret[-1] + ret[-2])
        return ret[-1]
        
# @lc code=end

