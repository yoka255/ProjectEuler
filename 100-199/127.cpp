#include <iostream>
#include <vector>

using namespace std;

typedef long long ll;

ll gcd(ll a, ll b)
{
    if(a < b)
        return gcd(b, a);
    if(b == 0)
        return a;
    return gcd(b, a%b);
}

ll lcm(ll a, ll b)
{
    return a * b / gcd(a,b);
}

ll lcm(ll a, ll b, ll c)
{
    return lcm(a, lcm(b, c));
}

int main()
{
    int N = 120000;
    vector<int> rad(N+1, 1);
    for(int i=2; i<=N; i++)
    {
        if(rad[i] == 1)
            for(int j=i; j<=N; j+=i)
                rad[j] *= i;
    }
    int res = 0;
    for(int a=0; a<N; a++)
        for(int b=a+1; b<N-a; b++)
        {
            int c = a+b;
            if(gcd(a,b) == 1 && lcm(rad[a], rad[b], rad[c]) < c){
//                cout<<a<<":"<<b<<":"<<c<<endl;
                res += c;
            }
        }
    cout<<res<<endl;
}