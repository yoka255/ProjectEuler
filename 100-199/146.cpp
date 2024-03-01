#include <vector>
#include <iostream>
#include <random>

using namespace std;

typedef __int128_t ll;

ll randrange(ll a, ll b){
    ll x = rand();
    x <<= 32;
    x += rand();
    return (x % (b - a)) + a;
}

ll modpow(ll a, ll b, ll mod){
    ll res = 1;
    while(b){
        if(b & 1)
            res *= a;
        a *= a;
        b >>= 1;
        a %= mod;
        res %= mod;
    }
    return res;
}

bool miller_rabin(ll n, ll k){
    if(n == 2 || n == 3)
        return true;
    if(n % 2 == 0)
        return false;

    ll r = 0, s = n - 1;
    while(s % 2 == 0){
        r += 1;
        s /= 2;
    }
    for(int i=0; i<k; i++){
        ll a = randrange(2, n-1);
        ll x = modpow(a, s, n);
        if(x == 1 || x == n-1)
            continue;
        for(int j=0; j<r-1; j++){
            if(x == 1 || x == n-1)
                break;
            x = (x * x) % n;
        }
        if(! (x == 1 || x == n-1)){
            return false;
        }
    }
    return true;
}

int main(){
    srand(1987);
    ll N = 150000000;
//    N = 1000000;
    long long sum = 0;
//    N = 1000000;
    int k = 100;
    for(ll n=10; n<N; n+=6){
        if(n % 100000 == 0)
            cout<<(long long)n<<endl;
        if(miller_rabin(n * n + 1, k) && miller_rabin(n * n + 3, k) && miller_rabin(n * n + 7, k) && miller_rabin(n * n + 9, k) && miller_rabin(n * n + 13, k) && miller_rabin(n * n + 27, k)){
            if(miller_rabin(n * n + 19, k) || miller_rabin(n * n + 21, k))
                continue;
            sum += n;
        }
    }
    for(ll n=14; n<N; n+=6){
        if(n % 100000 == 0)
            cout<<(long long)n<<endl;
        if(miller_rabin(n * n + 1, k) && miller_rabin(n * n + 3, k) && miller_rabin(n * n + 7, k) && miller_rabin(n * n + 9, k) && miller_rabin(n * n + 13, k) && miller_rabin(n * n + 27, k)){
            if(miller_rabin(n * n + 19, k) || miller_rabin(n * n + 21, k))
                continue;
            sum += n;
        }
    }
//    cout<<miller_rabin(642095669020709LL, 100)<<endl;
    cout<<sum<<endl;
}