#include <iostream>
#include <algorithm>
using namespace std;

class TwoToOne
{
public:
    static std::string longest(const std::string &s1, const std::string &s2);
};

std::string TwoToOne::longest(const std::string &s1, const std::string &s2)
{
    std::string letters;
    letters = s1[0];

    bool in;
    for (int i = 0; i<s1.size(); i++)
    {
        in = false;
        for (int j = 0; j<letters.size(); j++)
        {
            if (s1[i]==letters[j])
                in = true;
        }
        if (!in)
            letters+=s1[i];
    }
    for (int i = 0; i<s2.size(); i++)
    {
        in = false;
        for (int j = 0; j<letters.size(); j++)
        {
            if (s2[i]==letters[j])
                in = true;
        }
        if (!in)
            letters+=s2[i];
    }
    std::sort(letters.begin(), letters.end());
    return letters;
}

int main()
{
    std::cout << TwoToOne::longest("hey", "you");
    return 0;
}
