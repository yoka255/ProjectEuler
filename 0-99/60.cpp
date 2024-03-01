#include <iostream>
#include <vector>
#include <string>

using namespace std;

typedef long long ll;
typedef vector<ll> vi;
typedef vector<vi> vvi;


int main()
{
    ll N = (ll)1e8, M = (ll)1e4;
    vi p(N, 1);
    p[0] = 0, p[1] = 0;
    for(ll i=2; i<N; i++)
    {
        if(p[i])
            for(ll k=2*i; k<N; k+=i)
            {
                p[k] = 0;
            }
    }
    cout<<"BLA"<<endl;
    vi primes;
    for(ll k=0; k<M; k++)
        if(p[k])
            primes.push_back(k);
    
    vvi adj(M);
    vvi mat(M, vi(M, 0));
    for(ll i=0; i<primes.size(); i++)
    {
        ll k = primes[i];
        for(ll j = i+1; j < primes.size(); j++)
        {
            ll q = primes[j];
//            cout<<k<<" "<<q<<" "<<stoi(to_string(k) + to_string(q))<<" "<<stoi(to_string(q) + to_string(k))<<endl;
            if(stoll(to_string(k) + to_string(q)) < N && p[stoll(to_string(k) + to_string(q))] && p[stoll(to_string(q) + to_string(k))])
            {
                mat[k][q] = 1; 
                adj[k].push_back(q);
            }
        }
    }
    cout<<"BLA2"<<endl;
    for(ll a = 3; a < M; a++)
        for(ll b : adj[a])
        {
//            cout<<a<<" "<<b<<endl;
            for(ll c:adj[b])
                if(mat[a][c])
                    for(ll d:adj[c])
                        if(mat[a][d] && mat[b][d])
                        {
//                           cout<<a<<" "<<b<<" "<<c<<" "<<d<<":"<<a+b+c+d<<endl;
                            for(ll e:adj[d])
                                if(mat[a][e] && mat[b][e] && mat[c][e])
                                    cout<<a<<" "<<b<<" "<<c<<" "<<d<<" "<<e <<":"<<a+b+c+d+e<<endl;
                        }
        }
}