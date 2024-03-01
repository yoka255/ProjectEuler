#include <iostream>
#include <vector>
#include <queue>
#include <fstream>
#include <tuple>
#include <algorithm>

using namespace std;

typedef long long ll;
typedef vector<ll> vi;
typedef vector<vi> vvi;
typedef tuple<ll,ll,ll> tri;

int main()
{
    ifstream fin("p082_matrix.txt");
    int n = 80;
    vvi mat(n, vi(n, -1)), dist(n, vi(n, -1));
    for(int i=0; i<n; i++)
        for(int j=0; j<n; j++)
            fin>>mat[i][j];

    priority_queue<tri, vector<tri>, greater<tri>> dji;
    for(int i=0; i<n; i++)
        dji.push(make_tuple(mat[i][0], i, 0));
    while(!dji.empty())
    {
        ll i, j, d;
        tie(d, i, j) = dji.top();
        dji.pop();
        if(dist[i][j] == -1)
        {
            dist[i][j] = d;
            if(i < n - 1)
                dji.push(make_tuple(d + mat[i+1][j], i + 1, j));
            if(j < n - 1)
                dji.push(make_tuple(d + mat[i][j+1], i, j + 1));
            if(i > 0)
                dji.push(make_tuple(d + mat[i-1][j], i-1, j));
        }
    }
    ll res = 1e18;

    for(int i=0; i<n; i++)
        res = min(res, dist[i][n-1]);
    cout<<res<<endl;
}
