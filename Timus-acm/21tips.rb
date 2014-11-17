#21tips

# 2 shortcut for array # join
[1,2,3] * 1 # => 

%w{this is a test} * "," # => 
h = {:name => "Fred", :age => 77 }
h.map {|i| i * "="} * "n" # => 

# 3 format decimal amounts quickly
money = 9.5
"%.2f" % money # => 

# 4 interpolate text quickly 
"[%s]" % "same old drag"  # => 

x = %w{p hello p}
"<%s>%s</%s>" % x  # => 

# 5 delete trees of files
# require ' fileutils'
# FileUtils.rm_r 'somedir'


# 6 exploding enumerables

a = %w{a b }
b = %w{c d}
[a + b ] # => 
[*a + b] # => 

a = %w{a b c d e f g h }
b = [0.5,6]
a.values_at(*b).inspect # => 

(z ||= [ ] )  << 'test' 
p z 

does = is = { true => "YES", false => "NO"}
p does[10==50] # =


year = 1972
puts  case year
        when 1970..1979: "Seventies"
        when 1980..1989: "Eighties"
        when 1990..1999: "Nineties"
      end


# 
%w{rubygems daemons eventmachine}.each { |x| require x }

# 17 see the whole of an exception's backtrace

def do_division_by_zero; 5 / 0; end
begin
  do_division_by_zero
rescue => exception
  puts exception.backtrace
end


#18 

[*items].each do |item|
  
end





#>  # !> possibly useless use of a constant in void context
# => 
# ~> -:40: syntax error, unexpected tIDENTIFIER, expecting keyword_then or ';' or '\n'
# ~> ...73954199_15087_379141 != %does[10==50].strip;      $stderr...
# ~> ...                               ^
# ~> -:40: Invalid char `\x03' in expression
# ~> -:40: syntax error, unexpected keyword_elsif, expecting '}'
# ~> ...3954199_15087_379141);    elsif [____xmp_1373954199_15087_37...
# ~> ...                               ^
# ~> -:40: syntax error, unexpected keyword_end, expecting '}'
# ~> ...199_15087_379141 + "]");    end;  };  nil;rescue Exception; ...
# ~> ...                               ^
# ~> -:40: syntax error, unexpected keyword_rescue, expecting '}'
# ~> ...+ "]");    end;  };  nil;rescue Exception;  nil;end || _xmp_...
# ~> ...                               ^
# ~> -:40: syntax error, unexpected keyword_end, expecting '}'
# ~> ... nil;rescue Exception;  nil;end || _xmp_1373954199_15087_379...
# ~> ...                               ^
# ~> -:40: syntax error, unexpected ')', expecting '}'
# ~> ... _xmp_1373954199_15087_379141;));.strip;      $stderr.puts(...
# ~> ...                               ^
# ~> -:40: Invalid char `\x03' in expression
# ~> -:40: syntax error, unexpected keyword_elsif, expecting '}'
# ~> ...3954199_15087_379141);    elsif [____xmp_1373954199_15087_37...
# ~> ...                               ^
# ~> -:40: syntax error, unexpected keyword_end, expecting '}'
# ~> ...199_15087_379141 + "]");    end;  };  nil;rescue Exception; ...
# ~> ...                               ^
# ~> -:40: syntax error, unexpected keyword_rescue, expecting '}'
# ~> ...+ "]");    end;  };  nil;rescue Exception;  nil;end || _xmp_...
# ~> ...                               ^
# ~> -:40: syntax error, unexpected keyword_end, expecting '}'
# ~> ... nil;rescue Exception;  nil;end || _xmp_1373954199_15087_379...
# ~> ...                               ^
# ~> -:40: syntax error, unexpected ')', expecting '}'
# ~> ... _xmp_1373954199_15087_379141;));# ~> -:36: syntax error, un...
# ~> ...                               ^
