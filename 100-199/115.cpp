#include <iostream>
#include <vector>

using namespace std;

typedef long long ll;

int main()
{
    int N = 300, M = 50;
    vector<ll> dp(N+1, 0);
    dp[0] = 1;
    for(int i=1; i<=N; i++)
    {
        dp[i] = dp[i-1];
        if(i >= M)
            dp[i] += 1;
        for(int j=0; j<i - M; j++)
            dp[i] += dp[j];
        if(dp[i] > 1e6)
        {
            cout<<i<<endl;
            return 0;
        }
    }
    for(int i=0; i<N; i++)
        cout<<dp[i]<<" ";
    
    cout<<dp[N]<<endl;
}