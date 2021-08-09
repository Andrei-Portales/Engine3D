# Programa principal
from gl import Renderer, V2, color, V3
import time
from obj import Texture


width = 960
height = 540


rd = Renderer(width, height)

rd.glColor(1, 1, 1)

texture = Texture('textures/model.bmp')


# rd.glLoadModel('models/face.obj', scale=V2(70, 70), translate=V2(width/2, 100), fill=True)

rd.glLoadModelTriangle('models/model.obj', scale=V3(200, 200, 200), translate=V3(width/2, height / 2, 0), texture=texture)


# rd.glTriangle_bc(V2(10, 10), V2(190, 10), V2(100, 190), _color=color(1, 0, 0))


rd.glFinish('output.bmp')
