#
# @lc app=leetcode.cn id=66 lang=python3
#
# [66] 加一
#

# @lc code=start
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        length = len(digits)
        carry = 1
        i = length - 1

        while i >= 0 and carry:
            carry = (digits[i] + 1) // 10
            digits[i] = (digits[i] + 1) % 10
            i -= 1

        if carry:
            # digits.insert(0, 1)
            digits = [1] + digits
        
        return digits

        
# @lc code=end

