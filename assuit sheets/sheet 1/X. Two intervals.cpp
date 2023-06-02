#include <iostream>

using namespace std;



int main()
{
   int l1,l2,r1,r2,n1,n2;
   cin >>l1>>r1>>l2>>r2;

   if(r1 < l2 || r2 < l1)
    cout <<-1;
   else{
    if(l2>=l1 && l2 <= r1)
    n1 = l2;
   else
    n1 = l1;

   if(r1 <= r2)
    n2 = r1;
   else
    n2 = r2;

cout << n1<<" "<<n2;
   }




}

