from math import sqrt

def dist(point1, point2) -> float:
    return sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)

def signal(a) -> int:
    if a!=0:
        return abs(a)/a
    else: 
        return 0