#
# @lc app=leetcode.cn id=20 lang=python3
#
# [20] 有效的括号
#

# @lc code=start
from collections import deque

class Solution:
    def isValid(self, s: str) -> bool:
        if s == "":
            return True
        if len(s) % 2 == 1:
            return False

        stk = deque()

        for i in s:
            if i == '(' or i == '[' or i == '{':
                stk.append(i)
                continue
            if len(stk) == 0:
                return False
            t = stk.pop()
            if (t == '(' and i != ')') or (t == '[' and i != ']') or (t == '{' and i != '}'):
                return False
        
        if not stk:
            return True
        return False


        
# @lc code=end

