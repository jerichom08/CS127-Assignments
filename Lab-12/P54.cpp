//Name: Jericho Maniago
//Email: jericho.maniago49@myhunter.cuny.edu
//Date: November 28, 2022
//This program pints '10' 6 times in a row, for 10 rows.

#include <iostream>
using namespace std;

int main() 
{
    int i;
    for(i = 0; i < 10; i++)
    {
        int j;
        for(j = 0; j < 6; j++)
        {
            cout << "10";
        }
        cout << " \n";
    }
    return 0;
}