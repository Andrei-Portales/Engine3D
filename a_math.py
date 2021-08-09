import math


def det2X2(*v):
    return v[0][0] * v[1][1] - v[0][1] * v[1][0]


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
    return math.sqrt(v[0]**2 + v[1]**2 + v[2]**2)

def div(vector: tuple, normal: float):
    return tuple(map(lambda item: item / normal, vector))



