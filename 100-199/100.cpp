#include <iostream>
#include <vector>
#include <tgmath.h>
#include <tuple>

using namespace std;

typedef long long ll;

int main()
{
    tuple<ll, ll> curr = make_tuple(3, 1);
    ll N = 1e12;
    while(1)
    {
        ll x, y;
        tie(x, y) = curr;
        if((2*y + 1 + x) % 2 == 0 && (2*y + 1 + x)/2 + y > N)
        {
            cout<<(2*y + 1 + x)/2<<":"<<y<<endl;
            return 0;
        }
        curr = make_tuple(3 * x + 8 * y, 3 * y + x);
    }
}