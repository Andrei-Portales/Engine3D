import struct
from collections import namedtuple

V2 = namedtuple('Point2', ['x', 'y'])


def char(c):
    # 1 byte
    return struct.pack('=c', c.encode('ascii'))


def word(w):
    # 2 bytes
    return struct.pack('=h', w)


def dword(d):
    # 4 bytes
    return struct.pack('=l', d)


def color(r: float, g: float, b: float):
    # Acepta valores de 0 a 1
    return bytes([int(b * 255), int(g * 255), int(r * 255)])


BLACK = color(0, 0, 0)
WHITE = color(1, 1, 1)


class Renderer(object):

    def __init__(self, width: int, height: int):
        super().__init__()
        self.glInit(width, height)

    def glInit(self, width: int, height: int):
        self.clear_color = BLACK
        self.curr_color = WHITE
        self.glCreateWindow(width, height)

    def glCreateWindow(self, width: int, height: int):
        self.width = width
        self.height = height
        self.glViewPort(0, 0, width, height)
        self.glClear()

    def glClearColor(self, r: float, g: float, b: float):
        self.clear_color = color(r, g, b)

    def glClear(self):
        self.pixels = [[self.clear_color for x in range(
            self.width)] for y in range(self.height)]

    def glColor(self, r: float, g: float, b: float):
        self.curr_color = color(r, g, b)

    def glViewPort(self, x: int, y: int, width: int, height: int):
        tempX = x + width
        tempY = y + height

        if tempX > self.width or tempY > self.height:
            raise 'ViewPort out of screen range'

        self.vpX = x
        self.vpY = y
        self.vpWidth = width
        self.vpHeight = height

    def glViewPortClear(self, color:color):
        for x in range(self.vpWidth):
            xp = self.vpX + x
            for y in range(self.vpHeight):
                yp = self.vpY + y
                self.pixels[yp][xp] = color

    def glPoint_NDC(self, x: int, y: int, color:color=None):

        if x < -1 or x > 1:
            return

        if y < -1 or y > 1:
            return

        pixelX = (x + 1) * (self.vpWidth / 2) + self.vpX
        pixelY = (y + 1) * (self.vpHeight / 2) + self.vpY
        if (0 <= x <= self.width) and (0 <= y <= self.height):
            self.pixels[int(y)][int(x)] = color or self.curr_color


    def glPoint(self, x: int, y: int, color: color = None):
        if x < self.vpX or x >= self.vpX + self.vpWidth or y < self.vpY or y >= self.vpY + self.vpHeight:
            return

        if (0 <= x <= self.width) and (0 <= y <= self.height):
            self.pixels[int(y)][int(x)] = color or self.curr_color

    def glLine_NDC(self, v0: V2, v1: V2, color: color = None):
        print()


    def glLine(self, v0: V2, v1: V2, color: color = None):
        x0 = v0.x
        x1 = v1.x
        y0 = v0.y
        y1 = v1.y

        dx = abs(x1 - x0)
        dy = abs(y1 - y0)

        steep = dy > dx

        if steep:
            x0, y0 = y0, x0
            x1, y1 = y1, x1

        if x0 > x1:
            x0, x1 = x1, x0
            y0, y1 = y1, y0

        dx = abs(x1 - x0)
        dy = abs(y1 - y0)

        offset = 0
        limit = 0.5
        m = dy / dx
        y = y0

        for x in range(x0, x1 + 1):
            if steep:
                self.glPoint(y, x, color=color)
            else:
                self.glPoint(x, y, color=color)

            offset += m
            if offset >= limit:
                y += 1 if y0 < y1 else - 1
                limit += 1

    def glVertex(self, x: int, y: int, color:color=None):
        if (-1 > x > 1) or (-1 > y > 1):
            raise 'Invalid vertex'

        mX = int(self.vpWidth / 2)
        mY = int(self.vpHeight / 2)
        cX = self.vpX + mX + (mX * x)
        cY = self.vpY + mY + (mY * y)
        self.glPoint(cX, cY, color)

    def glFinish(self, filename: str):
        file = open(filename, 'wb')
        # header
        file.write(bytes('B'.encode('ascii')))
        file.write(bytes('M'.encode('ascii')))
        file.write(dword(14 + 40 + (self.width * self.height * 3)))
        file.write(dword(0))
        file.write(dword(14 + 40))

        # info header
        file.write(dword(40))
        file.write(dword(self.width))
        file.write(dword(self.height))
        file.write(word(1))
        file.write(word(24))
        file.write(dword(0))
        file.write(dword(self.width * self.height * 3))
        file.write(dword(0))
        file.write(dword(0))
        file.write(dword(0))
        file.write(dword(0))

        # color table
        for x in range(self.height):
            for y in range(self.width):
                file.write(self.pixels[x][y])

        file.close()
