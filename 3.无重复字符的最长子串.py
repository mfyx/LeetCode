#
# @lc app=leetcode.cn id=3 lang=python3
#
# [3] 无重复字符的最长子串
#

# @lc code=start
from collections import deque

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dq = deque()
        win = set()
        for i in s:
            if i in win:
                break
            win.add(i)
            dq.append(i)
        
        #length = len(dq)
        maxlen = len(dq)

        for i in range(len(dq), len(s)):
            # if s[i] in  win:
            #     win.remove(s[i])
            while s[i] in dq:
                dq.popleft()
            dq.append(s[i])
            maxlen = max(len(dq), maxlen)
        
        return maxlen
            






        
# @lc code=end

