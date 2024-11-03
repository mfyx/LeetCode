#
# @lc app=leetcode.cn id=35 lang=python3
#
# [35] 搜索插入位置
#

# @lc code=start
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        i = 0
        for i in range(len(nums)):
            if nums[i] >= target:
                break
        
        if i == len(nums) - 1 and nums[-1] < target:
            return len(nums)
        return i

        
# @lc code=end

