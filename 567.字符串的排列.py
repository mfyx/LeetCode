#
# @lc app=leetcode.cn id=567 lang=python3
#
# [567] 字符串的排列
#

# @lc code=start

from collections import defaultdict

class Solution:
    def count_char(self, s: str) -> dict:
        return {char: s.count(char) for char in set(s)}

    def checkInclusion(self, s1: str, s2: str) -> bool:
        count_s1 = self.count_char(s1)

        s = s2[:len(s1)]
        count_s2 = self.count_char(s)
        if count_s1 == count_s2:
            return True
        
        for i in range(len(s1), len(s2)):
            count_s2[s2[i]] = count_s2.get(s2[i], 0) + 1
            count_s2[s2[i - len(s1)]] -= 1
            if count_s2[s2[i - len(s1)]] == 0:
                del count_s2[s2[i - len(s1)]]

            if count_s1 == count_s2:
                return True
        
        return False
        
# @lc code=end

