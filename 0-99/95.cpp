#include <iostream>
#include <vector>
#include <unordered_set>

using namespace std;

int main()
{
    int N = 1e6;
    vector<int> d(N+1);
    for(int i=1; i<=N; i++)
    {
        for(int j=2*i; j<=N; j+=i)
        {
            d[j] += i;
        }
    }
    int res = 0, best = 1;
    for(int i=1; i<=N; i++)
    {
        int x = d[i];
        int cnt = 1;
        unordered_set<int> vis;
        vis.insert(i);
        while(vis.find(x) == vis.end())
        {
            vis.insert(x);
            if(x > N)
                cnt = 0, x = i;
            else
                x = d[x];
            cnt++;
            
        }
        if(cnt > best && x == i)
        {
            cout<<i<<" "<<cnt<<endl;
            best = cnt, res = i;
        }

    }
}