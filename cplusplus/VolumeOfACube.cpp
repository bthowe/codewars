#include <iostream>

double getVolumeOfCubiod(double length, double width, double height)
{
  return length*width*height;
}

int main()
{
    std::cout << getVolumeOfCubiod(10, 10, 10);
    return 0;
}
