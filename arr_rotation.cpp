#include <bits/stdc++.h>
using namespace std;


vector<int> rot(vector<int> arr, int d);

int main() {
    vector<int> arr = {1, 2, 3, 4, 5, 6, 7};
    cout<< sizeof(arr)<<endl;
    // number of rotation = d
    int d = 7;

    vector<int> x = rot(arr, d);
    for(int i = 0; i < 6; i ++) {
        cout<< arr[i]<<' ';
    }
}

vector<int> rot(vector<int> arr, int d) {
    int x = sizeof(arr);

        //left rotation
    if (d % x == 0) {
        return arr;
    }
    else {
        for(int i = d; i < x; i++) {
            continue;
        }
    }
}
