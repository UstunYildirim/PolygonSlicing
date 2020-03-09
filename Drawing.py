from math import cos
from math import sin
from math import pi

class Drawing:
    N = 10
    ang = 2*pi/N
    pointsNgon = [(cos(i*ang),sin(i*ang)) for i in range(N)]

    intersectionPoints = []

    @classmethod
    def wCoords(cls,x,y):
        return (410+y*400,410-x*400)

    @classmethod
    def createPoints(cls):
        ang = 2*pi/Drawing.N
        Drawing.pointsNgon = [(cos(i*ang),sin(i*ang)) for i in range(Drawing.N)]

    @classmethod
    def incN(cls, event=None):
        Drawing.N = Drawing.N + 1 
        Drawing.createPoints()
        Drawing.init()

    @classmethod
    def decN(cls, event=None):
        Drawing.N = Drawing.N - 1 
        Drawing.createPoints()
        Drawing.init()
    
    @classmethod
    def dual(cls, event=None):
        Drawing.findIntersectionPoints()


    @classmethod
    def init(cls):
        Drawing.canvas.delete('all')
        Drawing.drawNgon()

    @classmethod
    def drawNgon(cls, event=None):
        for p1 in Drawing.pointsNgon:
            for p2 in Drawing.pointsNgon:
                Drawing.canvas.create_line(Drawing.wCoords(*p1),Drawing.wCoords(*p2))
    
    @classmethod
    def findIntersectionPoints(cls):
        Drawing.intersectionPoints = []
        for i1 in range(Drawing.N):
            for i2 in range(i1+2,Drawing.N):
                for i3 in range(i1+1,i2):
                    for i4 in range(i2+1,Drawing.N):
                        (x1,y1) = Drawing.pointsNgon[i1]
                        (x2,y2) = Drawing.pointsNgon[i2]
                        (x3,y3) = Drawing.pointsNgon[i3]
                        (x4,y4) = Drawing.pointsNgon[i4]
                        if x2-x1 == 0:
                            s = (x1-x3)/(x4-x3)
                        else:
                            s = (y2-y1)*(x3-x1)-(x2-x1)*(y3-y1) / ((x2-x1)*(y4-y3)-(y2-y1)*(x4-x3))
                        Drawing.intersectionPoints.append((x3+s*(x4-x3), y3+s*(y4-y3)))
        print(len(Drawing.intersectionPoints))
        Drawing.intersectionPoints = list(set(Drawing.intersectionPoints))
        print(len(Drawing.intersectionPoints))

