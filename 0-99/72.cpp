#include <iostream>
#include <vector>

using namespace std;

typedef vector<int> vi;
typedef long long ll;

int main()
{
    int N = 1e6;
    vi tot(N+1);
    for(int i=0; i<=N; i++)
        tot[i] = i;
    for(int i=2; i<=N; i++)
    {
        if(tot[i] == i)
            for(int j=i; j<=N; j+=i)
                tot[j] = (tot[j]) / i * (i-1);
    }
    ll cnt = 0;
    for(int i=2; i<=N; i++)
        cnt += tot[i];
    cout<<cnt<<endl;
}