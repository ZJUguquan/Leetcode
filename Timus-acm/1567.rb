# 1567  SMS-spam 

s = "pokupaite gvozdi tolko v kompanii gvozdederov i tovarischi"
a=s.each_char.to_a # => ["p", "o", "k", "u", "p", "a", "i", "t", "e", " ", "g", "v", "o", "z", "d", "i", " ", "t", "o", "l", "k", "o", " ", "v", " ", "k", "o", "m", "p", "a", "n", "i", "i", " ", "g", "v", "o", "z", "d", "e", "d", "e", "r", "o", "v", " ", "i", " ", "t", "o", "v", "a", "r", "i", "s", "c", "h", "i"] # !> assigned but unused variable - a



=begin


#include<cstdio>
int main()
{
    int s=0,a;
    for(;(a=getchar())!='\n';(a==' ')?s++:(a%3==0)?s+=3:s+=a%3);
    printf("%i",s);
    return 0;
}


=end
