#include <iostream>
#include <cmath>
#include "euler.h"
#include <vector>
#include <unordered_set>
#include <algorithm>

using namespace std;


typedef __int128_t ii;

vector<ii> PRIMES = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29};
vector<ii> residues;


ii f(ii n){
    return 5 * n * n + 2 * n + 1;
}

bool is_golden(ii n){
    ii x = f(n);
    ii s = sqrt(x);
    return s * s == x;
}

void calc_res(ii i, ii curr, ii curr_prod){
    if(i == PRIMES.size()){
        residues.push_back(curr);
        return;
    }
    unordered_set<ii> squares;
    ii p = PRIMES[i];

    for(ii k=0; k<p; k++)
        squares.insert((k * k) % p);
    
    for(ii k = 0; k < p; k++){
        if(squares.find(f(k) % p) != squares.end()){
            ii inv1, inv2;
            gcd(curr_prod, p, inv1, inv2);
            inv1 = (inv1 % p + p) % p;
            inv2 = (inv2 % curr_prod + curr_prod) % curr_prod;
            calc_res(i + 1, (curr_prod * inv1 * k + p * inv2 * curr) % (p * curr_prod), curr_prod * p);
        }
    }
}

int main(){
    residues = vector<ii>();

    calc_res(0, 0, 1);

    sort(residues.begin(), residues.end());

    // for(ii i=0; i<residues.size(); i++){
    //     cout<<residues[i]<<" ";
    // }
    // cout<<endl;

    ii cnt = 0;
    ii target = 16;
    long long i = 0;
    long long prod = 1;
    for(ii x : PRIMES)
        prod *= x;
    cout<<prod<<endl;
    cout<<(double)residues.size() / prod<<endl;
    while(cnt != target){
        for(long long k : residues){
            if(is_golden(i + k)){
                cout<<i + k<<endl;
                ++cnt;
                // if(cnt == target)
                //     exit(0);
            }
        }
        i += prod;
    }

}