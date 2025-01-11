# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        ans = defaultdict(list)
        queue = list()
        queue.append((1,root))

        while(queue):
            level, curr = queue.pop(0)
            if curr.left: queue.append((level+1, curr.left))
            if curr.right: queue.append((level+1, curr.right))
            ans[level].append(curr.val)

        return list(ans.values())