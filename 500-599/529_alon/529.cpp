#include <iostream>
#include <vector>

using namespace std;

typedef vector<int> vi;
typedef vector<vi> vii;
typedef vector<vii> viii;

#define addmod(x, y, mod) x = (x + y) % mod

int main()
{
    int n = 18, k = 10;
    n = 3;
    int MOD = 1e9 + 7;
    viii dp(n + 1, vii(1 << k, vi(k)));

    for (int i = 1; i < k; i++)
    {
        dp[1][1 << i][i] = 1;
    }
    for (int d = 1; d < n; d++)
    { // amount of digits
        for (int l = 0; l < k; l++)
        { // next digit to choose
            for (int S = 0; S < 1 << k; S++)
            { // current open sums
                for (int j = 0; j < k; j++)
                { // max open sum
                    int next_sums = ((S | 1) << l ) & ((1 << k) - 1);
                    if((S & (1 << (k - l))) && j + l <= k){
                        addmod(dp[d+1][next_sums][0], dp[d][S][j], MOD);
                    }
                    else if(j + l < k){
                        addmod(dp[d+1][next_sums][j + l], dp[d][S][j], MOD);
                    }
                }
            }
        }
    }
    int res = 0;
    for(int d=1; d<=n; d++){
        for(int S = 0; S < (1 << k); S++){
            addmod(res,dp[d][S][0], MOD);
        }
    }
    cout<<res<<endl;
}