# cargar modelos 3d OBJ

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
                