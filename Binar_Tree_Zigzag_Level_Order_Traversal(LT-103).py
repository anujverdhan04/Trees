# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []

        if not root:
            return result

        nodedata = deque()
        nodedata.append(root)

        LtoR = True
        while nodedata:
            n = len(nodedata)
            row = [0] * n
            for i in range(n):
                # Get the front node from the queue
                node = nodedata.popleft()
                
                # Determine the index to insert the node's value based on the traversal direction
                index = i if LtoR else (n - 1 - i)
                
                # Insert the node's value at the determined index
                row[index] = node.val
                
                # Enqueue the left and right children if they exist
                if node.left:
                    nodedata.append(node.left)
                if node.right:
                    nodedata.append(node.right)
            
            # Switch the traversal direction for the next level
            LtoR = not LtoR
            
            # Add the current level's values to the result list
            result.append(row)
        
        # Return the final result of zigzag level order traversal
        return result