#include <iostream>
#include <sstream>
#include <string>
#include <vector>
using namespace std;
int indx=0;
int res_indx = 0;

int find_maxnum_rec(vector<int> arr, int &max) {
    if (max < arr[0]) {
            max = arr[0];
            res_indx = indx;
    }
    if (arr.size() == 1){
        std::cout<<"At index: "<<res_indx+1;
        return max;
    }
    arr.erase(arr.begin());
    indx = indx + 1;
    find_maxnum_rec(arr, max);
}

void find_maxnum_itr(vector<int> arr, int max) {
    for (int i = 0; (unsigned)i < arr.size(); i++) {
        if (max < arr[i]) {
            max = arr[i];
            indx = i+1;
        }
    }
    std::cout<<"Max number is: "<<max;
    std::cout<<" at index: "<<indx<<endl;
}

int main()
{
    std::string line;
    int number;
    //take inputs from user
    std::vector<int> arr;
    std::cout << "Enter numbers separated by spaces: ";
    std::getline(std::cin, line);
    std::istringstream stream(line);
    while (stream >> number)
        arr.push_back(number);

    int max = arr[0];
    if (arr.size() > 1) {
        std::cout<<"Find max with iteration...\n";
        find_maxnum_itr(arr, max);
        indx = 0;
        std::cout<<"Find max with recursion...\n";
        find_maxnum_rec(arr, max);
    }
    std::cout<<" max number is: "<<max;
    return 0;
}

