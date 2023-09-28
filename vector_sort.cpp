#include <bits/stdc++.h>
using namespace std;

int main() {
    int a;
    cin>>a;
    cin.ignore();
    
    vector<int> arr;
    string input;
    getline(cin, input);
    istringstream is(input); 
    int num;
    while (is>>num) arr.push_back(num);
    sort(arr.begin(), arr.end());
    for(int x : arr) {
        cout<<x<<' ';
    }
    
    return 0;
}