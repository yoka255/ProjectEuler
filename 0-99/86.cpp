#include <iostream>
#include <tgmath.h>
#include <algorithm>

using namespace std;

typedef long long ll;

int main()
{
    ll M = 1;
    int counter = 0;
    while(counter < 1e6)
    {
        ll a = M;
        for(ll b = 1; b <= a; b++)
            for(ll c = 1; c <= b; c++)
            {
                double d = sqrt(min(min((a + b) * (a + b) + c * c, (a + c) * (a + c) + b * b), (b + c) * (b + c) + a * a));
                if(d - (int)d < 1e-5)
                    counter++;
            }
        if(!(M % 1000))
            cout<<M<<":"<<counter<<endl;
        M++;
    }
    cout<<M<<endl;
}