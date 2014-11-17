# 1881 Long problem statement

h,w,n = gets.chomp!.split(" ").map {|x| x.to_i }
i = -1 ; lines = 0

1.upto(n).each do |s|
   # iterate  every word.   
   s = gets.chomp!
   len = s.length    #  demostrate its len
   lines += (i==-1 ? 1 : 0)
   # what is i ? 
   
   if (i + 1 + len == w )
      i = -1 # to next line.  ( next turn lines + 1)
   else
      if (i + 1 + len < w)   # short words 
         i = i + 1 + len    # still in this line 
      else  # > w 
         i = (i+len)==w ? -1 : len
         lines += 1
      end
   end
end

printf "%d", lines/h + (lines%h ==0 ? 1: 0)
         
   
   
# 
# line = 1; start = 0 ; paper = 1; word = n; symbol = w ;right = 0
 
#    # cursor start   a : cursor ends : 
#    if (start ==0) 
#       a = s.size() # new string length   s1:  <= limit ; s2 : > limit  
#    else
#       a = s.length + 1
#    end
#    if (start + a) < w
#       start = start + a   # this 
#    else
#       start = 0
#       line ++
#       
# end
# 


=begin
#include<iostream>
#include<string>
using namespace std;
int main(){
    int line=1,liner,start=0,paper=1,word,symbol;
    cin>>liner>>symbol>>word;
    for(int i=0;i<word;i++){
            string s;
            cin>>s;
            int a;
            if(start==0) a=s.size();
            else a=s.size()+1;
            if((start+a)<symbol)  start=start+a;
            else {
                 start=0;
                 line++;}
                 }
    if(line%liner==0) cout<<(line/liner);
    else cout<<(line/liner+1);
    system("pause");
    return 0;
}
=end


# lines on a page,   number of symbols in a line , number of words in the problem statement 
#
# n lines : one word per line 
# length of each word  , at most w 

# to figure out  the pages 

