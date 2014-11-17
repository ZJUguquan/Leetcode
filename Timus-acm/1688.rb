# 1688

n,m = gets.chomp!.split(" ").map(&:to_i) ; s=0; exit = 3* n; 

if m == 0
   puts "Team.GOV!"   
else
   1.upto(m).each  {|e|
      t = gets.chomp!.to_i
      s += t 
      
   if s > exit   
      puts "Free after #{e} times."
      break; 
   end
   }
   puts "Team.GOV!" if s <= exit
       
end