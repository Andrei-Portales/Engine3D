# Programa principal
from gl import Renderer, V2, color, V3, V4

from obj import Texture


width = 1000
height = 800


rd = Renderer(width, height)

rd.glColor(1, 1, 1)

texture = Texture('textures/model.bmp')

modelPosition = V3(0, 0, -10)

rd.glLookAt(modelPosition, V3(-5, 5, 0))

rd.glLoadModelTriangle('models/model.obj', scale=V3(2, 2, 2), translate=modelPosition, texture=texture, rotate = V3(0, 0, 0))


rd.glFinish('output.bmp')
