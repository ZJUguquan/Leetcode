module BinaryTree
  class Node
    attr_reader :word, :count, :left, :right
 
    include Enumerable
 
    def initialize(word)
      @word, @count = word, 1
    end
 
    def size  # length
      size = 1
      size += @left.size  unless left.nil?
      size += @right.size unless right.nil?
      size
    end
 
    def <<(another_one)
      case @word <=> another_one.word
        when 1
          insert_into(:left, another_one)
        when 0
          @count += 1
        when -1
          insert_into(:right, another_one)
      end
    end
 
    def each
      @left.each {|node| yield node } unless @left.nil?
      yield self
      @right.each {|node| yield node } unless @right.nil?
    end
 
    def words
      entries.map {|e| e.word }
    end
 
    def count_all
      self.map { |node| node.count }.reduce(:+)
    end
 
    def insert_into(destination, another_one)
      var = destination.to_s
      eval(%Q{
        if @#{var}.nil?
          @#{var} = another_one
        else
          @#{var}.insert(another_one)
        end
      })
    end
 
    protected :insert_into
  end
end

myn = Node.new("1")
a = [1, 7, 5, 21, 22, 27 ,25, 20, 10] 
Nodes = []
a.each {|e|  insert_into(myn ,Node.new(e.to_s) )}

p myn.size


=begin
#include <iostream>

using namespace std;

int a[5000],b[5000],k,n;

void rec(int x,int y)
{
    if (x<y) return;
    b[k]=a[x];
    k++;
    for(int i=x-1;i>=y;i--)
    if (a[i]<a[x])
    {
         rec(i,y);
         rec(x-1,i+1);
         return;
    }
    rec(x-1,y);
}

int main()
{
    cin>>n;
    k=0;
    for(int i=0;i<n;i++)
    cin>>a[i];
    rec(n-1,0);
    for(int i=n-1;i>=0;i--)
    cout<<b[i]<<" ";
    return 0;
}
=end