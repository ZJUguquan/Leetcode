# Definition for a point
class Point:
	def __init__(self, a=0, b=0):
		self.x = a
		self.y = b

class Solution:
	def slope(self, p1, p2):
		if p1.x == p2.x and p1.y == p2.y:
			return 'co' # coincide
		elif p1.x == p2.x :
			return 'ver' # vertical
		else:
			return (p2.y-p1.y)/(p2.x-p1.x)

	def maxPoints(self, points):
		if len(points) <= 2:
			return len(points)
		slopeMatrix = [ [0 for i in range(len(points))] for j in range(len(points))]
		for i in range(len(points)):
			for j in range(len(points)):
				slopeMatrix[i][j] = self.slope(points[i], points[j])

		for i in range(len(points)):
			for j in range(i,len(points)):
				print(slopeMatrix[i][j],end=",")
			print("\n")



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