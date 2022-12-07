//Name: Jericho Maniago
//Email: jericho.maniago49@myhunter.cuny.edu
//Date: December 06, 2022
//This program takes an int between -128 and 127, and returns the int as a binary string.

#include <iostream>
using namespace std;

int main() {
    int n, rem, num, size, len;
    cout << "Enter an int in [-128, 127]: ";
    cin >> n;
    num = n;
    if(num < 0) {
        num = (num * -1) - 1;
    }
    string result = "";
    while(num > 0) {
        rem = num % 2;
        result = to_string(rem) + result;
        num /= 2;
    }
    size = 8;
    len = result.length();
    for(int i = 0;i < size - len;i++) {
        result = "0" + result;
    }
    if(n < 0) {
        for(int i = 0;i < result.length();i++) {
            if(result[i] == '0') {
                result[i] = '1';
            }
            else {
                result[i] = '0';
            }
        }
    }
    cout << "binary string: " + result;
    return 0;
}