# cargar modelos 3d OBJ
import struct

def color(r: float, g: float, b: float):
    # Acepta valores de 0 a 1
    return bytes([int(b * 255), int(g * 255), int(r * 255)])

class Obj(object):

    def __init__(self, filename: str):

        file = open(filename, 'r')
        self.lines = file.read().splitlines()
        file.close()

        self.vertices = []
        self.texcoords = []
        self.nomals = []
        self.faces = []
        self.read()

    def read(self):
        for line in self.lines:
            if line:
                try:
                    prefix, value = line.split(' ', 1)

                    if prefix == 'v': # vertices
                        self.vertices.append(list(map(float, value.split(' '))))
                    elif prefix == 'vt': # texture cords
                        self.texcoords.append(list(map(float, value.split(' '))))
                    elif prefix == 'vn': # normales
                        self.nomals.append(list(map(float, value.split(' '))))

                    elif prefix == 'f': # faces
                        self.faces.append([ list(map(int, face.split('/'))) for face in value.split(' ') ])
                except ValueError:
                    pass
                

class Texture(object):
    def __init__(self, filename):
        self.filename = filename
        self.read()

    def read(self):
        image = open(self.filename, 'rb')

        image.seek(10)
        headerSize = struct.unpack('=l', image.read(4))[0]

        image.seek(14 + 4)
        self.width = struct.unpack('=l', image.read(4))[0]
        self.height = struct.unpack('=l', image.read(4))[0]

        image.seek(headerSize)

        self.pixels = []

        for x in range(self.width):
            self.pixels.append([])
            for y in range(self.height):
               
                b = ord(image.read(1)) / 255
                g = ord(image.read(1)) / 255
                r = ord(image.read(1)) / 255

                self.pixels[x].append(color(r, g, b))
        

        image.close()

    def getColor(self, tx, ty):

        if 0 <= tx <= 1 and 0 <= ty <= 1:
            x = round(tx * self.width)
            y = round(ty * self.height)
            return self.pixels[y][x] # posiblemente este mal
        else:
            return color(0, 0, 0)


        