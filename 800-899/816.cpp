#include <bits/stdc++.h>

using namespace std;

long long square(long long x){
    return x * x;
}

long long ClosestPair(vector<pair<long long, long long>> pts) {
    int n = pts.size();
    sort(pts.begin(), pts.end());
    set<pair<long long, long long>> s;

    long long best_dist = square(pts[0].first - pts[1].first) + square(pts[0].second - pts[1].second);
    int j = 0;
    for (int i = 0; i < n; ++i) {
        long long d = ceil(sqrt(best_dist));
        while (pts[i].first - pts[j].first >= d) {
            s.erase({pts[j].second, pts[j].first});
            j += 1;
        }

        auto it1 = s.lower_bound({pts[i].second - d, pts[i].first});
        auto it2 = s.upper_bound({pts[i].second + d, pts[i].first});
        
        for (auto it = it1; it != it2; ++it) {
            int dx = pts[i].first - it->second;
            int dy = pts[i].second - it->first;
            best_dist = min(best_dist, 1LL * dx * dx + 1LL * dy * dy);      
        } 
        s.insert({pts[i].second, pts[i].first}); 
    }
    return best_dist;
}

int main(){
    int n = 2000000;
    vector<pair<long long,long long>> pts;
    long long s = 290797;
    for(int i=0; i<n; i++){
        long long a = s;
        s = s * s % 50515093;
        long long b = s;
        s = s * s % 50515093;
        pts.emplace_back(a,b);
    }
    cout<<std::fixed;
    cout<<setprecision(9);
    cout<<sqrt(ClosestPair(pts))<<endl;
    cout<<sqrt(2)<<endl;
}