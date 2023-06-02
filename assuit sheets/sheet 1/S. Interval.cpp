#include <iostream>

using namespace std;



int main()
{
    string groups[5] = {"Interval [0,25]", "Interval (25,50]", "Interval (50,75]", "Interval (75,100]","Out of Intervals"};
    int group;
    double number;
    cin >> number;

    for(int i = 0;i<4;i++){
        if(number >= 0 && number<= 25)
            group = 0;
        else if(number > 25 && number<= 50)
            group = 1;
        else if(number > 50 && number<= 75)
            group = 2;
        else if(number > 75 && number<= 100)
            group = 3;
        else
            group = 4;
    }

    cout<<groups[group];

}

