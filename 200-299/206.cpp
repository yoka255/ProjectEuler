#include <iostream>
#include <string>

using namespace std;

typedef long long ll;

bool ok(ll n)
{
    string s = to_string(n);
    if(s.size() != 17)
        return false;
    for(int i=0; i<s.size(); i+=2)
        if(s[i]-'0' != i/2 + 1)
            return false;
    return true;
}

int main()
{
    for(ll n = 0; 1; n++)
    {
        // if(n % 1000000 == 0)
        //     cout<<n<<endl;
        if(ok(n * n))
        {
            cout<<n<<":"<<n * n<<endl;
            return 0;
        }
    }
}