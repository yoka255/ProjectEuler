#include <vector>
#include <iostream>
#include <random>

using namespace std;

typedef long long ll;

__int128_t randrange(__int128_t a, __int128_t b){
    return rand() % (b - a) + a;
}

__int128_t modpow(__int128_t a, __int128_t b, __int128_t mod){
    __int128_t res = 1;
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

bool miller_rabin(__int128_t n, __int128_t k){
    if(n == 2 || n == 3)
        return true;
    if(n % 2 == 0)
        return false;

    __int128_t r = 0, s = n - 1;
    while(s % 2 == 0){
        r += 1;
        s >>= 1;
    }
    for(int i=0; i<k; i++){
        __int128_t a = randrange(2, n-1);
        __int128_t x = modpow(a, s, n);
        if(x == 1 || x == n-1)
            continue;
        for(int j=0; j<r-1; j++){
            if(x == 1 || x == -1)
                break;
            x = (x * x) % n;
        }
        if(! (x == 1 || x == n-1))
            return false;
    }
    return true;
}

__int128_t gcd(__int128_t a, __int128_t b, __int128_t& x, __int128_t& y) {
    if (b == 0) {
        x = 1;
        y = 0;
        return a;
    }
    __int128_t x1, y1;
    __int128_t d = gcd(b, a % b, x1, y1);
    x = y1;
    y = x1 - y1 * (a / b);
    return d;
}