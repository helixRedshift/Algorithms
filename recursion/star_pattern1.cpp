#include <iostream>
#include <sstream>
#include <string>
using namespace std;

int print_star_pattern_rec(int n, int len) {
    for (int i = n; i <= len; i++)
        cout<<"*";
    cout<<"\n";
    if(n == 1)
        return 0;
    print_star_pattern_rec(n-1, len);
}

void print_star_pattern_itr(int n) {
    for (int i = 0; i < n; i++) {
        for (int j = 0; j <= i; j++)
            cout <<"*";
        cout <<"\n";
    }
}

int main()
{
    int n;
    std::cout << "Enter number of lines for the pattern: ";
    cin>>n;

    print_star_pattern_itr(n);
    print_star_pattern_rec(n, n);
    return 0;
}
