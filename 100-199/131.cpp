#include <iostream>
#include <vector>

using namespace std;

int main()
{
    int N = 1000000;
    vector<int> p(N,1);
    p[0] = 0;
    p[1] = 0;
    for(int i=2; i<N; i++)
    {
        for(int j=2*i; j<N; j+=i)
        {
            p[j] = 0;
        }
    }
    int res = 0;
    for(int y = 0; 3*y*y + 3*y + 1 < N; y++)
    {
        if(p[3*y*y + 3*y + 1])
        {
            res++;
            int n = y * y * y;
            cout << n * n * (n + (3*y*y + 3*y + 1)) <<":"<< 3*y*y + 3*y + 1 << endl;
        }
    }
    cout<<res<<endl;
}