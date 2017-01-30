#include <iostream>
#include <vector>
using namespace std;

string sumLength(std::vector<int> v)
{
    int sum = 0;
    int neg_count = 0;
    int zero_count = 0;
    for (int i = 0; i<v.size(); i++)
        if (v[i]>0)
            sum+=v[i];
        else if (v[i]<0)
            neg_count+=1;
        else
            if (zero_count%2==0)
            {
                neg_count+=1;
                zero_count+=1;
            }
            else
                zero_count+=1;
    std:string s = std::to_string(sum) + " " + std::to_string(neg_count);
    return s;
}

int main()
{
    std::cout << sumLength({-1, 2, 3, 4, 0, 1, 0, -2, 0, -3});
    return 0;
}
