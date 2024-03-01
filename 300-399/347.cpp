#include <iostream>
#include <vector>
#include <set>

using namespace std;

typedef long long ll;

int main()
{
    int N = 1e7;
    vector<vector<int>> p(N+1);
    for(int k=2; k<=N; k++)
    {
        if(!p[k].size())
        {
            for(int j=2*k; j <= N; j += k)
            {
                if(p[j].size() <= 2)
                    p[j].push_back(k);
            }
        }
    }
    set<pair<int,int>> a;

    ll sum = 0;
    for(int k=N; k>=1; k--)
    {
        if(p[k].size() == 2 && a.find(make_pair(p[k][0], p[k][1])) == a.end())
        {
            a.insert(make_pair(p[k][0], p[k][1]));
            sum += k;
        }
    }
    cout<<sum<<endl;
}