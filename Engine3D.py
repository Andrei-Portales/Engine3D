# Programa principal
from gl import Renderer, V2, color


width = 960
height = 800


rd = Renderer(width, height)

rd.glColor(0, 0, 0)


rd.glLoadModel('models/face.obj', scale=V2(30, 30), translate=V2(width/2, height/4 - 145))



rd.glFinish('output.bmp')
