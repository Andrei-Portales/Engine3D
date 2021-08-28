from gl import Renderer, color, V3
from obj import Texture
from shaders import *
import time

width = 2200
height = 2000

rd = Renderer(width, height)
rd.clear_color = color(0,0,0)
rd.glClear()

rd.active_texture = Texture('textures/model.bmp')


rd.active_shader = disappearing
rd.glLoadModelTriangle('models/model.obj',  scale=V3(2, 2, 2), translate= V3(-4.3, 2.5, -10), rotate = V3(0, 0, 0))

rd.active_shader = toon
rd.glLoadModelTriangle('models/model.obj',  scale=V3(2, 2, 2), translate= V3(-1.4, 2.5, -10), rotate = V3(0, 0, 0))

rd.active_shader = photo
rd.glLoadModelTriangle('models/model.obj',  scale=V3(2, 2, 2), translate= V3(1.4, 2.5, -10), rotate = V3(0, 0, 0))

rd.active_shader = static
rd.glLoadModelTriangle('models/model.obj',  scale=V3(2, 2, 2), translate= V3(4.3, 2.5, -10), rotate = V3(0, 0, 0))

rd.active_shader = zebra
rd.glLoadModelTriangle('models/model.obj',  scale=V3(2, 2, 2), translate= V3(-4.3, -2.5, -10), rotate = V3(0, 0, 0))

rd.active_shader = termic
rd.glLoadModelTriangle('models/model.obj',  scale=V3(2, 2, 2), translate= V3(-1.4, -2.5, -10), rotate = V3(0, 0, 0))

rd.active_shader = radioactive
rd.glLoadModelTriangle('models/model.obj',  scale=V3(2, 2, 2), translate= V3(1.4, -2.5, -10), rotate = V3(0, 0, 0))





rd.glFinish('lab_outputs/Lab2_Shaders.bmp')
