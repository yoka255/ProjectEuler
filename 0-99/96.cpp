#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

typedef vector<int> vi;
typedef vector<vi> vvi;

bool canplace(int i, int j, vvi& mat, int n)
{
    for(int l=0; l<9; l++)
        if(mat[i][l] == n)
            return false;
    for(int l=0; l<9; l++)
        if(mat[l][j] == n)
            return false;
    int x = 3 * (i/3), y = 3 * (j/3);
    for(int k=0; k<3; k++)
        for(int l=0; l<3; l++)
            if(mat[x+k][y+l] == n)
            return false;
    return true;
}

int solve(int i, int j, vvi& mat)
{
    if(j == 9)
        j = 0, i++;
    if(i == 9)
    {
        return 100 * mat[0][0] + 10 * mat[0][1] + mat[0][2];
    }
    if(mat[i][j] > 0)
        return solve(i, j+1, mat);
    for(int n=1; n<=9; n++)
    {
        if(canplace(i, j, mat, n))
        {
            mat[i][j] = n;
            int tmp = solve(i, j+1, mat);
            if(tmp != -1)
                return tmp;
            mat[i][j] = 0;
        }
    }
    return -1;
}

int main()
{
    ifstream fin("p096_sudoku.txt");
    int n = 50;
    int res = 0;
    for(int sod = 0; sod < 50; sod++)
    {
        vvi mat(9, vi(9));
        string a;
        fin>>a>>a;
        cout<<a<<endl;
        for(int i=0; i<9; i++)
        {
            string nums;
            fin>>nums;
            for(int j=0; j<9; j++)
                mat[i][j] = nums[j]- '0';
        }
        res += solve(0, 0, mat);
    }
    cout<<res<<endl;
}