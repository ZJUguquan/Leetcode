# 1654  cipher message

s = gets.chomp!
one = 0; two = 1 ; pre = 0

0.upto(s.length-1).each do |i|
   
end

=begin  G ++ 
#include<iostream>
#include<string.h>
#include<deque>
#include<stdio.h>
using namespace std;
int main()
{
    string node;
    cin >> node;
    int one,two;
    one = 0;
    two = 1;
    int pre = 0;
    for(int i = 0;i < node.size();i++)
    {
        if(node[i] == '!')
        continue;
        if(node[i] == node[i+1])
        {
            node[i] = node[i+1] = '!';
            one = pre;
            if(i+2 < node.size())
            two = i+2;
            while(one> 0 && two < node.size())
            {
                while(one > 0 && node[one] == '!')
                one--;
                if(node[one] == node[two] )
                {
                    node[one] = node[two] = '!';
                    one--;two++;
                }
                else
                break;
            }
        }
        else
        pre = i;

    }

   for(int i = 0;i < node.size();i++)
   {
       if(node[i] != '!')
       cout << node[i];
   }

}
=end