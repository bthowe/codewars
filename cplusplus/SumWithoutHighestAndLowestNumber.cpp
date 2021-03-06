#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int sum(vector<int> numbers)
{
    //for (std::vector<int>::const_iterator i = numbers.begin(); i != numbers.end(); ++i)
    //    std::cout << *i << ' ';

    if (numbers.empty())
    {
        return 0;
    }
    else if  (numbers.size() == 1)
    {
        return 0;
    }
    else
    {
        int min_num = *(std::min_element(numbers.begin(), numbers.end()));
        int max_num = *(std::max_element(numbers.begin(), numbers.end()));

        int sum_of_elems = 0;
        for(std::vector<int>::iterator it = numbers.begin(); it != numbers.end(); ++it)
            sum_of_elems += *it;

        return sum_of_elems - min_num - max_num;
    }

}

int main()
{
    std::cout << sum({ });
    return 0;
}
