#include <iostream>
 #include <cstdio>
 #include <cstring>
 #include <functional>
 #include <algorithm>
 using namespace std;
 int n, p;
 int count(int *a, int val)                              
 {
     int num = 0;
     for (int i = 0; i < n; ++i)
         if (a[i] <= val && a[i] != 0)
             ++num;
     return num;
 }
 void asign(int *a, int val)                         
 {
      for (int i = 0; i < n; ++i)
          if (a[i] <= val)      
             a[i] = 0;
 }
 int main()
 {
     while (scanf("%d %d", &n, &p)!= EOF)
     {
     int a[n];
     for (int i = 0; i < n; ++i)
         scanf("%d", &a[i]);
     std::sort(a, a + n, greater<int>());               
     int sum = 0, magic_num = 0;                           
     int t = -1;                                        
     while (1)
     {
             
         for (int i = 0; i < n; ++i)
         {
             int cnt = count(a, a[i]);
             if (a[i] != 0 && a[i] * cnt <= p)           
             {
                 sum += cnt;
                 asign(a, a[i]);
                 ++magic_num;
             }
                 while (a[i] == a[i+1] && i < n)       
                     ++i;
         }
         if (t == sum)                                  
            break;
         t = sum;
     }
     printf("%d %d\n", sum, magicn);
 }
    // system("pause");
     return 0;
 }