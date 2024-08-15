# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
      
        ans = []
        if not root:
            return ans

        q = deque()
        q.append(root)

        while q:
            size = len(q)
            level = []

            for i in range(size):
                # Get the front node in the queue
                node = q.popleft()
                level.append(node.val)

                # Enqueue the child nodes if they exist
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            ans.append(level)
        return ans