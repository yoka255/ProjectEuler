#include <iostream>
#include <vector>
#include <algorithm>
#include <fstream>

using namespace std;

vector<vector<int>> dp, mat;
int cnt = 0;

int calc(int k, int v)
{
    ++cnt;
    if(k == 15)
        return 0;
    if(dp[k][v] != -1)
        return dp[k][v];
    dp[k][v] = 0;
    for(int i=0; i<15; i++)
    {
        if(!((1<<i) & v))
            dp[k][v] = max(dp[k][v], calc(k + 1, (v | (1 << i))) + mat[k][i]);
    }
//    cout<<dp[k][v]<<endl;
    return dp[k][v];
}

int main()
{
    dp = vector<vector<int>>(15, vector<int>(1 << 15, -1));
    mat = vector<vector<int>>(15, vector<int>(15));
    ifstream fin("p345_matrix.txt");
    for(int i=0; i<15; i++)
    {
        for(int j=0; j<15; j++)
        {
            fin>>mat[i][j];
        }
    }
    
    cout<<calc(0, 0)<<endl;
    cout<<cnt<<endl;
}