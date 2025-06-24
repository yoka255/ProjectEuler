#include <iostream>

using namespace std;

typedef long long ll;

ll factorial_padic(ll n, ll p)
{
    ll p_pow = p;
    ll res = 0;
    while (p_pow < n)
    {
        res += n / p_pow;
        p_pow *= p;
    }
    return res;
}

int main()
{
    ll res = 1, mod = 1e5, N = 1e12;
    // N = 20;
    ll padic_2 = factorial_padic(N, 5);

    for (ll i = 1; i <= N; i++)
    {
        if (i % (ll)(1e8) == 0)
        {
            cout << i / (ll)1e8 << endl;
        }
        ll j = i;
        while (j % 5 == 0)
            j /= 5;
        while (j % 2 == 0 && padic_2)
        {
            j /= 2;
            padic_2--;
        }
        res = (res * j) % mod;
    }
    cout<<res<<endl;
}