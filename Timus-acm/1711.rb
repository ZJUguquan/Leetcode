# 1711 code names
def wholarge(last, this) 
   last = last.sort ; this = this.sort; lastmin = last.min
   if this.min > last.min 
      return this.min
   elsif this[1] > last.min
      return this[1]
   elsif this[2] > last.min
      return this[2]
   else
      return "-1"
   end
end
      
     
   # problems number    
n = gets.chomp!.to_i  ;ma = []; 
1.upto(n).each {|i|   ma << temp = gets.chomp!.split(" ").sort   }
orders = gets.chomp!.split(" ").map(&:to_i)
ever_mins = [] ; newma=[]
1.upto(n).each {|index| newma << ma[orders[index-1]-1] }
ever_mins << newma[0].min  ; 
# p newma   # 
# newma.each_with_index {|e,index| print "\n #{index}  e.min : #{e.min}\n"}

1.upto(n-1).each {|i|  
   puts "last min:#{newma[i-1].min}"
   puts "this min: #{newma[i].min}"
   ever_mins << wholarge(newma[i-1],newma[i])
 }

 p ever_mins
 # if ever_mins.include?("-1") 
 #   puts "IMPOSSIBLE"
 # else
 #   ever_mins.each {|ev| puts ev }
 # end
 # 
 
=begin
number 2: (names, codenames, codes)
number 1:  (cipher, grille, kamkohob)
number 7: on the third (!!!) place there should be the task number 7 (keywords, subversion, commands)
number 10: on the 4th (!!!) place there should be the task number 10 (mnemonic, palindromes, bestname

order = [] ; order[0]= 0
outputorders = gets.chomp!.split(" ").map(&:to_i)
order += outputorders
p order
out = []

1.upto(n).each {|index|
   this_row = order[index]
   if index == 1
      out << problems[order[1]].min
   else
      last_row = order[index-1]
      res = nearlarger(problems[last_row], problems[this_row])
      if res == 1000
         puts "Impossible"
         break
      else
         out << res
      end
   end
                
}
out.each {|o| puts o}

=end