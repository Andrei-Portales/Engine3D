from gl import Renderer, V2, color, V3
import time
from obj import Texture

width = 960
height = 540

rd = Renderer(width, height)

rd.glColor(1, 1, 1)

texture = Texture('textures/model.bmp')

rd.glLoadModelTriangle('models/model.obj', scale=V3(200, 200, 200), translate=V3(width/2, height / 2, 0), texture=texture)

rd.glFinish('lab_outputs/SR4FlatShadingTextures.bmp')
