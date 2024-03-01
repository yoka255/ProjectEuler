#include <iostream>
#include <vector>

using namespace std;

typedef long long ll;

ll gcd(ll a, ll b)
{
    if(b == 0)
        return a;
    if(a < b)
        return gcd(b, a);
    return gcd(b, a%b);
}

int main()
{
    int cnt = 0, N = 12000;
    for(int d = 2; d <= N; d++)
    {
        for(int a = d/3; a < (double)d/2; a++)
        {
            if(gcd(a, d) == 1 && (double)a/d > 1.0/3 && (double)a/d < 1.0/2)
            {
                cnt++;
            }
        }
    }
    cout<<cnt<<endl;
}