#include <iostream>
#include <vector>

using namespace std;

int main()
{
    long long N = 5e7;
    vector<long long> cnt(N);

    for(long long a=0; a < 2 * N; a+=2){
        for(long long b=a; a * a - b * b < N && b >= 0; b--)
        {
            cnt[a * a - b * b]++;
        }
        for(long long b = (-a+1) / 2; (a * a - b * b < N) && b < 0; b++)
        {
            cnt[a * a - b * b]++;
        }
    }


    // for(long long a=0; a<1000; a++)
    // {
    //     for(long long d=0; d<1000; d++){
    //         long long x = a, y = a+d, z = a + 2 * d;
    //         long long n = z * z - y * y - x * x ;
    //         if(n < 100 && n > 0 && x > 0 && z > 0)
    //             cnt[n]--;
    //         if(n == 75)
    //             cout<<x<<":"<<y<<":"<<z<<endl;
    //     }
    // }

    long long res = 0;
    for(long long i=0; i<N; i++){
        if(cnt[i] == 1)
            res++;
        // cout<<i<<" : "<<cnt[i]<<endl;
    }
    cout<<res<<endl;
    // cout<<(-3)/2<<endl;
}