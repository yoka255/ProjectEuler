#include <iostream>
#include <vector>
#include <set>
#include <cmath>

using namespace std;

typedef long long ll;

ll MAX_RES = 120000;
vector<vector<int>> OPTS(MAX_RES + 1);

bool is_int(double x){
    return (int)x == x;
}

ll check_solution(int p, int b, int c){
    double q = (p + sqrt(4 * b * b - 3 * p * p)) / 2;
    double r = (p + sqrt(4 * c * c - 3 * p * p)) / 2;
    double a = sqrt(q * q + r * r - q * r);
    if(is_int(q) && is_int(r) && is_int(a)){
        return (ll)(p + q + r);
    }
    return 0;
}

int main(){
    for(ll b = 0; b < 2 * MAX_RES; b++){
        ll p = 1;
        while(p < MAX_RES && 4 * b * b - 3 * p * p > 0){
            if(is_int(sqrt(4 * b * b - 3 * p * p))){
                OPTS[p].push_back((b));
            }
            ++p;
        }
    }

    for(ll p = 0; p < 100; p++){
        if(OPTS[p].empty())
            continue;
        cout<<p<<endl;

    }

    set<int> res;
    for(ll p=0; p < MAX_RES; p++){
        for(ll b : OPTS[p]){
            for(ll c : OPTS[p]){
                ll sol = check_solution(p, b, c);
                if(sol && sol <= MAX_RES)
                    res.insert(sol);
            }
        }
    }
    ll sum = 0;
    for(ll x: res){
        sum += x;
    }
    cout<<sum<<endl;
}
