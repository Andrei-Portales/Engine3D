import math


def deg2rad(deg):
    return deg * 3.141592653589793 / 180


def subMatrix4to3(matrix, yo, xo):
    m = []
    for y in range(4):
        temp = []
        for x in range(4):
            if yo != y and xo != x:
                temp.append(matrix[y][x])
        if len(temp) == 3:
            m.append(temp)
    return m


def det2X2(*v):
    return v[0][0] * v[1][1] - v[0][1] * v[1][0]


def det3X3(m):
    return m[0][0] * det2X2(m[1][1:3], m[2][1:3]) - m[0][1] * det2X2([m[1][0], m[1][2]], [m[2][0], m[2][2]]) + m[0][2] * det2X2(m[1][0:2], m[2][0:2])


def det4X4(m):
    vals = []
    for x in range(4):
        subM = subMatrix4to3(m, 0, x)
        val = m[0][x] * det3X3(subM)
        vals.append(val)

    return vals[0] - vals[1] + vals[2] - vals[3]


def cross(*vectors):
    if len(vectors) == 2:
        v1 = vectors[0]
        v2 = vectors[1]
        return det2X2((v1[1], v1[2]), (v2[1], v2[2])), -1 * det2X2((v1[0], v1[2]), (v2[0], v2[2])), det2X2((v1[0], v1[1]), (v2[0], v2[1]))


def subtract(*vectors):
    return tuple(map(lambda i, j: i - j, *vectors))


def dot(*vectors):
    r = tuple(map(lambda i, j: i * j, *vectors))
    return r[0] + r[1] + r[2]


def norm(v):
    return (v[0]**2 + v[1]**2 + v[2]**2)**0.5


def div(vector: tuple, normal: float):
    return tuple(map(lambda item: item / normal, vector))


def matrixDiv(matrix, divisor):
    new = []
    for y in range(len(matrix)):
        vLen = len(matrix[y])
        temp = []
        for x in range(vLen):
            temp.append(matrix[y][x] / divisor)
        new.append(temp)

    return new


def rows2Cols(matrix):
    aT = [[], [], [], []]

    for n in range(4):
        vector = matrix[n]
        aT[0].append(vector[0])
        aT[1].append(vector[1])
        aT[2].append(vector[2])
        aT[3].append(vector[3])

    return aT


def cols2Rows(matrix):
    aT = [[], [], [], []]

    for n in range(4):
        aT[n] = [matrix[0][n], matrix[1][n], matrix[2][n], matrix[3][n]]

    return aT


def inv(matrix):
    aT = rows2Cols(matrix)

    adj = []
    sign = True

    for y in range(4):
        temp = []
        for x in range(4):
            subM = subMatrix4to3(aT, y, x)
            det = det3X3(subM)
            if sign:
                temp.append(det)
            else:
                temp.append(-(det))
            sign = not sign
        sign = not sign
        adj.append(temp)

    det = det4X4(matrix)
    return matrixDiv(adj, det)


def multMatrix4X4(m1, m2):
    m2T = cols2Rows(m2)
    mF = []

    for n in range(4):
        temp = []

        for j in range(4):
            res = 0
            for i in range(4):
                res += m1[n][i] * m2T[j][i]
            temp.append(res)
        mF.append(temp)

    return mF


def multMatrix4x4AndVector(matrix, vector):
    mF = []

    for n in range(4):
        res = 0
        for j in range(4):
            res += matrix[n][j] * vector[j]
        mF.append(res)
    return mF
