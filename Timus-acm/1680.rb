# # 1680
# y, n , q = gets.chomp!.split(" ").map(&:to_i)
# daiding=[] ; h = {} ; pmark = 0 ; input=[]
# 1.upto(n).each {|k|
#     line = gets.chomp!
#     univ, mingci = line.split("#")
#    if  mingci.nil? or !h.keys.include? univ
#          daiding << line  ;  pmark += 1;       h[univ] = pmark; 
#    end
# }   
# 
# 
# puts daiding[q]
# 
# # puts h.key(q+1)
# #puts daiding[q+1]
# #p pmark
# 
#    # 
#    # 1999 10 6
#    # St Petersburg SU #1
#    # Belarusian SU #1
#    # Moscow SU #4
#    # Southern Ural SU
#    # Moscow SU #1
#    # Novosibirsk SU #1
#    # St Petersburg SU #3
#    # Belarusian SU #3
#    # St Petersburg IFMO #1
#    # Ural SU #3
#    
#    Ural 1999年取得了第10. 距离进入决赛 相差6分钟时间惩罚.
#    2006年 资格最后一名和无资格的第一名相差4分钟. 
# 
#    地区有q个名额代表参赛.  根据规则, 来自于相同大学的两个代表队不能同时进入决赛. 
#    如果出现情况, 两队中的成绩差者被淘汰. 
#    成绩排名第q+1. 称作 第一名无资格. 如果这一地区再增加一个名额, 它能进入决赛. 
# 
#    y year 
#    n  teams  <=201
#    q 3-12
# 
#    接下来n行 大学名, 成绩
#    求这只 "第一名无资格"