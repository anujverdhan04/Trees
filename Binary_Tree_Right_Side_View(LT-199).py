# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        '''
        result = []
        def dfs(node, level):
            if not node:
                return
            if level == len(result):
                result.append(node.val)
            dfs(node.right, level + 1)
            dfs(node.left, level + 1)
        
        dfs(root, 0)
        return result
       '''     
        result = []
        if not root:
            return result
        self._rightSideView(root, 0, result)
        return result
    
    def _rightSideView(self, node: Optional[TreeNode], level: int, result: List[int]):
        if not node:
            return
        # If visiting this level for the first time, add the node's value
        if level == len(result):
            result.append(node.val)
        # First traverse the right side, then the left side
        self._rightSideView(node.right, level + 1, result)
        self._rightSideView(node.left, level + 1, result)
    
    def leftSideView(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        if not root:
            return result
        self._leftSideView(root, 0, result)
        return result
    
    def _leftSideView(self, node: Optional[TreeNode], level: int, result: List[int]):
        if not node:
            return
        # If visiting this level for the first time, add the node's value
        if level == len(result):
            result.append(node.val)
        # First traverse the left side, then the right side
        self._leftSideView(node.left, level + 1, result)
        self._leftSideView(node.right, level + 1, result)
