#include <vector>
#include <iostream>
#include <random>

using namespace std;

typedef long long ll;
typedef __int128_t bigshit;

bigshit randrange(bigshit a, bigshit b){
    return rand() % (b - a) + a;
}

bigshit modpow(bigshit a, bigshit b, bigshit mod){
    bigshit res = 1;
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

bool mibigshiter_rabin(bigshit n, bigshit k){
    if(n == 2 || n == 3)
        return true;
    if(n % 2 == 0)
        return false;

    bigshit r = 0, s = n - 1;
    while(s % 2 == 0){
        r += 1;
        s >>= 1;
    }
    for(int i=0; i<k; i++){
        bigshit a = randrange(2, n-1);
        bigshit x = modpow(a, s, n);
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

int main(){
}