#
# @lc app=leetcode.cn id=84 lang=python3
#
# [84] 柱状图中最大的矩形
#

# @lc code=start

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        if len(heights) == 0:
            return 0

        heights.append(0)

        stk = deque()
        max_area = 0
        
        for i in range(len(heights)):
            while len(stk) and heights[stk[-1]] > heights[i]:
                h = heights[stk.pop()]
                w = i if not stk else i - stk[-1] - 1
                area = h * w
                max_area = max(area, max_area)
            stk.append(i)
        
        return max_area
        
# @lc code=end

