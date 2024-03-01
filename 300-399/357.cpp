#include <iostream>
#include <vector>

using namespace std;

typedef long long ll;

int main()
{
    int N = 1e8;
    vector<bool> p(N+1, 1), d(N+1, 1);
    p[0] = 0; p[1] = 0;
    for(int i=2; i<=N; i++)
        if(p[i])
            for(int j=2 * i; j<=N; j+=i)
                p[j] = 0;

    for(int i=1; i<=N; i++)
        for(int j = i; j <= N; j += i)
            if(!p[i + j / i])
                d[j] = 0;
    
    ll res = 0;
    for(ll i=0; i<=N; i++)
        if(d[i])
            res += i;
    cout<<res<<endl;
}