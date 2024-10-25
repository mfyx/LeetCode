#
# @lc app=leetcode.cn id=22 lang=python3
#
# [22] 括号生成
#

# @lc code=start
class Solution:
    def backtrack(self, left_num: int, right_num: int, path: str):
        if len(path) == 2 * self.size:
            self.ret.append(path)
            return
        
        if left_num < self.size:
            path += '('
            left_num += 1
            self.backtrack(left_num, right_num, path)

            path = path[:-1]
            left_num -= 1
        
        if right_num < left_num:
            path += ')'
            right_num += 1
            self.backtrack(left_num, right_num, path)

            path = path[:-1]
            right_num -= 1

    def generateParenthesis(self, n: int) -> List[str]:
        self.size = n
        self.ret = []

        self.backtrack(0, 0, "")

        return self.ret

        
# @lc code=end

