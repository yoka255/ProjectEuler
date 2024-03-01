#include <iostream>
#include <vector>

using namespace std;

typedef long long ll;

int main(){
    int N = 40000000;
    vector<int> phi(N);
    for(int n=0; n<N; n++)
        phi[n] = n;
    for(int p=2; p<N; p++){
        if(phi[p] == p){
            for(int k=p; k < N; k+=p){
                phi[k] /= p;
                phi[k] *= (p-1);
            }
        }
    }
    ll sum = 0;
    vector<int> len(N);
    len[1] = 1;
    for(int n=2; n<N; n++){
        len[n] = len[phi[n]] + 1;
        if(phi[n] == n-1 && len[n] == 25)
            sum += n;
    }
    cout<<sum<<endl;
}