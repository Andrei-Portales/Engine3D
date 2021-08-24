from gl import color
import a_math as mt
import random as rn


def flat(renderer, **kwargs):
    A, B, C = kwargs['verts']
    u, v, w = kwargs['baryCoords']
    tA, tB, tC = kwargs['texCoords']
    b, g, r = kwargs['color']
    triangleNormal = kwargs['triangleNormal']

    b, g, r = b/255, g/255, r/255

    if renderer.active_texture:
        tx = tA[0] * u + tB[0] * v + tC[0] * w
        ty = tA[1] * u + tB[1] * v + tC[1] * w
        texColor = renderer.active_texture.getColor(tx, ty)
    else:
        texColor = color(1, 1, 1)

    b *= texColor[0] / 255
    g *= texColor[1] / 255
    r *= texColor[2] / 255

    intensity = mt.dot(triangleNormal, renderer.directional_light)

    b *= intensity
    g *= intensity
    r *= intensity

    if intensity > 0:
        return r, g, b
    else:
        return 0, 0, 0


def gourad(renderer, **kwargs):

    u, v, w = kwargs['baryCoords']
    tA, tB, tC = kwargs['texCoords']
    b, g, r = kwargs['color']
    nA, nB, nC = kwargs['normals']

    b /= 255
    g /= 255
    r /= 255

    if renderer.active_texture:
        tx = tA[0] * u + tB[0] * v + tC[0] * w
        ty = tA[1] * u + tB[1] * v + tC[1] * w
        texColor = renderer.active_texture.getColor(tx, ty)
    else:
        texColor = color(1, 1, 1)

    b *= texColor[0] / 255
    g *= texColor[1] / 255
    r *= texColor[2] / 255

    intensityA = mt.dot(nA, renderer.directional_light)
    intensityB = mt.dot(nB, renderer.directional_light)
    intensityC = mt.dot(nC, renderer.directional_light)

    intensity = intensityA * u + intensityB * v + intensityC * w

    b *= intensity
    g *= intensity
    r *= intensity

    if intensity > 0:
        return r, g, b
    else:
        return 0, 0, 0


def phong(renderer, **kwargs):

    u, v, w = kwargs['baryCoords']
    tA, tB, tC = kwargs['texCoords']
    b, g, r = kwargs['color']
    nA, nB, nC = kwargs['normals']

    b /= 255
    g /= 255
    r /= 255

    if renderer.active_texture:
        tx = tA[0] * u + tB[0] * v + tC[0] * w
        ty = tA[1] * u + tB[1] * v + tC[1] * w
        texColor = renderer.active_texture.getColor(tx, ty)
    else:
        texColor = color(1, 1, 1)

    b *= texColor[0] / 255
    g *= texColor[1] / 255
    r *= texColor[2] / 255

    nX = nA[0] * u + nB[0] * v + nC[0] * w
    nY = nA[1] * u + nB[1] * v + nC[1] * w
    nZ = nA[2] * u + nB[2] * v + nC[2] * w

    normal = (nX, nY, nZ)

    intensity = mt.dot(normal, renderer.directional_light)

    b *= intensity
    g *= intensity
    r *= intensity

    if intensity > 0:
        return r, g, b
    else:
        return 0, 0, 0


def unlit(renderer, **kwargs):
    u, v, w = kwargs['baryCoords']
    tA, tB, tC = kwargs['texCoords']
    b, g, r = kwargs['color']
    nA, nB, nC = kwargs['normals']

    b /= 255
    g /= 255
    r /= 255

    if renderer.active_texture:
        tx = tA[0] * u + tB[0] * v + tC[0] * w
        ty = tA[1] * u + tB[1] * v + tC[1] * w
        texColor = renderer.active_texture.getColor(tx, ty)
    else:
        texColor = color(1, 1, 1)

    b *= texColor[0] / 255
    g *= texColor[1] / 255
    r *= texColor[2] / 255

    return r, g, b


def toon(renderer, **kwargs):

    u, v, w = kwargs['baryCoords']
    tA, tB, tC = kwargs['texCoords']
    b, g, r = kwargs['color']
    nA, nB, nC = kwargs['normals']

    b /= 255
    g /= 255
    r /= 255

    if renderer.active_texture:
        tx = tA[0] * u + tB[0] * v + tC[0] * w
        ty = tA[1] * u + tB[1] * v + tC[1] * w
        texColor = renderer.active_texture.getColor(tx, ty)
    else:
        texColor = color(1, 1, 1)

    b *= texColor[0] / 255
    g *= texColor[1] / 255
    r *= texColor[2] / 255

    nX = nA[0] * u + nB[0] * v + nC[0] * w
    nY = nA[1] * u + nB[1] * v + nC[1] * w
    nZ = nA[2] * u + nB[2] * v + nC[2] * w

    normal = (nX, nY, nZ)

    intensity = mt.dot(normal, renderer.directional_light)

    if intensity > 0.7:
        intensity = 1
    elif intensity > 0.3:
        intensity = 0.5
    else:
        intensity = 0.05

    b *= intensity
    g *= intensity
    r *= intensity

    if intensity > 0:
        return r, g, b
    else:
        return 0, 0, 0


def static(renderer, **kwargs):

    u, v, w = kwargs['baryCoords']
    b, g, r = kwargs['color']
    nA, nB, nC = kwargs['normals']

    b /= 255
    g /= 255
    r /= 255

    nX = nA[0] * u + nB[0] * v + nC[0] * w
    nY = nA[1] * u + nB[1] * v + nC[1] * w
    nZ = nA[2] * u + nB[2] * v + nC[2] * w

    normal = (nX, nY, nZ)

    intensity = mt.dot(normal, renderer.directional_light)

    col = rn.random()

    b *= intensity * col
    g *= intensity * col
    r *= intensity * col

    if intensity > 0:
        return r, g, b
    else:
        return 0, 0, 0


def zebra(renderer, **kwargs):

    u, v, w = kwargs['baryCoords']
    b, g, r = kwargs['color']
    nA, nB, nC = kwargs['normals']

    b /= 255
    g /= 255
    r /= 255

    nX = nA[0] * u + nB[0] * v + nC[0] * w
    nY = nA[1] * u + nB[1] * v + nC[1] * w
    nZ = nA[2] * u + nB[2] * v + nC[2] * w

    normal = (nX, nY, nZ)

    intensity = mt.dot(normal, renderer.directional_light)

    unique = 1, 1, 1
    unique2 = 0, 0, 0

    if intensity > 0.95:
        r, g, b = unique
    elif intensity > 0.9:
        r, g, b = unique2
    elif intensity > 0.85:
        r, g, b = unique
    elif intensity > 0.8:
        r, g, b = unique2
    elif intensity > 0.75:
        r, g, b = unique
    elif intensity > 0.7:
        r, g, b = unique2
    elif intensity > 0.65:
        r, g, b = unique
    elif intensity > 0.6:
        r, g, b = unique2
    elif intensity > 0.55:
        r, g, b = unique
    elif intensity > 0.5:
        r, g, b = unique2
    elif intensity > 0.45:
        r, g, b = unique
    elif intensity > 0.4:
        r, g, b = unique2
    elif intensity > 0.35:
        r, g, b = unique
    elif intensity > 0.3:
        r, g, b = unique2
    elif intensity > 0.25:
        r, g, b = unique
    elif intensity > 0.2:
        r, g, b = unique2
    elif intensity > 0.15:
        r, g, b = unique
    elif intensity > 0.1:
        r, g, b = unique2
    else:
        r, g, b = unique


    b *= intensity
    g *= intensity
    r *= intensity

    if intensity > 0:
        return r, g, b
    else:
        return 0, 0, 0


def termic(renderer, **kwargs):

    u, v, w = kwargs['baryCoords']
    b, g, r = kwargs['color']
    nA, nB, nC = kwargs['normals']

    b /= 255
    g /= 255
    r /= 255

    nX = nA[0] * u + nB[0] * v + nC[0] * w
    nY = nA[1] * u + nB[1] * v + nC[1] * w
    nZ = nA[2] * u + nB[2] * v + nC[2] * w

    normal = (nX, nY, nZ)

    intensity = mt.dot(normal, renderer.directional_light)

    if intensity > 0.9:
        r, g, b = 234, 227, 217
    elif intensity > 0.8:
        r, g, b = 236, 220, 107
    elif intensity > 0.7:
        r, g, b = 238, 213, 70
    elif intensity > 0.6:
        r, g, b = 238, 167, 27
    elif intensity > 0.5:
        r, g, b = 238, 123, 28
    elif intensity > 0.4:
        r, g, b = 238, 66, 70
    elif intensity > 0.3:
        r, g, b = 148, 40, 85
    elif intensity > 0.2:
        r, g, b = 93, 37, 82
    else:
        r, g, b = 37, 35, 75

    b /= 255
    g /= 255
    r /= 255

    if intensity > 0:
        return r, g, b
    else:
        return 0, 0, 0


def photo(renderer, **kwargs):

    u, v, w = kwargs['baryCoords']
    b, g, r = kwargs['color']
    nA, nB, nC = kwargs['normals']

    b /= 255
    g /= 255
    r /= 255

    nX = nA[0] * u + nB[0] * v + nC[0] * w
    nY = nA[1] * u + nB[1] * v + nC[1] * w
    nZ = nA[2] * u + nB[2] * v + nC[2] * w

    normal = (nX, nY, nZ)

    intensity = mt.dot(normal, renderer.directional_light)

    if intensity > 0.85:
        r, g, b = 255, 255, 255
    elif intensity > 0.7:
        r, g, b = 191, 49, 6
    elif intensity > 0.6:
        r, g, b = 0, 3, 204
    elif intensity > 0.5:
        r, g, b = 142, 127, 0
    elif intensity > 0.4:
        r, g, b = 116, 27, 191
    elif intensity > 0.3:
        r, g, b = 0, 0, 0
    elif intensity > 0.2:
        r, g, b = 243, 128, 0
    elif intensity > 0.1:
        r, g, b = 0, 0, 12
    elif intensity > 0.05:
        r, g, b = 40, 40, 40
    else:
        r, g, b = 20, 20, 20

    b /= 255
    g /= 255
    r /= 255

    if intensity > 0:
        return r, g, b
    else:
        return 0, 0, 0


def desapering(renderer, **kwargs):
    u, v, w = kwargs['baryCoords']
    tA, tB, tC = kwargs['texCoords']
    b, g, r = kwargs['color']
    nA, nB, nC = kwargs['normals']
    minY, maxY, y = kwargs['yValues']

    porcentage = (y - minY) / (maxY - minY)

    tb, tg, tr = 0.3, 0.3, 0.3

    if porcentage > 0.9:
        pass
    elif porcentage > 0.8:
        return tr, tg, tb
    elif porcentage > 0.7:
        pass
    elif porcentage > 0.6:
        return tr, tg, tb
    elif porcentage > 0.5:
        pass
    elif porcentage > 0.4:
        return tr, tg, tb
    elif porcentage > 0.3:
        pass
    elif porcentage > 0.2:
        return tr, tg, tb
    elif porcentage > 0.1:
        pass
    else:
        return tr, tg, tb

    b /= 255
    g /= 255
    r /= 255

    if renderer.active_texture:
        tx = tA[0] * u + tB[0] * v + tC[0] * w
        ty = tA[1] * u + tB[1] * v + tC[1] * w
        texColor = renderer.active_texture.getColor(tx, ty)
    else:
        texColor = color(1, 1, 1)

    b *= texColor[0] / 255
    g *= texColor[1] / 255
    r *= texColor[2] / 255

    nX = nA[0] * u + nB[0] * v + nC[0] * w
    nY = nA[1] * u + nB[1] * v + nC[1] * w
    nZ = nA[2] * u + nB[2] * v + nC[2] * w

    normal = (nX, nY, nZ)

    intensity = mt.dot(normal, renderer.directional_light)

    b *= intensity
    g *= intensity
    r *= intensity

    if intensity > 0:
        return r, g, b
    else:
        return 0, 0, 0