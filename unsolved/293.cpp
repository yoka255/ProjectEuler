#include <iostream>
#include <vector>
#include <set>

using namespace std;

typedef long long ll;

int main()
{
    ll N = 1e9;
    vector<ll> p(2 * N, 1);
    ll last = 1;
    for(ll i=2; i<2 * N; i++)
    {
        // cout<<i<<endl;
        if(p[i] == 1)
        {
            for(ll j=i; j<2 * N; j+=i)
            {
                if(p[j] != 1 && p[j] != last)
                    p[j] = -1;
                else
                    p[j] = i;
            }
            last = i;
        }
    }
    set<ll> res;
    for(ll n=2; n<N; n++)
    {
        cout<<n<<endl;
        if(p[n] != -1)
        {
            for(ll m=2; 1; m++){
                if(p[n+m] == n+m)
                {
                    res.insert(m);
                    break;
                }
            }
        }
    }
    long long num = 0;
    for(ll a:res)
        num += a;
    cout<<num<<endl;
}