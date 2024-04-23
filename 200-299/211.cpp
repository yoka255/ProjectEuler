#include <vector>
#include <iostream>
#include <cmath>

using namespace std;

typedef long long ll;

bool is_square(ll x){
    ll q = (ll)sqrt(x);
//    cout<<q<<":"<<x<<endl;
    while(q * q > x){
        q--;
    }
    while((q+1) * (q+1) <= x){
        q++;
    }
    return q * q == x;
}

int main(){
    ll N = 64e6;
    vector<ll> sieve( N, 1);
    for(ll p=2; p < N; p++){
        if(sieve[p] != 1)
            continue;
        for(ll k = p; k < N; k += p){
            ll mul = p * p, x = k, mulsum = 1;
            while(x % p == 0){
                mulsum += mul;
                x /= p;
                mul *= p * p;
            }
            sieve[k] *= mulsum;
        }
    }
    cout<<sieve[10]<<endl;
    cout<<sieve[1]<<endl;
    ll res = 0;
    for(ll k=1; k < N; k++){
        if(sieve[k] < 0){
            cout<<sieve[k]<<":"<<k<<endl;
            exit(314);
        }
        if(is_square(sieve[k])){
            res += k;
        }
    }
    cout<<res<<endl;
}