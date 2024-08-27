# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def FindmaxPathSum(self, root: Optional[TreeNode], maxi: List[int]) -> int:
        if root is None:
            return 0

        leftsum = max(0, self.FindmaxPathSum(root.left, maxi))
        rightsum = max(0, self.FindmaxPathSum(root.right, maxi))


        maxi[0] = max(maxi[0], leftsum + rightsum + root.val)
        return root.val + max(leftsum, rightsum)
    
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maxi = [float('-inf')]
        self.FindmaxPathSum(root, maxi)
        return maxi[0]