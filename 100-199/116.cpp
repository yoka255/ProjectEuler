#include <iostream>
#include <vector>

using namespace std;

int main()
{
    int n = 50;
    vector<long long> a(n + 1), b(n + 1), c(n + 1);
    a[0] = 1; b[0] = 1; c[0] = 1;
    for(int i=1; i<=n; i++)
    {
        a[i] += a[i-1] + (i >= 2 ? a[i-2] : 0);
        b[i] += b[i-1] + (i >= 3 ? b[i-3] : 0);
        c[i] += c[i-1] + (i >= 4 ? c[i-4] : 0);
    }
    cout<<a[n] + b[n] + c[n] - 3<<endl;
}