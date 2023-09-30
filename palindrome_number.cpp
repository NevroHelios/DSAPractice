#include <bits/stdc++.h>
using namespace std;

bool isPalindrome(int x);

int main() {
        // x is your var
        int x = 123321;
        bool res = isPalindrome(x);
        cout<<res;
        // for true returns 1
        // for false returns 0

}
bool isPalindrome(int x) {
    if (x < 0) return false;
    int temp = x;
    long int b = 0;
    while (temp != 0) {
        b = (b * 10) + (temp % 10);
        temp /= 10;        
    }
    return (x == b);
};