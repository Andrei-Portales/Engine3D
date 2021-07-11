import struct


def char(c):
    # 1 byte
    return struct.pack('=c', c.encode('ascii'))

def word(w):
    # 2 bytes
    return struct.pack('=h', w)

def dword(d):
    # 4 bytes
    return struct.pack('=l', d)

def color(r, g, b):
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
        self.viewPortX = 0
        self.viewPortY = 0
        self.viewPortWidth = width
        self.viewPortHeight = height
        self.glCreateWindow(width, height)

    def glCreateWindow(self, width: int, height: int):
        self.width = width
        self.height = height
        self.glClear()

    def glClearColor(self, r: float, g: float, b: float):
        self.clear_color = color(r, g, b)

    def glClear(self):
        self.pixels = [[self.clear_color for x in range(
            self.width)] for y in range(self.height)]

    def glColor(self, r: float, g: float, b: float):
        self.curr_color = color(r, g, b)

    def glPoint(self, x: int, y: int):
        self.pixels[x][y] = self.curr_color

    def glViewPort(self, x: int, y: int, width: int, height: int):
        tempX = x + width
        tempY = y + height

        if tempX > self.width or tempY > self.height:
            raise 'ViewPort out of range'

        self.viewPortX = x
        self.viewPortY = y
        self.viewPortWidth = width
        self.viewPortHeight = height

    def glVertex(self, x: int, y: int):
        if (x > 1 or x < -1) or (y > 1 or y < -1):
            raise 'Invalid vertex'

        mX = int(self.viewPortWidth / 2)
        mY = int(self.viewPortHeight / 2)
        cX = self.viewPortX + mX + (mX * x)
        cY = self.viewPortY + mY + (mY * y)
        self.glPoint(cX, cY)

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
