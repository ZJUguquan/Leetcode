# 1727  znika's magic numbers

#k = gets.chomp!.to_i

a = Array 1..9999


def countsumdigt(s)
   a = s.to_s.each_char.map(&:to_i) 
   return a.inject(:+)
end

p countsumdigt 12

=begin 
using System;
using System.Linq;
using System.Collections.Generic;
 
// http://acm.timus.ru/problem.aspx?space=1&num=1727
static class Timus
{
  static void Main()
  {
    var n = int.Parse(Console.ReadLine());
    var set = Compute(ref n);
    var count = set.Count;
    for (var i = 0; n > 9; i++, n -= 10) count++;
    var tens = count - set.Count;
    Console.WriteLine(count += ((n > 0) ? 1 : 0));
    foreach (var i in set) Console.Write(i + " ");
    while (tens-- > 0) Console.Write("19 28 37 46 ".Substring(tens * 3, 3));
    if (n > 0) Console.Write(n);
    Console.WriteLine();
  }
   
  static HashSet<int> Compute(ref int n)
  {
    var set = new HashSet<int>();
    for (var rand = new Random(); n >= 45; )
    {
      var k = rand.Next(100, 100000);
      if (set.Add(k)) n -= k.ToString().Select(x => x - '0').Sum();
    }
    return set;
  }
}
=end

