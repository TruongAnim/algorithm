// https://codeforces.com/contest/1849/problem/B
#include <iostream>
#include <set>

struct PairCompare {
    bool operator()(const std::pair<int, int>& a, const std::pair<int, int>& b) const {
        if (a.first != b.first)
            return a.first < b.first;
        return a.second > b.second;
    }
};

using namespace std;

void process(){
    int n,k;
    cin>>n>>k;
    std::multiset<std::pair<int, int>, PairCompare> myMultiset;

    for (int i = 0; i< n; i++){
        int a; cin>>a;
        myMultiset.insert(make_pair(a<=k?a:a%k+k, i+1));
    }

    while(!myMultiset.empty()){
        auto lastElementIterator = std::prev(myMultiset.end());
        std::pair<int,int> lastElement = *lastElementIterator;
        myMultiset.erase(lastElementIterator);
        lastElement.first-=k;
        if(lastElement.first<=0){
            cout<<lastElement.second<<endl;
        }else{
            myMultiset.insert(std::make_pair(lastElement.first, lastElement.second));
        }
        // for (const auto& pair : myMultiset) {
        //     std::cout << "(" << pair.first << ", " << pair.second << ") ";
        // }
        // cout<<endl;
    }


}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int t; cin>> t;
    for(int i = 0; i< t; i++){
        process();
    }
    return 0;
}