class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        row=len(grid)
        col=len(grid[0])
            
        DP=grid
        
        for i in range(row):
            for j in range(col):
                if i==0 and j!=0:
                    DP[i][j]+=DP[i][j-1]
                if i!=0 and j==0:
                    DP[i][j]+=DP[i-1][j]
                if i!=0 and j!=0:
                    if DP[i-1][j]<DP[i][j-1]:
                        DP[i][j]+=DP[i-1][j]
                    else:
                        DP[i][j]+=DP[i][j-1]
                        
        return DP[row-1][col-1]
