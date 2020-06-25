#include <iostream>
#include <sstream>
#include <string>
#include <vector>
using namespace std;
int indx=0;
int res_indx = 0;

int find_minnum_rec(vector<int> arr, int &min) {
    if (min > arr[0]) {
            min = arr[0];
            res_indx = indx;
    }
    if (arr.size() == 1){
        std::cout<<"At index: "<<res_indx+1;
        return min;
    }
    arr.erase(arr.begin());
    indx = indx + 1;
    find_minnum_rec(arr, min);
}

void find_minnum_itr(vector<int> arr, int min) {
    for (int i = 0; (unsigned)i < arr.size(); i++) {
        if (min > arr[i]) {
            min = arr[i];
            indx = i+1;
        }
    }
    std::cout<<"Min number is: "<<min;
    std::cout<<" at index: "<<indx<<endl;
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

    int min = arr[0];
    if (arr.size() > 1) {
        std::cout<<"Find min with iteration...\n";
        find_minnum_itr(arr, min);
        indx = 0;
        std::cout<<"Find min with recursion...\n";
        find_minnum_rec(arr, min);
    }
    std::cout<<" min number is: "<<min;
    return 0;
}
