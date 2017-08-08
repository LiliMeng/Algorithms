#include <iostream>
#include <vector>

using namespace std;


class Solution{
public:
    int minPathSum(vector<vector<int>>& grid)
    {
        int row = grid.size();
        int col = grid[0].size();

        vector<vector<int>> DP=grid;
        for(int i=0; i<row; i++)
        {
            for(int j=0; j<col; j++)
            {
                if(i==0&j!=0)
                {
                    DP[i][j]+=DP[i][j-1];
                }
                if(i!=0 & j==0)
                {
                    DP[i][j]+=DP[i-1][j];
                }
                if(i!=0 & j!=0)
                {
                    if(DP[i-1][j]<DP[i][j-1])
                    {
                        DP[i][j]+=DP[i-1][j];
                    }
                    else
                    {
                        DP[i][j]+=DP[i][j-1];
                    }
                }
            }
        }

        return DP[row-1][col-1];

    }

};


int main()
{
    Solution s;
    vector<vector<int> > grid={{1,2,3},{1,2,3},{1,2,3}};
    cout<<s.minPathSum(grid)<<endl;
}
