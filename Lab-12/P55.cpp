//Name: Jericho Maniago
//Email: jericho.maniago49@myhunter.cuny.edu
//Date: November 28, 2022
//Asks user for temperature in Celsius and converts it to Fahrenheit.

#include <iostream>
using namespace std;

int main()
{
    double temp;
    cout << "Enter temperature in Celsius: ";
    cin >> temp;
    temp *= 9.0/5;
    temp += 32;
    cout << temp;
    return 0;
}