# 1123 salary  huiwen palindrome

s = Array.new(1000,0)
def work(p)
   while s[p] == "9"
      s[p] = "0"
      p -= 1
   end
   s[p] 
 
cin = gets.chomp!

=begin
#include <iostream>

using namespace std;

char s[10000];
long long i,j;

void work (long p)
{
     while (s[p]=='9')
           {
           s[p]='0';
           p--;
           }
     s[p]=(char)((long)(s[p])+1);
     return;
}

int main ()
{
    cin>>s;
    for (i=0;i<((strlen(s))/2);i++)
        {
        j=strlen(s)-i-1;
        if (s[i]>=s[j]) {
                        s[j]=s[i];
                        }
                        else {
                             work (j-1);
                             s[j]=s[i];
                             }
        }
    cout<<s<<endl;
    return (0);
}
=end