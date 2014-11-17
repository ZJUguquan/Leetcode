/*
 * ACM Timus Online Judge Contest 15 October 2011
 * Problem H - New Year Cruise
 */


 def max(a,b)
    return a > b ? a : b 
 end
 arr = Array.new(n){}
 n = gets.chomp!.to_i
 0.upto(n-1).each {|i|
    arr[i] = gets.chomp!.split(" ").map(&:to_i)
 }
 0.upto(n-1).each {|i|
    0.upto(n-1).each {|j|
       if arr[i][j]  == 0
          next
       end
       
       # vladi - > moscow
       if (i<j and j-i > 1)
          i.upto(j-1).each {|k|
             arr[k][k+1] += arr[i][j]
          }
   }
}

                        if (i < j && j - i > 1)
                        {
                                for (k = i; k < j; k++)
                                {
                                        A[k][k + 1] += A[i][j];
                                }
                        }
                        // Moscow -> Vladi
                        else if (i > j && i - j > 1)
                        {
                                for (k = i; k > j; k--)
                                {
                                        A[k][k - 1] += A[i][j];
                                }
                        }
                };


        // get maximum for each pair of stations
        max = 0;
        for (i = 0; i < N - 1; i++)
        {
                if (MAX(A[i][i + 1], A[i + 1][i]) > max)
                {
                        max = MAX(A[i][i + 1], A[i + 1][i]);
                }
        }

        if (max % 36 == 0)
                max /= 36;
        else
                max = 1 + max / 36;
        printf("%d", max);

        return 0;
}