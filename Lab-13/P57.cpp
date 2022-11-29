//Name: Jericho Maniago
//Email: jericho.maniago49@myhunter.cuny.edu
//Date: November 28, 2022
//Asks for number of credit hours and returns grade level.

#include <iostream>
using namespace std;

int main()
{
    int num;
    cout << "Enter number of credit hours taken: ";
    cin >> num;
    if(num < 28)
    {
        cout << "freshman";
    }
    else if(num < 61)
    {
        cout << "sophomore";
    }
    else if(num < 94)
    {
        cout << "junior";
    }
    else
    {
        cout << "senior";
    }
    return 0;
}