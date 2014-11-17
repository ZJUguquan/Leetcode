# 1413  mars jumper
# 8 north   2 south  6 east  7 north-west ,  
# 5 , take a sample of soil   0  selft-destroyed

# know input. keys sequence
# where to find it ? 
scale = 0.70710678118654752440084436210485
class String
  def remove(index)
    self[0..index-1] + self[index+1 .. self.length-1]
  end
  
  def sselfclean(a,b)
     # if self.include? (a)  and self.include?(b)
        s = self.remove(self.index(a))
        s = s.remove(s.index(b))
     # end
     s
  end
end

s = "123698741236987023"
zero = s.index("0")
p s.length
s = s[0..zero-1]
s = s.delete("5")
while s.include?("1") and s.include? ("9")
   s = s.sselfclean("1","9")
end
while s.include?("2") and s.include? ("8")
   s = s.sselfclean("2","8")
end
while s.include?("4") and s.include? ("6")
   s = s.sselfclean("4","6")
end
while s.include?("3") and s.include? ("7")
   s = s.sselfclean("3","7")
end
p s


=begin
#include <stdio.h>

double X, Y;
#define rad2    0.70710678118654752440084436210485

int main()
{
    char ch;

    X = Y = 0;

    while (scanf("%c", &ch) == 1 && ch != '0')
    {
        switch (ch)
        {
            case '1': X -= rad2; Y -= rad2; break;
            case '2': Y--; break;
            case '3': X += rad2; Y -= rad2; break;
            case '4': X--; break;
            case '6': X++; break;
            case '7': X -= rad2; Y += rad2; break;
            case '8': Y++; break;
            case '9': X += rad2; Y += rad2; break;
        }
    }
    printf("%.10lf %.10lf\n", X, Y);

    return 0;
}
=end

      