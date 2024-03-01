#include <iostream>
#include <vector>

using namespace std;

int main()
{
    int N = (1e8) + 1;
    vector<int> t(N, 0);
    for(int i=2; i<N; i++)
    {
        if(t[i] == 0)
        {
            for(int m=i; m < N; m += i)
            {
                int k=0;
                for(int r=m; r % i == 0; r /= i)
                    k++;
                t[m] += k;
            }
        }
    }
    // for(int i=0; i<20; i++)
    //     cout<<i<<" "<<t[i]<<endl;
    // cout<<endl;
    int res = 0;
    for(int i=2; i<N; i++)
    {
        if(t[i] == 2)
        {
            ++res;
        }
    }
    cout<<t[14]<<" "<<t[15]<<endl;
    cout<<res<<endl;
}