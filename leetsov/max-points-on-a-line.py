# # Definition for a point
class Point:
	def __init__(self, a=0, b=0):
		self.x = a
		self.y = b

"参考方法:  存在一条直线 经过点i, 而且这条直线通过的点数 肯定比其他通过i的直线要多. !!!"
# Definition for a point
# class Point:
#     def __init__(self, a=0, b=0):
#         self.x = a
#         self.y = b
class Solution:
  def maxPoints(self, points):
    res = 0; n = len(points)
    for i in range(n):
        # ni number of repeating
        # max_count
        ni, max_count = 1, 0
        counter = {} ; counter[float('inf')] = 0
        for j in range(i+1, n):
            if points[i].x == points[j].x:
                if points[i].y == points[j].y:
                    ni +=1
                else:
                    # vertical lines, passing point i.
                    counter[float('inf')] +=1
            else:
                if (points[i].y - points[j].y) / (points[i].x - points[j].x) not in counter:
                    counter[(points[i].y - points[j].y) / (points[i].x - points[j].x)] = 1
                else:
                    counter[(points[i].y - points[j].y) / (points[i].x - points[j].x)] += 1
        max_count = max(list(counter.values()))
        max_count += ni
        res =  max_count if res < max_count else res
    return res
"""
    //general case
    int res = 0;

    for (int i = 0; i < n; i++)
    {      // all line will pass through ith element
        int ni(1), max_count(0); //ni is the number of repeating point for ith
        map<double, int> count;  //count the number of points for each line (determined by slope)
        for (int j = i + 1; j < n; j++)
        {
            if (points[i].x == points[j].x)
            {
                if (points[i].y == points[j].y)   //same point
                    ni++;
                else //vertical
                    count[INT_MAX - INT_MIN + 1] += 1;
            }
            else
                count[double(points[i].y - points[j].y) / (points[i].x - points[j].x)] += 1;
        }
        for (map<double, int>::iterator it = count.begin(); it != count.end(); it++)
            max_count = (max_count < (it->second)) ? (it->second) : max_count;

        max_count += ni;
        res = (res < max_count) ? max_count : res;
    }

    return res;
}
"""

# class Solution:
# 	def slope(self, p1, p2):
# 		if p1.x == p2.x and p1.y == p2.y:
# 			return 'co' # coincide
# 		elif p1.x == p2.x :
# 			return 'ver' # vertical
# 		else:
# 			return (p2.y-p1.y)/(p2.x-p1.x)

# 	def maxPoints(self, points):
# 		if len(points) <= 2:
# 			return len(points)
# 		slopeMatrix = [ [0 for i in range(len(points))] for j in range(len(points))]
# 		for i in range(len(points)):
# 			for j in range(len(points)):
# 				slopeMatrix[i][j] = self.slope(points[i], points[j])

# 		for i in range(len(points)):
# 			for j in range(i,len(points)):
# 				print(slopeMatrix[i][j],end=",")
# 			print("\n")



p1 = Point()
p2 = Point()
p3 = Point(1,2)
points= []
points.append(p1)
points.append(p2)
points.append(p3)
s = Solution()
s.maxPoints(points)


'others'
'http://is.gd/Lc6Aqy'
    def maxPoints(self, points):
    n = len(points)
    if n <= 2: return n

    maxp = 2
    for i in range(n - 2):
        ratioMaps, maxpi, overlap = {}, 1, 0
        for j in range(i + 1, n):
            dx = float(points[j].x) - float(points[i].x)
            dy = float(points[j].x) - float(points[i].x)
            if abs(dx) < 0.00001 and abs(dy) < 0.00001:
                overlap += 1
                continue
            ratio = int(abs(dy) / (abs(dx) + abs(dy)) * 1000000)
            if (dx < 0 and dy > 0) or \
                    (dx > 0 and dy < 0):
                ratio = -ratio
            if ratioMaps.has_key(ratio):
                ratioMaps[ratio] += 1
                # ratioMaps[ratio].append(j)
            else:
                ratioMaps[ratio] = 2
                # ratioMaps[ratio] = [i, j]
            if maxpi < ratioMaps[ratio]:
                maxpi = ratioMaps[ratio]
        maxpi += overlap
        if maxp < maxpi: maxp = maxpi
        # print ratioMaps, overlap, maxpi

    return maxp