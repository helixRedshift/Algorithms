#include <iostream>
#include <sstream>
#include <string>
#include <vector>
using namespace std;
int sum = 0;

int find_sum_rec(std::vector<int> arr) {
    if (arr.size() == 2){
        sum = arr[0] + arr[1];
        return sum;
    }
    if (arr.size() == 1)
        return arr[0];
    
    int first_elem = arr[0];
    arr.erase(arr.begin());
    return (first_elem + find_sum_rec(arr));
}

void find_sum_itr(vector<int> arr) {
    int sum = 0;
    for (int i = 0; (unsigned)i < arr.size(); i++) {
        sum += arr[i];
    }
    std::cout<<"Sum of the array from Iteration: "<<sum<<endl;;
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

    find_sum_itr(arr);
    std::cout<<"Sum of the array from Recursion: "<<find_sum_rec(arr);
    return 0;
}
