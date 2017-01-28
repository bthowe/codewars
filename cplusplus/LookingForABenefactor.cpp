#include <iostream>
#include <vector>
//#include <numeric>
#include <stdexcept>
#include <math.h>
using namespace std;

class NewAverage
{
public:
   static long long newAvg(std::vector<double> &arr, double navg);
};

long long NewAverage::newAvg(std::vector<double> &arr, double navg)
{
    float sum = 0;
    for (int i = 0; i<arr.size(); i++)
    {
        sum+=arr[i];
//        std::cout << arr[i] << ",";
    }

//    std::cout << "\n" << sum << "\n";
    long long num = ceil(navg*(arr.size()+1) - sum);
//    std::cout << "\n" << ceil(num) << "\n";
    if (num>0)
        return num;
    else
        throw std::logic_error("");
}

int main()
{
//    std::vector<double> arr1 = {1753,1445,522,964,923,381,1175,684,1204,1286,786,742,590,1422,420,526,1533,1294,1043,454,792,1648,1361,1124,520,1368,1678,1371,1045,1401,284,1107,551,1172,930,462,785,905,261,868,1773,1154,686,1387,1805,480,467,1304,955,1218,1874,249,1286,1669,940,195,1533,1156,1044,356,1363,1485,611};
    std::vector<double> arr1 = {1400.25,30000.8,5.56,7,9,11,15.48,120.98};
    std::cout << NewAverage::newAvg(arr1, 10000);
    return 0;
}
