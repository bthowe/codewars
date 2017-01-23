#include <iostream>

std::string even_or_odd(int number)
{
    //int num = nb_petals%6;
    if (number%2 == 0)
    {
        return "Even";
    }
    else
    {
        return "Odd";
    }
}

int main()
{
    std::cout << even_or_odd(6);
    return 0;
}
