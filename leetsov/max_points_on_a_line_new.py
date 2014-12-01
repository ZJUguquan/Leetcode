class Point:
    def __init__(self, a=0, b=0):
        self.x = float(a)
        self.y = float(b)
        self.copy=1 # copy to mark  repeatation times.

    def __repr__(self):
        return str((self.x,self.y,self.copy))

    def tuple(self):
        return (self.x,self.y,self.copy)


class Line:
    def __init__(self,p1=None,p2=None):
        self.p1=p1
        self.p2=p2

    def __repr__(self):
        return str((self.p1,self.p2))


class Solution:
    # @param points, a list of Points
    # @return an integer
    def maxPoints(self, points):
        #calculate duplicates
        uniquePoints={}
        for point in points:
            key=(point.x,point.y)
            if uniquePoints.__contains__(key):
                uniquePoints[key].copy=uniquePoints[key].copy+1
            else:
                uniquePoints[key]=point

        points=list(uniquePoints.values())
        #print('unique points:',points)

        if len(points)<1:
            return 0
        if len(points)==1:
            return points[0].copy

        #calculate lines with two points
        lines=[]
        for i in range(0,len(points)-1):
            for j in range(i+1,len(points)):
                line=Line(points[i],points[j])
                lines.append(line)
        #print('line pairs:',lines)

        #calculate line key
        lineSets={}
        for line in lines:
            p1=line.p1
            p2=line.p2
            if p1.x!=p2.x:
                ka=p1.y-(p2.y-p1.y)/(p2.x-p1.x)*p1.x
                kb=(p2.y-p1.y)/(p2.x-p1.x)
            else:
                ka=p1.x-(p2.x-p1.x)/(p2.y-p1.y)*p1.y
                kb=None
            key=(ka,kb)
            if lineSets.__contains__(key)==False:
                lineSets[key]=set()
            lineSets[key].add(p1.tuple())
            lineSets[key].add(p2.tuple())
        #print('lineSets:',lineSets)

        #calculate line sizes
        lineSizes=map(lambda s:sum(map(lambda e:e[2],s)),lineSets.values())
        #print(lineSizes)
        return max(lineSizes)