#include <iostream>
#include <sstream>
#include <string>
#include <vector>
using namespace std;

int find_rev_rec(std::vector<int> arr, int len) {
    if (len >= 0) {
        cout<<arr[len]<<" ";
        return find_rev_rec(arr, len-1);
    }
    return 0;
}

void find_rev_itr(vector<int> arr, int len) {
    cout<<"Reverse of the array from Iteration is: ";
    for (int i = len; i >= 0; i--) {
        cout<<arr[i]<<" ";
    }
}

int main()
{
    std::string line;
    int number;
    std::vector<int> arr;
    std::cout << "Enter numbers separated by spaces: ";
    std::getline(std::cin, line);
    std::istringstream stream(line);
    while (stream >> number)
        arr.push_back(number);

    int len = arr.size() - 1;
    find_rev_itr(arr, len);
    cout<<endl<<"Reverse of the array from Recursion is: ";
    find_rev_rec(arr, len);
    return 0;
}
