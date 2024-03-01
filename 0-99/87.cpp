#include <iostream>
#include <vector>

using namespace std;

typedef long long ll;
typedef vector<ll> vi;

int main()
{
    ll N = 1e4, M = 5e7;
    vi p(N, 1), cnt(M+1, 0);
    p[0] = 0, p[1] = 0;
    for(int k=2; k<N; k++)
        if(p[k])
            for(int j = 2*k; j<N; j+=k)
                p[j] = 0;
    
    vi primes;
    for(ll k=0; k<N; k++)
        if(p[k])
            primes.push_back(k);
    
    for(ll a:primes)
    {
        if(a * a < M)
            for(ll b:primes)
            {
                if(a*a + b*b*b < M)
                    for(ll c:primes)
                    {
                        if(a*a + b*b*b + c*c*c*c > M)
                            break;
                        cnt[a*a + b*b*b + c*c*c*c] = 1;
                    }
            }
    }
    int res = 0;
    for(int c:cnt)
        res += c;
    cout<<res<<endl;
    
}