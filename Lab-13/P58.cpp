//Name: Jericho Maniago
//Email: jericho.maniago49@myhunter.cuny.edu
//Date: November 28, 2022
//Asks for an int and symbol and creates a right hand triangle.

#include <iostream>
using namespace std;

int main()
{
    int rows;
    char c;
    cout << "Enter an int: ";
    cin >> rows;
    cout << "Enter a symbol other than space: ";
    cin >> c;

    int i;
    for(i = 1; i <= rows; i++)
    {
        int j;
        for(j = rows - i; j > 0; j--)
        {
            if(i != rows)
            {
                cout << " ";
            }
        }
        int k;
        for(k = 1; k <= i; k++)
        {
            cout << c;
        }
        cout << "\n";
    }
    return 0;
}