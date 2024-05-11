#include <iostream>
#include <vector>

using namespace std;

int main(){
    int N = 1e9;
    vector<int> primes = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97};

    int res = 0;
    for(int k=1; k<=N; k++){
        if(k % 1000000 == 0)
            cout<< k / 1000000<<endl;
        int n = k;
        for(int p : primes){
            while(!(n % p))
                n /= p;
        }
        if(n == 1)
            ++res;
    }
    cout<<res<<endl;
}