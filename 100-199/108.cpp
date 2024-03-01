#include <iostream>
#include <vector>

using namespace std;

int main()
{
    int N = 10000000;
    int goal = 1000;
    vector<int> t(N, 1);
    for(int i=2; i<N; i++)
    {
        if(t[i] == 1)
        {
            for(int m=i; m < N; m += i)
            {
                int k=0;
                for(int r=m; r % i == 0; r /= i)
                    k++;
                t[m] *= (2 * k+1);
            }
        }
    }
    // for(int i=0; i<20; i++)
    //     cout<<i<<" "<<t[i]<<endl;
    // cout<<endl;
    
    for(int i=0; i<N; i++)
    {
        if((t[i] + 1) / 2 >= goal)
        {
            cout<<i<<endl; return 0;
        }
    }
}