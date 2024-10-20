#
# @lc app=leetcode.cn id=14 lang=python3
#
# [14] 最长公共前缀
#

# @lc code=start
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        prefix = min(strs)
        for s in strs:
            while not s.startswith(prefix):
                prefix = prefix[:-1]
        return prefix

        
# @lc code=end

