#include <iostream>
#include <vector>
using namespace std;

std::vector<int> digitize(unsigned long n)
{
    std::cout << std::to_string(n);
    std::cout << "\n";
    std::string s;
    if ((int)n<0)
    {
        s = std::to_string(-(int)n);
    }
    else
    {
        s = std::to_string((int)n);
    }

    int l = s.length();
    std::vector<int> s_array(l);

    for(int i = 0; i<l; i++)
    {
        s_array[i] = (int)s[l - i - 1] - 48;
    }

    return s_array;
}

int main()
{
    std:vector<int> yo = digitize(-1481746336);
    int l = yo.size();
    for(int i = 0; i<l; i++)
    {
        std::cout << yo[i];
    }
    return 0;
}
