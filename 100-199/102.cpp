#include <iostream>
#include <vector>
#include <tgmath.h>
#include <fstream>

using namespace std;

typedef long long ll;
#define X first
#define Y second

ll orient(ll a, ll b, ll x, ll y)
{
    ll s = a * y - b * x;
    if(s == 0)
        return 0;
    return s / abs(s);
}

ll side(pair<ll,ll> a, pair<ll,ll> b, pair<ll,ll> x)
{
    return orient(b.X - a.X, b.Y - a.Y, x.X - b.X, x.Y - b.Y);
}

int main()
{
    ifstream fin("p102_triangles.txt");
    int N = 1000;
    int count = 0;
    for(int i=0; i<N; i++)
    {
        pair<ll,ll> x, y, z;
        fin>>x.X>>x.Y>>y.X>>y.Y>>z.X>>z.Y;
        ll a = side(x, y, make_pair(0, 0)), b = side(y, z, make_pair(0,0)), c = side(z, x, make_pair(0,0));
        if(a && a == b && a == c)
            ++count;
    }
    cout<<count<<endl;
}