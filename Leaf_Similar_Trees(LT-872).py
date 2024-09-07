# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        
        def dfs(node , arr):
            if not node:
                return
            if node.left is None and node.right is None:
                arr.append(node.val)
            else:
                dfs(node.left , arr)
                dfs(node.right,arr)
        arr1=[]
        arr2=[]
        dfs(root1,arr1)
        dfs(root2,arr2)        
        return arr1==arr2
        