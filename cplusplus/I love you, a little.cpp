#include <iostream>

std::string how_much_i_love_you(int nb_petals)
{
    int num = nb_petals%6;
    if (num == 0)
    {
        return "not at all";
    }
    else if (num == 1)
    {
        return "I love you";
    }
    else if (num == 2)
    {
        return "a little";
    }
    else if (num == 3)
    {
        return "a lot";
    }
    else if (num == 4)
    {
        return "passionately";
    }
    else
    {
        return "madly";
    }
}

//alternatively
/*
std::string how_much_i_love_you(int nb_petals)
{
    string arr[] = {"I love you", "a little", "a lot", "passionately", "madly", "not at all"};
    return arr[(nb_petals - 1) % 6];
}
*/

int main()
{
    std::cout << how_much_i_love_you(7);
    return 0;
}
