class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        
        oldToNew = {}
         
        def dfs(node):
            if node in oldToNew:
                return oldToNew[node]
            
            copy = Node(node.val)
            oldToNew[node] = copy
            
            for neig in node.neighbors:
                copy.neighbours.append(dfs(neig))
            return copy
        
        return dfs(node) if node else None
             