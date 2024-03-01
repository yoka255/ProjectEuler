#include <iostream>
#include <vector>

using namespace std;

typedef long long ll;

int main()
{
    vector<ll> fib(50);
    fib[0] = 0; fib[1] = 1;
    for(int i=2; i<50; i++)
        fib[i] = fib[i-1] + fib[i-2];
    int count = 0;
    for(int i=1; i<=1<<7; i++)
        if((i ^ (i * 2) ^ (i * 3)) == 0)
            ++count;
    cout<<count - fib[9]<<endl;
    cout<<fib[32]<<endl;
}