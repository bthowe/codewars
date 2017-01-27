#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int min(vector<int> list){
    auto result = std::min_element(list.begin(), list.end());
    return *result;
}

int max(vector<int> list){
    auto result = std::max_element(list.begin(), list.end());
    return *result;
}

int main()
{
    std::cout << min({-52, 56, 30, 29, -54, 0, -110});
    std::cout << max({4,6,2,1,9,63,-134,566});
    return 0;
}
