# 1777 Anindilyakwa
a= (gets.chomp!.split(" ").map(&:to_i)).sort
def diff_min(a)
   res = []
   0.upto(a.length - 2) {|i|
      (i+1).upto(a.length - 1) { |j|
         a[i] > a[j] ? res << a[i] - a[j] : res << a[j] - a[i]  
      }
   }
   res.min
end
def diff_step(a,i)
   i = 0
   while diff_min(a) > 0
      a << diff_min(a)
      i +=1
   end
   i + 1
end
#p diff_min([11,5,9])
p diff_step(a,0)


# input 11 5 9  instinct out : 3