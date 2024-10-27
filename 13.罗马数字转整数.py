#
# @lc app=leetcode.cn id=13 lang=python3
#
# [13] 罗马数字转整数
#

# @lc code=start
class Solution:
    def romanToInt(self, s: str) -> int:
        mp = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
        }

        n = len(s)
        ans = 0

        for i, ch in enumerate(s):
            val = mp[ch]
            if i < n - 1 and mp[s[i]] < mp[s[i+1]]:
                ans -= val
            else:
                ans += val
        
        return ans

        
# @lc code=end

