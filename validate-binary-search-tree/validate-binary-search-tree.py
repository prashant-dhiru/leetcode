from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(node, left, right):
            if not node:
                return True
            
            if left < node.val and node.val< right:
                return dfs(node.left, left, node.val) and \
                dfs(node.right, node.val, right)
            else:
                return False

        return dfs(root, float("-inf"), float("inf"))