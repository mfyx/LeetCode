#
# @lc app=leetcode.cn id=337 lang=python3
#
# [337] 打家劫舍 III
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import defaultdict

class Solution:
    f = defaultdict(int)
    g = defaultdict(int)

    def dfs(self, node) -> int :
        if not node:
            return 0
        
        self.dfs(node.left)
        self.dfs(node.right)

        self.f[node] = node.val + self.g[node.left] + self.g[node.right]
        self.g[node] = max(self.f[node.left], self.g[node.left]) + max(self.f[node.right], self.g[node.right])

        return max(self.f[node], self.g[node])

    def rob(self, root: Optional[TreeNode]) -> int:
        ret = self.dfs(root)
        return ret



        
# @lc code=end

