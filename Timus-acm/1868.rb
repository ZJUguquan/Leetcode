# 1868   prediction contest
names = []; real = {}
1.upto(12).each {|i| names << gets.chomp!}

names.each_with_index {|e,index|
   case index
   when   0..3
      real[e] = "gold"
   when 4..7
      real[e] = "silver"
   else 
      real[e] = "bronze"
   end 
}

number = gets.chomp!.to_i
numbers = Array.new(number,0)

h = {}
#participants = Array.new(number){Array.new(number,0)}
0.upto(number-1).each {|block|
   #participants[block-1] <<
   n_temp = gets.chomp!.to_i
   
   1.upto(n_temp).each {|index|
      name, predict = gets.chomp!.split(" : ")
      numbers[block] +=1 if real.select{|k,v| v==predict }.include?(name)
   }
}
#p real
p numbers

if numbers.max == 0
   puts 0
else
 puts 5*(numbers.count(numbers.max))
end



=begin
Zhejiang_U
U_of_Michigan_at_Ann_Arbor
Tsinghua_U
St._Petersburg_SU
Nizhny_Novgorod_SU
Saratov_SU
Friedrich_Alexander_U
Donetsk_National_U
Jagiellonian_U_in_Krakow
Moscow_SU
Ural_SU
U_of_Waterloo
3
6
Moscow_SU : gold
St._Petersburg_SU_of_ITMO : gold
Warsaw_U : gold
Tsinghua_U : gold
Nizhny_Novgorod_SU : silver
Saratov_SU : silver
6
Warsaw_U : gold
Saratov_SU : gold
Tsinghua_U : gold
Donetsk_National_U : silver
St._Petersburg_SU_of_ITMO : silver
Ural_SU : bronze
5
Zhejiang_U : gold
Tsinghua_U : gold
Shanghai_Jiao_Tong_U : gold
Fudan_U : gold


**
=end



=begin
other ac

#include <iostream>
#include <string>
#include <cstring>
#include <cstdio>
#include <map>
using namespace std;

map<string,string> m;

int main()
{
    //freopen("1.in","r",stdin);
    string str;
    for(int i=1;i<=4;i++)
    {
        cin>>str;
        m[str]="gold";
    }
    for(int i=1;i<=4;i++)
    {
        cin>>str;
        m[str]="silver";
    }
    for(int i=1;i<=4;i++)
    {
        cin>>str;
        m[str]="bronze";
    }
    int n,sum=0,qt=0;
    cin>>n;
    while(n--)
    {
        string s1,s2,s3;
        int t;
        cin>>t;
        int cnt=0;
        for(int i=0;i<t;i++)
        {
            cin>>s1>>s2>>s3;
            if(m[s1]==s3) cnt++;

        }
        if(sum<cnt)
        {
            sum=cnt;
            qt=1;
        }
        else if(sum==cnt)
        {
            qt++;
        }

    }
    cout<<qt*5<<endl;

    return 0;
}
=end