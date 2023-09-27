#include <bits/stdc++.h>
using namespace std;

int divide(int dividend, int divisor);

int main() {
    // int dividend = 7;
    // int divisor = -3;
    int dividend = INT_MIN ;
    int divisor = -1;
    int x = divide(dividend, divisor);
    cout<<x<<endl;

}

int divide(int dividend, int divisor) {
    // int c = ;
    if (dividend == INT_MIN && divisor == -1) {
        return INT_MAX;
    }
    else {
        return dividend / divisor;
    }
    
}