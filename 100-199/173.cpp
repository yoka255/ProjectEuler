#include <iostream>
#include <vector>

using namespace std;

typedef long long ll;

int main()
{
    ll res = 0;
    ll t = 1000000;
    for(ll a = 1; 4 * a  - 4 <= t; a++)
    {
        
        ll l = 1, r = a - 1;
        while(l < r)
        {
            ll m = (l+r) / 2;
            if(a * a - m * m <= t)
                r = m;
            else
                l = m+1;
        }
        
        l += (a + l) % 2;
        // cout<<a<<":"<<(a - l) / 2<< endl;
        res += (a - l) / 2;
    }
    cout<<res<<endl;
}
