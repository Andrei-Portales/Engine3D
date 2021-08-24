# Programa principal
from gl import Renderer, V2, color, V3, V4
from obj import Texture
from shaders import *
import time


width = 1500
height = 1300


rd = Renderer(width, height)

# rd.curr_color = color(0,1,0)

rd.clear_color = color(0.3,0.3,0.3)
rd.glClear()

rd.active_texture = Texture('textures/model.bmp')

# modelPosition = V3(0, 0, -10)

# rd.glLookAt(modelPosition, V3(-4, 4, 0))


rd.active_shader = flat
rd.glLoadModelTriangle('models/model.obj', scale=V3(1.5, 1.5, 1.5), translate=V3(-4, 3, -10), rotate = V3(0, 0, 0))

rd.active_shader = gourad
rd.glLoadModelTriangle('models/model.obj', scale=V3(1.5, 1.5, 1.5), translate=V3(0, 3, -10), rotate = V3(0, 0, 0))

rd.active_shader = phong
rd.glLoadModelTriangle('models/model.obj',  scale=V3(1.5, 1.5, 1.5), translate= V3(4, 3, -10), rotate = V3(0, 0, 0))

rd.active_shader = unlit
rd.glLoadModelTriangle('models/model.obj',  scale=V3(1.5, 1.5, 1.5), translate= V3(-4, 0, -10), rotate = V3(0, 0, 0))

rd.active_shader = toon
rd.glLoadModelTriangle('models/model.obj',  scale=V3(1.5, 1.5, 1.5), translate= V3(0, 0, -10), rotate = V3(0, 0, 0))

rd.active_shader = photo # rainbow
rd.glLoadModelTriangle('models/model.obj',  scale=V3(1.5, 1.5, 1.5), translate= V3(4, 0, -10), rotate = V3(0, 0, 0))

rd.active_shader = static
rd.glLoadModelTriangle('models/model.obj',  scale=V3(1.5, 1.5, 1.5), translate= V3(-4, -3.3, -10), rotate = V3(0, 0, 0))

rd.active_shader = zebra
rd.glLoadModelTriangle('models/model.obj',  scale=V3(1.5, 1.5, 1.5), translate= V3(0, -3.3, -10), rotate = V3(0, 0, 0))

rd.active_shader = termic
rd.glLoadModelTriangle('models/model.obj',  scale=V3(1.5, 1.5, 1.5), translate= V3(4, -3.3, -10), rotate = V3(0, 0, 0))


rd.glFinish('output.bmp')
