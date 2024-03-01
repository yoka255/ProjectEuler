#include <iostream>
#include <vector>

using namespace std;

typedef long long ll;

int main()
{
    int N = 1e6;
    vector<int> cnt(N+1);
    for(int a=0; a<=N; a++)
    {
        for(int b=a-2; b>0 && a * a - b * b <= N; b -= 2)
        {
            cnt[a * a - b * b]++;
        }
    }
    int res = 0;
    for(int a : cnt)
        if(1<=a && a <= 10)
            res++;
    cout<<res<<endl;
}