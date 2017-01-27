#include <iostream>
#include <vector>
#include <algorithm>

std::string twoSort(std::vector<std::string> s)
{
    int SIZE = s.size();
    std::sort(s.begin(), s.end());
    std::string str = s[0];

    std::string new_str;
    new_str = str[0];
    for (int i = 1; i < str.size(); ++i)
    {
        new_str+="***";
        new_str+=str[i];
    }
    return new_str;
}

int main()
{
    std::cout << twoSort({ "bitcoin", "take", "over", "the", "world", "maybe", "who", "knows", "perhaps" }) << "\n";
    return 0;
}
