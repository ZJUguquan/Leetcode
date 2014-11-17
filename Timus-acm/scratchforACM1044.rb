
 # p RUBY_VERSION
 
 # 6  55252
 $luck_6 = 0

 "000000".upto("999999").each {  |number|
   # value = number.to_i
    qian = number[0,3]
    hou = number[3,3]
    sumqian = 0
    sumhou = 0
    qian.each_char {|c| 
       sumqian += c.to_f
      }
   
    hou.each_char { |e|
       sumhou += e.to_f
    }  
    if sumqian == sumhou
       $luck_6 += 1
    end
 }

 puts $luck_6
 

 # "111111".upto("111120").each {|number|
 #    qian = number[0,3]
 #  hou = number[3,3]
 #  p qian
 #  p hou
 # }
 
 
=begin

 

=begin
 input = "237890" # !> assigned but unused variable - input
 qu = 237890 / 1000 # => 237

 sumpre = 0
 
 p "000000".next 
 
 
qu.to_s.each_char {|c| 
   sumpre += c.to_f
} 
p sumpre 
# ~> -:10:in `block in <main>': undefined method `+' for nil:NilClass (NoMethodError)
# ~> 	from -:10:in `each_char'
# ~> 	from -:10:in `<main>'
# >> "2.0.0"
=end