class BinaryTree
    include Enumerable      
   attr_accessor :value
      def initialize( value = nil )
         @value = value
      end 
      
     def each # visit
         return if self.nil?         
         yield self.value
         self.left.each( &block ) if self.left
         self.right.each( &block ) if self.right     
     end
 
     def empty?
         # code here
     end
         
     def <<( value ) # insert
         return self.value = value if self.value == nil
         test = self.value <=> value
         case test
             when -1, 0
                 @right = BinaryTree.new if self.value == nil
                 self.right << value
             when 1 
                 @left = BinaryTree.new if self.value == nil
                 self.left << value
         end
     end     # <<
  end
  
  bt = BinaryTree.new
a = [1, 7, 5, 21, 22, 27 ,25, 20, 10] 
a.each {|e| bt << a}
p bt 
=begin
module BinaryTree
  class Node
    attr_reader :word, :count, :left, :right
 
    include Enumerable
 
    def initialize(word)
      @word, @count = word, 1
    end
 
    def size
      size = 1
      size += @left.size  unless left.nil?
      size += @right.size unless right.nil?
      size
    end
 
    def insert(another_one)
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
=end