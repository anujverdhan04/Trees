# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        def helper(node,current_sum):
            if not node:
                return 0
            current_sum = (current_sum << 1) | node.val

            if not node.left and not node.right:
                return current_sum

            return helper(node.left , current_sum) + helper(node.right,current_sum)
        return helper(root,0)    