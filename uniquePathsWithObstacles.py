class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        row = len(obstacleGrid)
        col = len(obstacleGrid[0])
        
        DP = [[0 for i in range(col)] for j in range(row)]
        
        if obstacleGrid[0][0]==0:
            DP[0][0]=1
        else:
            DP[0][0]=0
   
        
        for i in range(row):
            for j in range(col):
                if(obstacleGrid[i][j]==0):
                    if i==0 and j!=0:
                        DP[i][j]=DP[i][j-1]
                    if i!=0 and j==0:
                        DP[i][j]=DP[i-1][j]
                    if i!=0 and j!=0:
                        DP[i][j]=DP[i-1][j]+DP[i][j-1]
                else:
                    DP[i][j]=0
                    
        return DP[row-1][col-1]
