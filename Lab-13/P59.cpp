//Name: Jericho Maniago
//Email: jericho.maniago49@myhunter.cuny.edu
//Date: November 28, 2022
//Asks for the users annual budget and estimated monthly expense. Then, prints out expense and remaing balance for each end of the month.

#include <iostream>
using namespace std;

int main()
{
    float budget, monExpense;
    cout << "Input your annual budget: ";
    cin >> budget;
    cout << "Input your month expense: ";
    cin >> monExpense;
    cout << "month\texpense\tremaining balance of budget\n";
    for(int i = 1;i <= 12;i++)
    {
        if(i == 7)
        {
            monExpense *= 1.15;
        }
        budget -= monExpense;
        printf("%5d\t%7.2f\t%27.2f\n", i, monExpense, budget);
    }
    if(budget < 0)
    {
        cout << "need higher budget";
    }
    return 0;
}