#
# @lc app=leetcode.cn id=118 lang=python3
#
# [118] 杨辉三角
#

# @lc code=start
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0:
            return []
        elif numRows == 1:
            return [[1]]
        elif numRows == 2:
            return [[1], [1, 1]]

        ret = []
        ret.append([1])
        ret.append([1, 1])

        while(len(ret) < numRows):
            pre = ret[-1]
            now = [1]
            for i in range(1, len(pre)):
                now.append(pre[i - 1] + pre[i])
            now.append(1)
            ret.append(now)
        
        return ret

        
# @lc code=end

