#include <iostream>
#include <vector>

using namespace std;

typedef long long ll;

ll pp(ll b, ll p, ll MOD){ // O(log(p))
    if (p==0) return 1;
    return pp(b*b%MOD, p/2, MOD) * (p%2?b:1) % MOD;
}

int main()
{
    ll n = 1e8;
    ll MOD = 1e6;
    vector<ll> c(n), t(n), d(n);
    c[0] = 1; c[1] = 1; c[2] = 1; c[3] = 2;
    for(ll i=4; i<n; i++)
        c[i] = (c[i-1] + c[i-2] + c[i-4])% MOD;
    vector<ll> csum(n+1);
    for(ll i=1; i<=n; i++)
        csum[i] = (csum[i-1] + c[i-1]) % MOD; 
    for(ll m=0; m<n; m++)
    {
        t[m] += pp(2, m/2, MOD);
        if(m != 0 && (m % 2 == 0))
        {
            t[m] += c[m/2 - 1];
        }
        t[m] = (t[m] - csum[m / 2 + 1]) % MOD;
    }
    for(ll i=0; i<n; i++)
    {
        if(t[i] % MOD == 0)
            cout<<i<<endl;
    }
}