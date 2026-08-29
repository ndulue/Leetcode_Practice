class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        m = len(matrix[0])
        ansMatrix = [[0]*(m + 1) for _ in range(n+1)]
        count = 0
        
        for row in range(1, n+1):
            for col in range(1, m+1):
                if matrix[row - 1][col - 1] == 1:
                    ansMatrix[row][col] = min(ansMatrix[row-1][col-1], ansMatrix[row][col-1], ansMatrix[row-1][col])
                    count += ansMatrix[row][col]
                    print(count)
        
        return count
        
        
        