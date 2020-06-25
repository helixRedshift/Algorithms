#include <iostream>
#include <sstream>
#include <string>
using namespace std;

int print_space(int n1) {
    if (n1 == 0)
        return 0;
    cout<<" ";
    print_space(n1 - 1);
}

int print_star(int n2) {
    if (n2 == 0)
        return 0;
    cout<<"* ";
    print_star(n2 - 1);
}

int print_star_pattern_rec(int n, int len) {
    int len2 = 2*n - 1;
    int len3 = 2*(len - n) - 1;
    if (n == 0)
        return 0;
    print_space(len2);
    print_star(len3);
    cout<<"\n";
    print_star_pattern_rec(n-1, len);
}

void print_star_pattern_itr(int n) {
    int n2 = n;
    for (int i = 1; i <= n; i++) {
        for (int j = 1; j < (2*n2); j++) 
            cout<<" ";
        n2--;
        for (int j = 1; j < (2*i); j++)
            cout <<"* ";
        cout <<"\n";
    }
}

int main()
{
    int n;
    std::cout << "Enter number of lines for the pattern: ";
    cin>>n;
    
    int len = n+1;
    print_star_pattern_itr(n);
    print_star_pattern_rec(n, len);
    return 0;
}
