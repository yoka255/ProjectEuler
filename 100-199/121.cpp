#include <iostream>
#include <vector>

using namespace std;

typedef long long ll;

struct frac
{
    ll a, b;
    frac()
    {
        a = 0; b = 0;
    }
    frac(ll a, ll b):a(a), b(b)
    {}
    frac operator+(frac x)
    {
        if(b != x.b)
        {
            cout<<"FUCK"<<endl;
        }
        return frac(a + x.a, b);
    }
    frac operator*(frac x)
    {
        return frac(a * x.a, b * x.b);
    }
};

int main()
{
    int n = 15;
    vector<vector<ll>> p(n + 1, vector<ll>(n+1));
    p[0][0] = 1;
    for(ll i=1; i<=n; i++)
    {
        p[i][0] = p[i-1][0] * i;
        for(int j=1; j<=i; j++)
        {
            p[i][j] = p[i-1][j-1] + p[i-1][j] * i;
        }
    }
    ll res = 0;
    for(int i=0; i<=n; i++)
        if(i > n-i)
            res += p[n][i];
    cout<<res<<endl;
    ll fact = 1;
    for(int i=1; i<=n+1; i++)
        fact *= i;
    cout << fact / res << endl;
}