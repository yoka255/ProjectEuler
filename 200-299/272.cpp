#include <iostream>
#include <vector>

using namespace std;

typedef __int128_t ll;
typedef vector<ll> vl;

vl prefsum, relprimes, sieve, no_3_prefsum;
ll limit = 1e11, n = 1e7;

std::ostream&
operator<<( std::ostream& dest, __int128_t value )
{
    std::ostream::sentry s( dest );
    if ( s ) {
        __uint128_t tmp = value < 0 ? -value : value;
        char buffer[ 128 ];
        char* d = std::end( buffer );
        do
        {
            -- d;
            *d = "0123456789"[ tmp % 10 ];
            tmp /= 10;
        } while ( tmp != 0 );
        if ( value < 0 ) {
            -- d;
            *d = '-';
        }
        int len = std::end( buffer ) - d;
        if ( dest.rdbuf()->sputn( d, len ) != len ) {
            dest.setstate( std::ios_base::badbit );
        }
    }
    return dest;
}


ll calc_res(ll prod, int index, int count){
    if(prod > limit)
        return 0;
    if(count == 5){
        // cout<<prod<<endl;
        // exit(0);
        ll end = limit / prod;
        if(end >= n){
            cout<<"FUCK"<<endl;
            exit(0);
        }
        
        if(prod % 3 == 0){
//            cout<<prod<<":"<<end<<":"<<no_3_prefsum[end]<<endl;
            return no_3_prefsum[end] * prod;
        }
//        cout<<prod<<":"<<end<<":"<<prefsum[end]<<endl;
        return prefsum[end] * prod;
    }
    ll res = 0;
    while(index < relprimes.size() && prod * relprimes[index] <= limit){
        ll p = relprimes[index];
        ll mul = p;
        if(p == 9)
            mul = 3;
        while(p * prod < limit){
            res += calc_res(prod * p, index + 1, count + 1);
            p *= mul;
        }
        index++;
    }
    return res;
}

string my_to_string(ll a){
    if(a < 10){
        return "" + (char)('0' + (int)a);
    }
    return my_to_string(a / 10) + (char)('0' + (int)(a % 10));
}


int main(){
//    limit = 1000000;

    prefsum = vl(n);
    no_3_prefsum = vl(n);
    sieve = vl(n, 1);
    sieve[0] = 0;
    sieve[1] = 0;
    for(ll i=2; i<n; i++){
        if(i == 9){
            relprimes.push_back(9);
        }
        if(sieve[i]){
            for(ll k = 2 * i; k<n; k+=i){
                sieve[k] = 0;
            }
            if(i % 3 == 1){
                relprimes.push_back(i);
            }
        }
    }
    cout<<"Done initial sieve"<<endl;
    sieve = vl(n, 1);
    sieve[0] = 0;
    for(ll p : relprimes){
        for(ll i = p; i <= n; i+=p){
            sieve[i] = 0;
        }
    }
    cout<<"Done second sieve"<<endl;
    for(ll i=1; i<n; i++){
        prefsum[i] = sieve[i] * i + prefsum[i-1];
        if(i % 3 != 0){
            no_3_prefsum[i] = sieve[i] * i + no_3_prefsum[i-1];
        }
        else{
            no_3_prefsum[i] = no_3_prefsum[i-1];
        }
    }
    cout<<"Done prefsum"<<endl;
    ll regs = calc_res(1, 0, 0);
    cout<<"Calculated res"<<endl;
    cout<<regs<<endl;
}