#include <iostream>
#include <tgmath.h>

using namespace std;

typedef long long ll;

int main()
{
    ll res = 0, N = 1e9;
    for(ll a = 3; 3 * a + 1 <= N; a += 2)
    {
        ll area = (ll)sqrt((3 * a + 1) * (a - 1));
        if(area * area == (3 * a + 1) * (a - 1))
        {
            res += 3 * a + 1;
        // cout<<a<<" "<<a<<" "<<a+1<<":"<<area<<endl;
        }
    }
    for(ll a = 3; 3 * a - 1 <= N; a += 2)
    {
        ll area = (ll)sqrt((3 * a - 1) * (a + 1));
        if(area * area == (3 * a - 1) * (a + 1))
        {
            res += 3 * a - 1;
        // cout<<a<<" "<<a<<" "<<a-1<<":"<<area<<endl;
        }
    }
    cout<<res<<endl;
}