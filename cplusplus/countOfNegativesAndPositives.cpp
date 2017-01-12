#include <vector>
#include <iostream>

std::vector<int> countPositivesSumNegatives(std::vector<int> input)
{
    for (auto const &element: input)
        std::cout << element << ' ';

    int neg = 0;
    int pos = 0;

    if (input.size()==0)
        return std::vector<int>{};

    else
        for (auto const &element: input)
            if (element>0)
                pos++;
            else if (element<0)
                neg+=element;
        std::vector<int> array { pos, neg};
        return array;

}

int main()
{
//    std::vector<int> array { 0, 1, 2, -3, 4, -5 };
    std::vector<int> array {};
    for (auto const &element: countPositivesSumNegatives(array))
        std::cout << element << ' ';
    return 0;
};
