#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int digsum(int n)
{
    if(n == 0)
        return 0;
    return n % 10 + digsum(n/10);
}

int main()
{
    int N = 1e6;
    vector<int> dig_root(N);
    for(int i=0; i<10; i++)
        dig_root[i] = i;
    for(int i=10; i<N; i++)
        dig_root[i] = dig_root[digsum(i)];
    
    vector<vector<int>> facts(N);
    for(int p=2; p<N; p++)
    {
        for(int j=p; j<N; j+=p){
            facts[j].push_back(p);
        }
    }

    vector<int> MDRS(N);
    MDRS[1] = 0;
    for(int n=2; n<N; n++)
    {
        for(int d : facts[n])
            MDRS[n] = max(MDRS[n], MDRS[n/d] + dig_root[d]);
    }
    long long res = 0;
    for(int x : MDRS)
        res += x;
        cout<<res<<endl;
}