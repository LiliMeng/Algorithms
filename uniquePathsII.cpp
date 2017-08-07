#include <iostream>
#include <vector>

using namespace std;

class Solution{
public:
    int uniquePathsWithObstacles(vector<vector<int>>& obstacleGrid)
    {

        int line = obstacleGrid.size();

        int col  = obstacleGrid[0].size();

        int DP[line][col];
        if(obstacleGrid[0][0]==0)
        {
            DP[0][0]=1;
        }
        else
        {
            DP[0][0]=0;
        }


        for(int i = 0; i<line; i++)
        {
            for (int j=0; j<col; j++)
            {
                if(obstacleGrid[i][j]==0)
                {
                    if(i==0&j!=0)
                    {
                        DP[i][j]=DP[i][j-1];
                    }
                    if(i!=0&j==0)
                    {
                        DP[i][j]=DP[i-1][j];
                    }

                    if(i!=0&j!=0)
                    {
                        DP[i][j]=DP[i-1][j]+DP[i][j-1];
                    }
                }
                else
                {
                    DP[i][j]=0;
                }

            }
        }

        return DP[line-1][col-1];
    }
};

int main()
{
    vector<vector<int>> obstacleGrid={{0,0}};

    Solution s;

    cout<<s.uniquePathsWithObstacles(obstacleGrid)<<endl;
}
