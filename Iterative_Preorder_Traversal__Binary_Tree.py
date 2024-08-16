class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        st = deque()

        if not root:
            return 
              
        st.append(root)   
        while st:
            node = st.pop()  # Pop the last element from the stack
            result.append(node.val)  # Add the node's value to the result list

            # Push right child first so that left child is processed first
            if node.right:
                st.append(node.right)
            if node.left:
                st.append(node.left)
        
        return result