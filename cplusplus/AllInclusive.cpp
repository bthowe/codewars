#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

class Rotations
{
public:
    static bool containAllRots(const std::string &strng, std::vector<std::string> &arr);
};

bool Rotations::containAllRots(const std::string &strng, std::vector<std::string> &arr)
{
    int l = strng.size();
    std::string s;
    std::vector<std::string> v(strng.size());
    for (int i = 0; i<strng.size(); i++)
    {
        s = "";
        for (int j = 0; j<strng.size(); j++)
        {
            s+=strng[(i+j)%l];
        }
        v[i] = s;
    }

    bool all_in = true;
    bool in = false;
    for (int i = 0; i<v.size(); i++)
    {
        in=false;
        for (int j = 0; j<arr.size(); j++)
        {
            if (v[i]==arr[j])
                in=true;
        }
        if (!in)
            all_in=false;
    }
    return all_in;
}

int main()
{
    std::string s1 = "bsjq";
    std::vector<std::string> v1 = {"bsjq", "qbsj", "sjqb", "twZNsslC", "jqb"};
    bool b;
    b = Rotations::containAllRots(s1, v1);
    std::cout << b;
    return 0;
}
