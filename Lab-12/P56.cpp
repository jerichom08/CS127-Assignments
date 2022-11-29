//Name: Jericho Maniago
//Email: jericho.maniago49@myhunter.cuny.edu
//Date: November 28, 2022
//Asks for two integers and prints even numbers between them.

#include <iostream>
using namespace std;

int main()
{
    int start, end;
    cout << "Enter start: ";
    cin >> start;
    cout << "Enter end: ";
    cin >> end;
    
    int i;
    for(i = start; i <= end; i++)
    {
        if(i % 2 == 0)
        {
            cout << i;
            cout << "\n";
        }
    }
    return 0;
}