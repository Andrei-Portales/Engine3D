from gl import color
import a_math as mt
import random as rn


def generatePalette(c1, c2, count):
    palette = [()] * count
    palette[0] = c1
    palette[-1] = c2

    s1 = (c2[0] - c1[0]) / count + 1
    s2 = (c2[1] - c1[1]) / count + 1
    s3 = (c2[2] - c1[2]) / count + 1

    for i in range(1, count-1):
        r = int(c1[0] + (s1 * i))
        g = int(c1[1] + (s2 * i))
        b = int(c1[2] + (s3 * i))
        palette[i] = r, g, b

    return palette

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

    if intensity < 0:
        return 0,0,0

    colors = [(234, 227, 217), (236, 220, 107), (238, 213, 70), (238, 167, 27), (238, 123, 28), (238, 66, 70), (148, 40, 85), (93, 37, 82), (37, 35, 75), (30, 29, 61 )]
    colors.reverse()


    if intensity > 0.8:
        c1 = colors[0]
        c2 = colors[2]
        c3 = colors[4]
    elif intensity > 0.6:
        c1 = colors[2]
        c2 = colors[4]
        c3 = colors[6]
    elif intensity > 0.4:
        c1 = colors[4]
        c2 = colors[6]
        c3 = colors[8]
    elif intensity > 0.2:
        c1 = colors[6]
        c2 = colors[8]
        c3 = colors[9]
    else:
        c1 = colors[8]
        c2 = colors[9]
        c3 = colors[9]

    palette = generatePalette(c1, c2, 20)
    palette.reverse()

    palette[1] = ((palette[1][0] + palette[0][0]) / 2,
                  (palette[1][1] + palette[0][1]) / 2,
                  (palette[1][2] + palette[0][2]) / 2)

    palette[2] = ((palette[2][0] + palette[1][0]) / 2,
                  (palette[2][1] + palette[1][1]) / 2,
                  (palette[2][2] + palette[1][2]) / 2)


    palette[3] = ((palette[3][0] + palette[2][0]) / 2,
                  (palette[3][1] + palette[2][1]) / 2,
                  (palette[3][2] + palette[2][2]) / 2)

    palette[4] = ((palette[4][0] + palette[3][0]) / 2,
                  (palette[4][1] + palette[3][1]) / 2,
                  (palette[4][2] + palette[3][2]) / 2)

    p2 = generatePalette(c2, c3, 20)
    p2.reverse()

    palette[0] = ((palette[1][0] + p2[19][0]) / 2, 
                  (palette[1][1] + p2[19][1]) / 2, 
                  (palette[1][2] + p2[19][2]) / 2)

    position = abs(int((intensity * 100) % 20)) 

    if position < 0:
        position = 0

    r, g, b = palette[position]

    
    r = r if r <= 255 else 255
    g = g if r <= 255 else 255
    b = b if r <= 255 else 255

    b /= 255
    g /= 255
    r /= 255

    return r, g, b



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

    if intensity < 0:
        return 0,0,0

    colors = [(255, 255, 255),( 191, 49, 6), (0, 3, 204), (142, 127, 0), (116, 27, 191), (0, 0, 0), (243, 128, 0), (0, 0, 12), (40, 40, 40), (20, 20, 20)]

    if intensity > 0.8:
        c1 = colors[0]
        c2 = colors[1]
        c3 = colors[4]
    elif intensity > 0.6:
        c1 = colors[1]
        c2 = colors[4]
        c3 = colors[6]
    elif intensity > 0.4:
        c1 = colors[4]
        c2 = colors[6]
        c3 = colors[8]
    elif intensity > 0.2:
        c1 = colors[6]
        c2 = colors[8]
        c3 = colors[9]
    else:
        c1 = colors[8]
        c2 = colors[9]
        c3 = colors[9]

    palette = generatePalette(c1, c2, 20)
    palette.reverse()

    palette[1] = ((palette[1][0] + palette[0][0]) / 2,
                  (palette[1][1] + palette[0][1]) / 2,
                  (palette[1][2] + palette[0][2]) / 2)

    palette[2] = ((palette[2][0] + palette[1][0]) / 2,
                  (palette[2][1] + palette[1][1]) / 2,
                  (palette[2][2] + palette[1][2]) / 2)


    palette[3] = ((palette[3][0] + palette[2][0]) / 2,
                  (palette[3][1] + palette[2][1]) / 2,
                  (palette[3][2] + palette[2][2]) / 2)

    palette[4] = ((palette[4][0] + palette[3][0]) / 2,
                  (palette[4][1] + palette[3][1]) / 2,
                  (palette[4][2] + palette[3][2]) / 2)

    p2 = generatePalette(c2, c3, 20)
    p2.reverse()

    palette[0] = ((palette[1][0] + p2[19][0]) / 2, 
                  (palette[1][1] + p2[19][1]) / 2, 
                  (palette[1][2] + p2[19][2]) / 2)

    position = abs(int((intensity * 100) % 20)) 

    if position < 0:
        position = 0

    r, g, b = palette[position]

    
    r = r if r <= 255 else 255
    g = g if r <= 255 else 255
    b = b if r <= 255 else 255

    b /= 255
    g /= 255
    r /= 255

    return r, g, b


def disappearing(renderer, **kwargs):

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


def radioactive(renderer, **kwargs):

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

    yellow = 251/255, 1, 0

    r = ((1 - intensity) * yellow[0] + r) / 2
    g = ((1 - intensity) * yellow[1] + g) / 2
    b = ((1 - intensity) * yellow[2] + b) / 2

    if intensity > 0:
        return r, g, b
    else:
        return 93/255, 95/255, 0

