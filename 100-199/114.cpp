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
        for(int j=0; j<i - 3; j++)
            dp[i] += dp[j];
    }
    for(int i=0; i<N; i++)
        cout<<dp[i]<<" ";
    
    cout<<dp[N]<<endl;
}