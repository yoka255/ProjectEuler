#include <iostream>
#include <vector>

using namespace std;

typedef long long ll;

int MOD = 250;

ll pow(ll a, ll b)
{
    ll res = 1;
    while (b > 0)
    {
        if (b & 1)
            res = (a*res)%MOD;
        b >>= 1;
        a = (a*a)%MOD;
    }
    return res;
}

int main()
{
    int n = 250250;
    vector<ll> dp(MOD);
    dp[0] = 1;

    for(ll k=1; k<=n; k++)
    {
        int a = pow(k,k);
        vector<ll> cp(MOD);
        for(int i=0; i<MOD; i++)
            cp[i] = dp[i];
        for(int i=0; i<MOD; i++)
            cp[(i + a) % MOD] += dp[i];
        for(int i=0; i<MOD; i++)
            dp[i] = cp[i] % ((ll)1e16);
    }
    cout<<dp[0]<<endl;
}
