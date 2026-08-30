class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        self.maximum = float('-inf')
        
        def dfs(root) -> int:
            if root is None:
                return 0
            
            left_root = max(0, dfs(root.left))
            right_root = max(0, dfs(root.right))
            
            self.maximum = max(self.maximum, left_root + right_root + root.val)
            
            return max(left_root, right_root) + root.val
        
        dfs(root)
        return self.maximum