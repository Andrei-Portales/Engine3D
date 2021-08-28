import struct
from collections import namedtuple
from obj import Obj
import a_math as mt
import math


V2 = namedtuple('Point2', ['x', 'y'])
V3 = namedtuple('Point3', ['x', 'y', 'z'])
V4 = namedtuple('Point4', ['x', 'y', 'z', 'w'])


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


def baryCoords(A, B, C, P):
    try:
        # PCB / ABC
        u = (((B.y - C.y) * (P.x - C.x) + (C.x - B.x) * (P.y - C.y)) /
             ((B.y - C.y) * (A.x - C.x) + (C.x - B.x) * (A.y - C.y)))

        #PCA / ABC
        v = (((C.y - A.y) * (P.x - C.x) + (A.x - C.x) * (P.y - C.y)) /
             ((B.y - C.y) * (A.x - C.x) + (C.x - B.x) * (A.y - C.y)))

        w = 1 - u - v

        return u, v, w
    except:
        return -1, -1, -1


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
        self.glViewMatrix()

        self.active_texture = None
        self.active_shader = None
        self.directional_light = V3(0, 0, 1)

    def glCreateWindow(self, width: int, height: int):
        self.width = width
        self.height = height
        self.glClear()
        self.glViewPort(0, 0, width, height)

    def glClearColor(self, r: float, g: float, b: float):
        self.clear_color = color(r, g, b)

    def glClear(self):
        self.pixels = [[self.clear_color for x in range(
            self.width)] for y in range(self.height)]
        self.zbuffer = [[float('inf') for x in range(self.width)]
                        for y in range(self.height)]

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

        self.viewPortMatrix = [[width/2, 0, 0, x + width / 2],
                               [0, height/2, 0,  y + height / 2],
                               [0, 0, 0.5, 0.5],
                               [0, 0, 0, 1]]
        self.glProjectionMatrix()

    def glViewPortClear(self, color: color):
        for x in range(self.vpWidth):
            xp = self.vpX + x
            for y in range(self.vpHeight):
                yp = self.vpY + y
                self.pixels[yp][xp] = color

    def glPoint_NDC(self, x: int, y: int, color: color = None):

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

    def glLine(self, v0: V2, v1: V2, color: color = None, returnPoints=False):
        points = []
        x0 = v0.x
        x1 = v1.x
        y0 = v0.y
        y1 = v1.y

        if x0 == x1 and y0 == y1:
            self.glPoint(x0, y0, color=color)

            if returnPoints:
                points.append(V2(x0, y0))

            return points

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

                if returnPoints:
                    points.append(V2(y, x))
            else:
                self.glPoint(x, y, color=color)

                if returnPoints:
                    points.append(V2(x, y))

            offset += m
            if offset >= limit:
                y += 1 if y0 < y1 else - 1
                limit += 1
        if returnPoints:
            return points

    def glVertex(self, x: int, y: int, color: color = None):
        if (-1 > x > 1) or (-1 > y > 1):
            raise 'Invalid vertex'

        mX = int(self.vpWidth / 2)
        mY = int(self.vpHeight / 2)
        cX = self.vpX + mX + (mX * x)
        cY = self.vpY + mY + (mY * y)
        self.glPoint(cX, cY, color)

    def glTransform(self, vertex, vMatrix):
        augVertex = V4(vertex[0], vertex[1], vertex[2], 1)
        transVertex = mt.multMatrix4x4AndVector(vMatrix, augVertex)
        transVertex = V3(transVertex[0] / transVertex[3],
                         transVertex[1] / transVertex[3],
                         transVertex[2] / transVertex[3])
        return transVertex

    def glDirTransform(self, dirVector, vMatrix):
        augVertex = V4(dirVector[0], dirVector[1], dirVector[2], 0)
        transVertex = mt.multMatrix4x4AndVector(vMatrix, augVertex)
        transVertex = V3(transVertex[0], transVertex[1], transVertex[2])
        return transVertex

    def glCamTransform(self, vertex):
        augVertex = V4(vertex[0], vertex[1], vertex[2], 1)

        transVertex = mt.multMatrix4x4AndVector(mt.multMatrix4X4(self.viewPortMatrix, mt.multMatrix4X4(
            self.projectionMatrix, self.viewMatrix)), augVertex)

        transVertex = V3(transVertex[0] / transVertex[3],
                         transVertex[1] / transVertex[3],
                         transVertex[2] / transVertex[3])

        return transVertex

    def glLoadModelTriangle(self, filename, scale=V3(1, 1, 1), translate=V3(0.0, 0.0, 0.0), rotate=V3(0, 0, 0)):
        model = Obj(filename)

        modelMatrix = self.glCreateObjectMatrix(translate, scale, rotate)

        rotationMatrix = self.glCreateRotateMatrix(rotate)

        for face in model.faces:
            vertCount = len(face)

            index0 = face[0][0] - 1
            index1 = face[1][0] - 1
            index2 = face[2][0] - 1

            vert0 = model.vertices[index0]
            vert1 = model.vertices[index1]
            vert2 = model.vertices[index2]

            if vertCount == 4:
                vert3 = model.vertices[face[3][0] - 1]

            vt0 = model.texcoords[face[0][1] - 1]
            vt1 = model.texcoords[face[1][1] - 1]
            vt2 = model.texcoords[face[2][1] - 1]

            if vertCount == 4:
                vt3 = model.texcoords[face[3][1] - 1]

            vn0 = model.nomals[face[0][2] - 1]
            vn1 = model.nomals[face[1][2] - 1]
            vn2 = model.nomals[face[2][2] - 1]

            if vertCount == 4:
                vn3 = model.nomals[face[3][2] - 1]

            vn0 = self.glDirTransform(vn0, rotationMatrix)
            vn1 = self.glDirTransform(vn1, rotationMatrix)
            vn2 = self.glDirTransform(vn2, rotationMatrix)

            if vertCount == 4:
                vn3 = self.glDirTransform(vn3, rotationMatrix)

            vert0 = self.glTransform(vert0, modelMatrix)
            vert1 = self.glTransform(vert1, modelMatrix)
            vert2 = self.glTransform(vert2, modelMatrix)

            if vertCount == 4:
                vert3 = self.glTransform(vert3, modelMatrix)

            a = self.glCamTransform(vert0)
            b = self.glCamTransform(vert1)
            c = self.glCamTransform(vert2)

            if vertCount == 4:
                d = self.glCamTransform(vert3)

            self.glTriangle_bc(a, b, c, texCoords=(
                vt0, vt1, vt2), verts=(vert0, vert1, vert2), normals=(vn0, vn1, vn2))
            if vertCount == 4:
                self.glTriangle_bc(a, c, d, texCoords=(
                    vt0, vt2, vt3), verts=(vert0, vert2, vert3), normals=(vn0, vn2, vn3))

    def glViewMatrix(self, translate=V3(0, 0, 0), rotate=V3(0, 0, 0)):
        camMatrix = self.glCreateObjectMatrix(translate, V3(1, 1, 1), rotate)
        self.viewMatrix = mt.inv(camMatrix)

    def glLookAt(self, eye, camPosition=V3(0, 0, 0)):
        forward = mt.subtract(camPosition, eye)
        forward = mt.div(forward, mt.norm(forward))

        right = mt.cross(V3(0, 1, 0), forward)
        right = mt.div(right, mt.norm(right))

        up = mt.cross(forward, right)
        up = mt.div(up, mt.norm(up))

        camMatrix = [[right[0], up[0], forward[0], camPosition.x],
                     [right[1], up[1], forward[1], camPosition.y],
                     [right[2], up[2], forward[2], camPosition.z],
                     [0, 0, 0, 1]]

        self.viewMatrix = mt.inv(camMatrix)

    def glProjectionMatrix(self, n=0.1, f=1000, fov=60):
        t = math.tan((mt.deg2rad(fov) / 2) * n)
        r = t * self.vpWidth / self.vpHeight

        self.projectionMatrix = [[n/r, 0, 0, 0],
                                 [0, n/t, 0, 0],
                                 [0, 0, -(f+n)/(f-n), -(2*f*n)/(f-n)],
                                 [0, 0, -1, 0]]

    def glLoadModel(self, filename, scale=V2(1, 1), translate=V2(0.0, 0.0), fill=False):
        model = Obj(filename)

        for face in model.faces:
            verCount = len(face)
            lines = []

            for v in range(verCount):
                index0 = face[v][0] - 1
                index1 = face[(v + 1) % verCount][0] - 1

                vert0 = model.vertices[index0]
                vert1 = model.vertices[index1]

                x0 = int(vert0[0] * scale.x + translate.x)
                y0 = int(vert0[1] * scale.y + translate.y)

                x1 = int(vert1[0] * scale.x + translate.x)
                y1 = int(vert1[1] * scale.y + translate.y)

                lines.append(self.glLine(
                    V2(x0, y0), V2(x1, y1), returnPoints=True))

            if fill:
                from random import random
                self.glPolygon(lines, color(random(), random(),
                                            random()), includeLines=False)

    def glCreateObjectMatrix(self, translate=V3(0, 0, 0), scale=V3(1, 1, 1), rotate=V3(0, 0, 0)):

        translateMatrix = [[1, 0, 0, translate.x],
                           [0, 1, 0, translate.y],
                           [0, 0, 1, translate.z],
                           [0, 0, 0, 1]]

        scaleMatrix = [[scale.x, 0, 0, 0],
                       [0, scale.y, 0, 0],
                       [0, 0, scale.z, 0],
                       [0, 0, 0, 1]]

        rotationMatrix = self.glCreateRotateMatrix(rotate=rotate)
        return mt.multMatrix4X4(mt.multMatrix4X4(translateMatrix, rotationMatrix), scaleMatrix)

    def glCreateRotateMatrix(self, rotate=V3(0, 0, 0)):

        pitch = mt.deg2rad(rotate.x)
        yaw = mt.deg2rad(rotate.y)
        roll = mt.deg2rad(rotate.z)

        rotationX = [[1, 0, 0, 0],
                     [0, math.cos(pitch), -math.sin(pitch), 0],
                     [0, math.sin(pitch), math.cos(pitch), 0],
                     [0, 0, 0, 1]]

        rotationY = [[math.cos(yaw), 0, math.sin(yaw), 0],
                     [0, 1, 0, 0],
                     [-math.sin(yaw), 0, math.cos(yaw), 0],
                     [0, 0, 0, 1]]

        rotationZ = [[math.cos(roll), -math.sin(roll), 0, 0],
                     [math.sin(roll), math.cos(roll), 0, 0],
                     [0, 0, 1, 0],
                     [0, 0, 0, 1]]

        return mt.multMatrix4X4(mt.multMatrix4X4(rotationX, rotationY), rotationZ)

    def glPolygon(self, lines, color=color(1, 1, 1), includeLines=True):
        p = []

        for n in lines:
            for m in n:
                p.append(m)

        ys = [n.y for n in p]
        ymin = min(ys)
        ymax = max(ys)

        for y in range(ymin, ymax + 1):
            xs = [point.x for point in p if point.y == y]
            xmin = min(xs)
            xmax = max(xs)

            for x in range(xmin, xmax + 1):
                y2p = [point.y for point in p if point.x == x]
                y2min = min(y2p)
                y2max = max(y2p)

                if y2min <= y <= y2max:
                    if includeLines:
                        if (x not in xs):
                            self.glPoint(x, y, color)
                    else:
                        self.glPoint(x, y, color)

    def glTriangle(self, A: V2, B: V2, C: V2, color=None):

        if A.y < B.y:
            A, B = B, A
        if A.y < C.y:
            A, C = C, A
        if B.y < C.y:
            B, C = C, B

        def flatBottomTriangle(v1, v2, v3):
            try:
                d_21 = (v2.x - v1.x) / (v2.y - v1.y)
                d_31 = (v3.x - v1.x) / (v3.y - v1.y)
            except:
                pass
            else:
                x1 = v2.x
                x2 = v3.x
                for y in range(v2.y, v1.y + 1):
                    self.glLine(V2(int(x1), y), V2(int(x2), y), color)
                    x1 += d_21
                    x2 += d_31

        def flatTopTriangle(v1, v2, v3):
            try:
                d_31 = (v3.x - v1.x) / (v3.y - v1.y)
                d_32 = (v3.x - v2.x) / (v3.y - v2.y)
            except:
                pass
            else:
                x1 = v3.x
                x2 = v3.x

                for y in range(v3.y, v1.y + 1):
                    self.glLine(V2(int(x1), y), V2(int(x2), y), color)
                    x1 += d_31
                    x2 += d_32

        if B.y == C.y:
            # triangulo con base inferior plana
            flatBottomTriangle(A, B, C)
        elif A.y == B.y:
            # triangulo con base superior plana
            flatTopTriangle(A, B, C)
        else:
            # dividir el triangulo en dos
            # dibujar ambos casos
            # Teorema de intercepto
            D = V2(A.x + ((B.y - A.y) / (C.y - A.y)) * (C.x - A.x), B.y)
            flatBottomTriangle(A, B, D)
            flatTopTriangle(B, D, C)

    def glTriangle_bc(self, A: V2, B: V2, C: V2, _color=None, texCoords=(), verts=(), normals=()):
        # Bounding box
        minX = int(min(A.x, B.x, C.x))
        minY = int(min(A.y, B.y, C.y))
        maxX = int(max(A.x, B.x, C.x))
        maxY = int(max(A.y, B.y, C.y))

        triangleNormal = mt.cross(mt.subtract(
            verts[1], verts[0]), mt.subtract(verts[2], verts[0]))
        triangleNormal = mt.div(triangleNormal, mt.norm(triangleNormal))

        for x in range(minX, maxX + 1):
            for y in range(minY, maxY + 1):
                u, v, w = baryCoords(A, B, C, V2(x, y))

                if u >= 0 and v >= 0 and w >= 0:

                    z = A.z * u + B.z * v + C.z * w

                    if x < self.vpX or x >= self.vpX + self.vpWidth or y < self.vpY or y >= self.vpY + self.vpHeight:
                        pass
                    else:
                        if (0 <= x <= self.width) and (0 <= y <= self.height):
                            if z <= 1 and z >= -1 and z < self.zbuffer[int(y)][int(x)]:

                                if self.active_shader:
                                    r,g,b = self.active_shader(self, 
                                                                 verts=verts, baryCoords=(u, v, w), 
                                                                 texCoords=texCoords, 
                                                                 normals=normals, 
                                                                 triangleNormal=triangleNormal, 
                                                                 color=_color or self.curr_color,
                                                                 yValues=(minY, maxY, y),
                                                                 xValues=(minX, maxX, x))
                                else:
                                    b, g, r = _color or self.curr_color
                                    b, g, r = b/255, g/255, r/255

                                self.glPoint(x, y, color(r, g, b))
                                self.zbuffer[int(y)][int(x)] = z

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

        # if self.active_texture:
        #     tA, tB, tC = texCoords
        #     tx = tA[0] * u + tB[0] * v + tC[0] * w
        #     ty = tA[1] * u + tB[1] * v + tC[1] * w
        #     texColor = self.active_texture.getColor(tx, ty)
        # else:
        #     texColor = color(1, 1, 1)
