# ACM 1026  questions and answers
# 

#1.upto(5).each{|i| puts i*i }
n=gets.chomp.to_i
input =  Array.new(n,0)#[7,121,123,7,121]
1.upto(n).each {  input << gets.chomp.to_i }
input_sorted= input.sort
separate = gets.chomp
#p input_sorted 
queries_count =  gets.chomp.to_i 
queries = Array.new(queries_count , 0)
1.upto(queries_count).each {  queries << gets.chomp.to_i }

0.upto(queries.length-1).each {|i|
  puts  input_sorted[queries[i]-1]
}
