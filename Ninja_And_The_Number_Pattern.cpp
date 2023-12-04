#include <stdio.h>
#include <iostream>
#include <algorithm>
using namespace std;
int main()
{
    int n = 4;
    
    for (int i = 0; i < (int)(2*n-1)/2; i++){
        for (int j = 0; j < (int)(2*n-1)/2; j++){
            cout<<std::max(n-i, n-j);
        }
        for (int j = (int)(2*n-1)/2; j > -1; j--){
            cout<<std::max(n-i, n-j);
        }
    cout<<endl;
    }
    
    for (int i = (int)(2*n-1)/2; i > -1; i--){
        for (int j = 0; j < (int)(2*n-1)/2; j++){
            cout<<std::max(n-i, n-j);
        }
        for (int j = (int)(2*n-1)/2; j > -1; j--){
            cout<<std::max(n-i, n-j);
        }
    cout<<endl;
    }
}

/*

4444444
4333334
4322234
4321234
4322234
4333334
4444444
*/