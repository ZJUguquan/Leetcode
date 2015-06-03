class Solution:
    # @param {integer} m
    # @param {integer} n
    # @return {integer}
    def uniquePaths(self, m, n):
        if m ==1 or n == 1:
            return 1
        if m == 2:
            return n
        if n == 2:
            return m

        maps = [ [0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if i == j == 0:
                    maps[i][j] = 1
                elif i == 0 and j > 0:
                    maps[i][j] = maps[i][j-1]
                elif i > 0 and j == 0:
                    maps[i][j] = maps[i-1][j]
                else:
                    maps[i][j] = maps[i-1][j] + maps[i][j-1]
        return maps[m-1][n-1]


s =Solution()
print s.uniquePaths(23, 12)


# public class Solution {
#     public int uniquePaths(int m, int n) {
#         int[][] map = new int[m][n];
#         for(int i = 0; i<m; i++) {
#             for(int j = 0; j<n; j++) {
#                 if(i==0 && j==0) {
#                     map[i][j] = 1;
#                 }else if(i==0 && j!=0) {
#                     map[i][j] = map[i][j-1];
#                 }else if(i!=0 && j==0) {
#                     map[i][j] = map[i-1][j];
#                 }else if(i!=0 && j!=0) {
#                     map[i][j] = map[i-1][j] + map[i][j-1];
#                 }
#             }
#         }
#         return map[m-1][n-1];
#     }
# }