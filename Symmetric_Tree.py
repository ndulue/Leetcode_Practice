class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if root is None:
            return True
        
        return self.isMirror(root.left, root.right)
    
    
    def isMirror(self, Lroot: TreeNode, Rroot: TreeNode) -> bool:
        if Lroot and Rroot:
            return Lroot.val == Rroot.val and self.isMirror(Lroot.right, Rroot.right) and self.isMirror(Lroot.left, Rroot.left)
        
        return Lroot == Rroot