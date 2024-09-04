# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:

        min_value = root.val
        self.second_min = None

        def dfs(node):
            if not node:
                return

            # If the node's value is greater than the minimum and less than the current second minimum, update it
            if min_value < node.val and (self.second_min is None or node.val < self.second_min):
                self.second_min = node.val

            # Continue DFS traversal
            dfs(node.left)
            dfs(node.right)

        dfs(root)

        # Return the second minimum value if it was updated, otherwise return -1
        return self.second_min if self.second_min is not None else -1