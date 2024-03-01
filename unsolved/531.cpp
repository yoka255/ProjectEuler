#include <iostream>
#include <vector>

using namespace std;

typedef long long ll;

ll modPow(ll a, ll b, ll mod)
{
	ll res = 1;
	while (b > 0)
	{
		if (b & 1)
			res = (a * res) % mod;
		b >>= 1;
		a = (a * a) % mod;
	}
	return res;
}

ll gcd(ll a, ll b)
{
    if(b > a)
        return gcd(b,a);
    if(b == 0)
        return a;
    return gcd(b, a%b);
}

int main()
{
    ll N = 1005000;
    vector<ll> phi(N);
    for(int i=2; i<N; i++)
        phi[i] = i;
    for(ll i=2; i<N; i++)
    {
        if(phi[i] == i)
            for(ll j=i; j<N; j+=i){
                phi[j] = (phi[j] / i) * (i-1);
            }
    }
    ll res = 0;
    for(ll n = 1000000; n<N; n++)
    {
        for(ll m=n+1; m<N; m++)
        {
            if((phi[n] - phi[m]) % gcd(m,n) == 0)
            {
                ll a = n;
                ll b = m/gcd(m,n);
                ll x = modPow(b, phi[a]-1, a) * phi[n];
                ll y = modPow(a, phi[b]-1, b) * phi[m];
                ll f = (b * x + a * y) % (m * n / gcd(m,n));
                // cout<<m<<":"<<phi[m]<<", "<<n<<":"<<phi[n]<<": "<<f;
                if(f % n == phi[n] && f % m == phi[m]){
                    res += f;
   //                 cout<<"  YES";
                }
 //               cout<<endl;
            }
        }
    }
    cout<<res<<endl;
}