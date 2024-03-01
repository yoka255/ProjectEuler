#include <iostream>
#include <vector>
#include <tgmath.h>

using namespace std;

#define MOD (993353399)

__int128_t phi(__int128_t p, __int128_t k, vector<vector<__int128_t>>& prime_decomp, __int128_t offset){
    __int128_t res = k;
    for(__int128_t q : prime_decomp[p-1 - offset]){
        if(k % q == 0){
            res = (res / q) * (q-1);
        }
    }
    return res % MOD;
}
__int128_t go_over_divs(__int128_t p, __int128_t x, __int128_t d, int index, vector<vector<__int128_t>>& prime_decomp, __int128_t offset){
    // sum of phi(p-1/d) * d for all divisors of x
    if(index >= prime_decomp[p - 1 - offset].size())
        return 0;
    __int128_t res = 0;//d * phi(p, (p-1)/d, prime_decomp, offset);
    if(x % (d * prime_decomp[p-1-offset][index]) == 0){
        __int128_t newd = d * prime_decomp[p-1-offset][index];
        res += newd * phi(p, (p-1)/newd, prime_decomp, offset);
        res += go_over_divs(p, x, newd, index, prime_decomp, offset);
    }
    res += go_over_divs(p, x, d, index + 1, prime_decomp, offset);
    return res % MOD;
}
__int128_t magic_val(__int128_t p, __int128_t k, vector<vector<__int128_t>>& prime_decomp, __int128_t offset){
    // __int128_t res = 1;
    // for(__int128_t q : prime_decomp[p-1 - offset]){
    //     __int128_t tmpval = 0;
    //     __int128_t tmpmul = 1;
    //     while(((p-1) / k) % tmpmul == 0){
    //         tmpval += tmpmul;
    //         tmpmul *= q;
    //     }
    //     res *= tmpval;
    //     res %= MOD;
    // }
    __int128_t res = go_over_divs(p, (p-1)/k, 1, 0, prime_decomp, offset);
    res += phi(p, (p-1), prime_decomp, offset);
    // for(__int128_t i=1; i<=(p-1) / k; i++)
    //     if(((p-1) /  k) % i == 0)
    //         res += i * phi(p, (p-1) / i, prime_decomp, offset);
    return (res * res) % MOD;
}



int main(){
    __int128_t range_start = (__int128_t)1e16;
    __int128_t range_end = range_start + (__int128_t)1e6;
    vector<__int128_t> sieve((int)sqrt(range_end) + 3, 1), primes;
    for(int k = 2; k < sieve.size(); k++){
        if(sieve[k]){
            for(int j=2 * k; j < sieve.size(); j += k){
                sieve[j] = 0;
            }
            primes.push_back(k);
        }
    }
    __int128_t offset = (range_start - 1);
    vector<vector<__int128_t>> prime_decomp(range_end - range_start + 1); //value at place i is the prime decomp of range_start + i - 1

    for(__int128_t p : primes){
        __int128_t start_point = p * ((range_start - 1 + p - 1) / p);
        for(__int128_t j = start_point; j < offset + prime_decomp.size(); j += p){
            prime_decomp[j - offset].push_back(p);
        }
    }
    cout<<"BLA"<<endl;
    for(__int128_t j=0; j<prime_decomp.size(); j++){
        if(j + offset > 1){
            __int128_t tmp = j + offset;
            for(__int128_t q : prime_decomp[j]){
                while(tmp % q == 0)
                    tmp /= q;
            }
            if(tmp != 1){
                prime_decomp[j].push_back(tmp);
            }
        }
    }
    cout<<"BLA"<<endl;
    vector<__int128_t> f(range_end - range_start + 1, 0);

    __int128_t res = 0;

    for(__int128_t j=range_start; j < range_end; j++){
        cout<<(long long)j<<endl;
        if(!prime_decomp[j - offset].empty() && prime_decomp[j - offset][0] == j)
            f[j] += (j-1) * (j-1);
    }
    cout<<"BLA"<<endl;
    // for(int j=2; j<100; j++){
    //     cout<<j<<":";
    //     for(int q : prime_decomp[j]){
    //         cout<<q<<" ";
    //     }
    //     cout<<endl;
    // }

    for(__int128_t k=1; k * k < range_end; k++){
        cout<<(long long)k<<endl;
        __int128_t start_point = k * ((range_start - 1 + k - 1) / k);
        for(__int128_t j=start_point; j < range_end - 1; j += k){
            if(j > 0 && prime_decomp[j + 1 - offset][0] == j + 1){
                f[j+1 - offset] += phi(j+1, k, prime_decomp, offset) * magic_val(j+1, k, prime_decomp, offset);
//                cout<<(int)(j+1)<<"/"<<(int)k<<"    ";
//                cout<<(int)phi(j+1, k, prime_decomp, offset) << ":" <<(int)magic_val(j+1, k, prime_decomp, offset) << endl;
                if((j / k) * (j / k) >= range_end){
//                    cout<<(int)(j+1)<<"/"<<(int)(j/k)<<"     ";
//                    cout<<(int)phi(j+1, j/k, prime_decomp, offset) << ":" <<(int)magic_val(j+1, j/k, prime_decomp, offset) << endl;
                    f[j+1 - offset] += phi(j+1, j/k, prime_decomp, offset) * magic_val(j+1, j/k, prime_decomp, offset);
                }
                f[j+1 - offset] %= MOD;
            }
        }
    }

    // for(int i=2; i<100; i++){
    //     if(f[i] != 0){
    //         cout<<i<<":"<<(int)f[i]<<endl;
    //     }
    // }
    for(__int128_t s : f)
        res = (res + s) % MOD;
    cout<<(long long)res<<endl;
}