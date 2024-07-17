import math
points= [[2,3],[5,3],[2,1],[7,3],[4,3]]
x= int
y= int
def euclideanDistance(x,y):
    return math.sqrt((x*x)+(y*y))
for sayi in range(len(points)):
        x=points[sayi][0]
        y=points[sayi][1]
        print(round(euclideanDistance(x,y)))


