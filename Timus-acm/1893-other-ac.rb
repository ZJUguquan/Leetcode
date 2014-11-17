=begin
#include<iostream>
using namespace std;
int n;
char c;
int main()
{
cin>>n>>c;
if (n>=1 && n<=2)
{ if(c=='A')
cout<<"window";
if(c=='D')
cout<<"window";
if(c=='B')
cout<<"aisle";
if(c=='C')
cout<<"aisle";
}
if(n>=3 && n<=20)
{ if(c=='A')
cout<<"window";
if(c=='F')
cout<<"window";
if(c=='B')
cout<<"aisle";
if(c=='E')
cout<<"aisle";
if(c=='C')
cout<<"aisle";
if(c=='D')
cout<<"aisle";
}
if(n>=21 && n<=65)
{ if(c=='A')
cout<<"window";
if(c=='K')
cout<<"window";
if(c=='B')
cout<<"neither";
if(c=='C')
cout<<"aisle";
if(c=='D')
cout<<"aisle";
if(c=='E')
cout<<"neither";
if(c=='F')
cout<<"neither";
if(c=='G')
cout<<"aisle";
if(c=='H')
cout<<"aisle";
if(c=='J')
cout<<"neither";
}
return 0;
}
=end