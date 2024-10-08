# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        def traverse (node):
            if node:
                result.append(node.val)       # Visit the root
                traverse(node.left)           # Traverse the left subtree
                traverse(node.right)          # Traverse the right subtree
        
        traverse(root)
        return result
        