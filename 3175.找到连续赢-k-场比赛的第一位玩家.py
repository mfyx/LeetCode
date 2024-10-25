#
# @lc app=leetcode.cn id=3175 lang=python3
#
# [3175] 找到连续赢 K 场比赛的第一位玩家
#

# @lc code=start
from collections import deque, defaultdict

class Solution:
    def findWinningPlayer(self, skills: List[int], k: int) -> int:
        dq = deque(skills)
        mp = defaultdict(int)
        winner = -1
        for i in range(len(skills)):
            mp[skills[i]] = i
            winner = max(skills[i], winner)

        a = dq.popleft()
        
        cnt = 0
        now = a

        while cnt < k:
            b = dq.popleft()
            if a > b:
                dq.append(b)
                cnt += 1
                # now = a
            else:
                dq.append(a)
                a = b
                cnt = 1
                now = b
            
            if a == winner:
                return mp[winner]
        
        return mp[now]
        
# @lc code=end

