#include <iostream>
#include <cmath>

using namespace std;

class ASum
{
public:
    static long long findNb(long long m);
};

long long ASum::findNb(long long m)
{
    long long i = 0;
    while ((m>0))
    {
        i++;
        m += -i * i * i;
    }
    if (m==0)
        return i;
    else
        return -1;
}

int main()
{
    std::cout << ASum::findNb(4183059834009) << "\n";
    return 0;
}
