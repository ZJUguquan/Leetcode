# 1349
# var n:integer;begin readln(n);
# case n of 0,3..200:writeln('-1');1:writeln('1 2 3');
# 2:writeln('3 4 5');end;end.

n = gets.chomp!.to_i
case n 
when 0,3..100 
   puts "-1"
when 2
   puts "3 4 5"
else
   puts "1 2 3"
end