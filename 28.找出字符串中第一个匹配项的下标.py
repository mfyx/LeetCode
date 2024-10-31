#
# @lc app=leetcode.cn id=28 lang=python3
#
# [28] 找出字符串中第一个匹配项的下标
#

# @lc code=start
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        len1 = len(haystack)
        len2 = len(needle)
        for i in range(len1):
            if haystack[i] == needle[0] and i + len2 <= len1:
                if haystack[i : i + len2] == needle[:]:
                    return i
                else:
                    i += len2
        
        return -1

        
# @lc code=end

