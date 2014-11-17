# 1112. Cover 
# max number 
# unintersect  interval 

n = 5


class Interval
   attr_accessor :left, :right, :lenth 
   attr_accessor :state 
   # 1 none intersect 
   # 2 have include
   # 3 have intersect
   #@lenth = @right  - @left 
   def initialize(left,right)
    @left= left ; @right = right
   end
   def lenth
    self.right - 
    self.left
  end
end
a  = []
1.upto(n).each {|e|
  x,y = gets.chomp!.split(" ").map(&:to_i)
  left = [x,y].min ; right = [x,y].max
  int = Interval.new(left,right)
  a << int
}

0.upto(n-1).each {|i|
  (i+1).upto(n) {|j|
    if a[i].left < a[j].left and a[i].right < a[i].right
      a.delete_at i  # interval i  include other
    end
    if a[i].right > a[j].left and a[i].left < a[j].right
      if (a[i].right - a[i].left) < (a[j].right -a[j].left )
        a.delete_at j
      else
        a.delete_at i
      end
    end

  }
}
a.each {|inte|
  puts 
  print "#{inte.left} #{inte.right}"
}











