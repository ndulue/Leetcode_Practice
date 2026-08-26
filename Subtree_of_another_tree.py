class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        if s is None and t is None:
            return True
        
        if t is None:
            return True
        
        if s is None and t is not None:
            return False
        
        return self.isSame(s, t) and self.isSubtree(s.left, t.left) and self.isSubtree(s.right, t.right)
        
        
    def isSame(self, s, t):
        if s is None and t is None:
            return True
        
        if s is None or t is None:
            return False
        
        return s.val == t.val and self.isSame(s.left, t.left) and self.isSame(s.right, t.left)