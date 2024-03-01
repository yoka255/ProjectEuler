#include <iostream>
#include <vector>

using namespace std;

typedef long long ll;

int main()
{
    int n = 50;
    vector<ll> a(n + 1), b(n + 1), c(n + 1);
    a[0] = 1; b[0] = 1; c[0] = 1;
    for(int i=1; i<=n; i++)
    {
        a[i] += a[i-1] + (i >= 2 ? a[i-2] : 0) + (i >= 3 ? a[i-3] : 0) + (i >= 4 ? a[i-4] : 0);
    }
    cout<<a[n]<<endl;
}