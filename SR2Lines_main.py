from gl import Renderer, V2, color
import math

width = 1100
height = 600

rd = Renderer(width, height)

rd.glClearColor(0.2, 0.2, 0.2)
rd.glClear()

rd.glColor(1, 1, 1)


def degToRad(deg):
    return deg * 3.141592653589793 / 180

def rotate(origin: V2, point: V2, degrees: float):
    ox, oy = origin.x, origin.y
    px, py = point.x, point.y
    angle = degToRad(degrees)
    qx = ox + math.cos(angle) * (px - ox) - math.sin(angle) * (py - oy)
    qy = oy + math.sin(angle) * (px - ox) + math.cos(angle) * (py - oy)
    return V2(int(qx), int(qy))


def triangle(size: int, x: int, y: int, rotation=0):
    center = V2(int(x + size / 2), int(y + size / 2))
    col = color(1, 1, 1)

    p1x, p1y = rotate(center, V2(x, y), rotation), rotate(center, V2(int(x + size / 2), y + size), rotation)
    p2x, p2y = rotate(center, V2(int(x + size / 2), y + size), rotation), rotate(center,  V2(x + size, y), rotation)
    p3x, p3y = rotate(center, V2(x, y), rotation), rotate(center,  V2(x + size, y), rotation)

    rd.glLine(p1x, p1y, col)
    rd.glLine(p2x, p2y, col)
    rd.glLine(p3x, p3y, col)

def square(size: int, x: int, y: int, rotation=0):
    center = V2(int(x + size / 2), int(y + size / 2))
    col = color(1, 1, 1)

    p1x, p1y = rotate(center, V2(x, y), rotation), rotate(center,  V2(x, y + size), rotation)
    p2x, p2y = rotate(center, V2(x, y + size), rotation), rotate(center,  V2(x + size, y + size), rotation)
    p3x, p3y = rotate(center, V2(x + size, y+ size), rotation), rotate(center,  V2(x + size, y), rotation)
    p4x, p4y = rotate(center, V2(x + size, y), rotation), rotate(center,  V2(x, y), rotation)

    rd.glLine(p1x, p1y, color=col)
    rd.glLine(p2x, p2y, color=col)
    rd.glLine(p3x, p3y, color=col)
    rd.glLine(p4x, p4y, color=col)

def triangleRectangle(size: int, x: int, y: int, rotation=0):
    center = V2(int(x + size / 2), int(y + size / 2))
    col = color(1, 1, 1)

    p1x, p1y = rotate(center, V2(x, y), rotation), rotate(center,  V2(x, y + size), rotation)
    p2x, p2y = rotate(center, V2(x, y), rotation), rotate(center,  V2(int(x + size * 1.5), y), rotation)
    p3x, p3y = rotate(center, V2(x, y + size), rotation), rotate(center,  V2(int(x + size * 1.5), y), rotation)

    rd.glLine(p1x, p1y, color=col)
    rd.glLine(p2x, p2y, color=col)
    rd.glLine(p3x, p3y, color=col)

def hexagono(size: int, x: int, y: int, rotation=0):
    center = V2(int(x + size / 2), int(y + size / 2))
    col = color(1, 1, 1)

    p1x, p1y = rotate(center, V2(int(x + size * 0.2), y), rotation), rotate(center, V2(int(x + size * 0.8), y), rotation)
    p2x, p2y = rotate(center, V2(int(x + size * 0.8), y), rotation), rotate(center, V2(x + size, int(y + size * 0.5)), rotation)
    p3x, p3y = rotate(center, V2(x + size, int(y + size * 0.5)), rotation), rotate(center, V2(int(x + size * 0.8), y + size), rotation)
    p4x, p4y = rotate(center, V2(int(x + size * 0.2), y + size), rotation), rotate(center, V2(int(x + size * 0.8), y + size), rotation)
    p5x, p5y = rotate(center, V2(int(x + size * 0.2), y), rotation), rotate(center, V2(x, int(y + size * 0.5)), rotation)
    p6x, p6y = rotate(center, V2(x, int(y + size * 0.5)), rotation), rotate(center, V2(int(x + size * 0.2), y + size), rotation)

    rd.glLine(p1x, p1y, color=col)
    rd.glLine(p2x, p2y, color=col)
    rd.glLine(p3x, p3y, color=col)
    rd.glLine(p4x, p4y, color=col)
    rd.glLine(p5x, p5y, color=col)
    rd.glLine(p6x, p6y, color=col)

def rectangle(size: int, x: int, y: int, rotation=0):
    center = V2(int(x + size / 2), int(y + size / 2))
    col = color(1, 1, 1)

    p1x, p1y = rotate(center, V2(x, y), rotation), rotate(center,  V2(x, y + size), rotation)
    p2x, p2y = rotate(center, V2(x + size * 2, y + size), rotation), rotate(center,   V2(x + size * 2, y), rotation)
    p3x, p3y = rotate(center, V2(x, y + size), rotation), rotate(center,  V2(x + size * 2, y + size), rotation)
    p4x, p4y = rotate(center, V2(x + size * 2, y), rotation), rotate(center,  V2(x, y), rotation)

    rd.glLine(p1x, p1y, color=col)
    rd.glLine(p2x, p2y, color=col)
    rd.glLine(p3x, p3y, color=col)
    rd.glLine(p4x, p4y, color=col)

def circle(radius: int, x: int, y: int, fill=1, color=color(1,1,1)):
    center = V2(int(x), int(y))
    col = color

    currPoint = V2(center.x + radius, center.y)

    for n in range(361 * fill):
        currPoint = rotate(center, currPoint, n)
        rd.glPoint(currPoint.x, currPoint.y, col)



triangle(100, 50, 50, rotation=45)
triangle(100, 150, 50, rotation=-45)

square(100, 325, 50, rotation=45)
square(100, 465, 50, rotation=80)

triangleRectangle(100, 700, 50, rotation=45)
triangleRectangle(100, 880, 100, rotation=-60)

hexagono(100, 20, 300, rotation=15)
hexagono(100, 120, 400, rotation=-15)

rectangle(100, 325, 300, rotation=75)
rectangle(100, 475, 350, rotation=-50)

circle(50, 800, 310, fill=110, color=color(0, 1, 0))
circle(50, 800, 460, fill=110, color=color(1, 0, 0))
circle(50, 930, 390, fill=110, color=color(0, 0, 1))


rd.glFinish('lab_outputs/lab2.bmp')
