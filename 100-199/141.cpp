#include "../euler.h"
#include <vector>
#include <algorithm>
#include <set>
#include <cmath>
#include <iostream>

using namespace std;

typedef long long ll;
typedef __int128_t ii;

bool is_square(ll x){
    ll s = int(sqrt(x));
    return s * s == x;
}

int main(){
    ii N = 1e12;
//    N = 1e5;
    vector<vector<ll>> divs = get_divs(1000001);
    vector<vector<ll>> good_divs(1e6 + 1);
    for(ll a=1; a<=1e6; a++){
        reverse(divs[a].begin(), divs[a].end());
        for(ll d : divs[a]){
            if(a % (d * d) == 0)
                good_divs[a].push_back(d);
        }
    }
    set<ll> res_set;
    for(ll a=1; a * a < N; a++){
        if(a % 10000 == 0)
            cout<<a<<endl;
        for(ll b=1; b * b * b * sqrt(a) < N; b++){
            for(ll c : good_divs[a]){
                if(c > b)
                    continue;
                if(a * a / (c * c * c) * b * b * b + a > N)
                    break;
                if(gcd(b, c) != 1)
                    continue;
                if(is_square(a * a / (c * c * c) * b * b * b + a)) {
//                    cout<<a * a / (c * c * c) * b * b * b + a<<endl;
                    res_set.insert(a * a / (c * c * c) * b * b * b + a);
                }
            }
        }
    }
    ll res = 0;
    for(ll s : res_set)
        res += s;
    cout<<res<<endl;
}