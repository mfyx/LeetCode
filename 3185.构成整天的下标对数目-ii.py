#
# @lc app=leetcode.cn id=3185 lang=python3
#
# [3185] 构成整天的下标对数目 II
#

# @lc code=start
class Solution:
    def countCompleteDayPairs(self, hours: List[int]) -> int:
        ran = 24
        cnt = [0] * (ran + 1)
        cnt[ran-(hours[0] % ran)] += 1

        ans = 0
        for i in range(1, len(hours)):
            if hours[i] % 24 == 0:
                ans += cnt[ran]
                # print(i, hours[i])
            elif cnt[hours[i] % ran]:
                ans += cnt[hours[i] % ran]
                # print(i, hours[i])
            cnt[ran-(hours[i] % ran)] += 1
        
        return ans

        
# @lc code=end

