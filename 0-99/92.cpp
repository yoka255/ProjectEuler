#include <iostream>
#include <vector>

using namespace std;

int main()
{
    int N = 1e7;
    vector<int> res(N + 1, -1);
    res[1] = 1;
    res[89] = 89;
    for(int k=1; k<=N; k++)
    {
        int x = k;
        while(res[x] != 1 && res[x] != 89)
        {
            string s = to_string(x);
            x = 0;
            for(char c : s)
                x += (c - '0') * (c - '0');
        }
        int tmpres = res[x]; x = k;
        while(res[x] != 1 && res[x] != 89)
        {
            res[x] = tmpres;
            string s = to_string(x);
            x = 0;
            for(char c : s)
                x += (c - '0') * (c - '0');
        }
    }
    int cnt = 0;
    for(int i=1; i<=N; i++)
        if(res[i] == 89)
            cnt++;
    cout<<cnt<<endl;
}