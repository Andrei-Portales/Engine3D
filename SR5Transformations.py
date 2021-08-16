from gl import Renderer, V2, color, V3, V4
from obj import Texture


def draw(output, camPosition, rotation):
    width = 1000
    height = 800

    rd = Renderer(width, height)
    rd.glColor(1, 1, 1)
    texture = Texture('textures/model.bmp')

    modelPosition = V3(0, 0, 0)

    rd.glLookAt(modelPosition, camPosition)
    rd.glLoadModelTriangle('models/model.obj', scale=V3(2, 2, 2), translate=modelPosition, texture=texture, rotate = rotation)


    rd.glFinish(output)


draw('lab_outputs/SR5Transformations/mediumshot.bmp', V3(0.5, 0, 6), V3(0, 0, 5))
draw('lab_outputs/SR5Transformations/lowangle.bmp', V3(0, -2, 4), V3(0, 0, 0))
draw('lab_outputs/SR5Transformations/highangle.bmp', V3(0, 3, 5.5), V3(0, 0, 0))
draw('lab_outputs/SR5Transformations/dutchangle.bmp', V3(4, 0, 6), V3(-20, 0, 0))
