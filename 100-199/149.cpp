#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

ll math_mod(ll x, ll m){
    return (x % m + m) % m; 
}

int main(){
    ll n = 2000 * 2000 + 1;
    ll mod = 1000000;
    vector<ll> s(n);
    for(ll k=1; k<=55; k++){
        s[k] = 100003 - 200003 * k + 300007 * k * k * k;
        s[k] = math_mod(s[k], 1000000);
        s[k] -= mod/2;
    }
    for(ll k=56; k<n; k++){
        s[k] = (s[k-24] + s[k-55] + mod) % mod - mod/2;
    }
    ll res = 0;
    cout<<s[55]<<endl;
    cout<<s[10] <<":"<< s[100]<<endl;

    for(int i=0; i<n; i++){
        s[i] = s[i+1];
    }

    for(int i=0; i<2000; i++){
        ll cur = 0;
        for(int j=0; j<2000; j++){
            cur = max(cur, 0LL);
            cur += s[i * 2000 + j];
            res = max(res, cur);
        }
    }
    for(int i=0; i<2000; i++){
        ll cur = 0;
        for(int j=0; j<2000; j++){
            cur = max(cur, 0LL);
            cur += s[j * 2000 + i];
            res = max(res, cur);
        }
    }
    for(int i=0; i<2000; i++){
        ll cur = 0;
        for(int j=0; i+j<2000; j++){
            cur = max(cur, 0LL);
            cur += s[(i+j) * 2000 + j];
            res = max(res, cur);
        }
    }
    for(int j=0; j<2000; j++){
        ll cur = 0;
        for(int i=0; i+j<2000; i++){
            cur = max(cur, 0LL);
            cur += s[(i+j) * 2000 + j];
            res = max(res, cur);
        }
    }

    for(int i=0; i<2000; i++){
        ll cur = 0;
        for(int j=2000-1; i-j < 1 && j >= 0; j--){
            cur = max(cur, 0LL);
            cur += s[(i+2000-1-j) * 2000 + j];
            res = max(res, cur);
        }
    }
    for(int j=2000-1; j >= 0; j--){
        ll cur = 0;
        for(int i=0; i<2000 && i-j < 1; i++){
            cur = max(cur, 0LL);
            cur += s[(i+2000-1-j) * 2000 + j];
            res = max(res, cur);
        }
    }
    cout<<res<<endl;
}