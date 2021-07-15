# Programa principal
from gl import Renderer, V2, color

width = 960
height = 540

rd = Renderer(width, height)

rd.glClearColor(0, 0, 0)
rd.glClear()

rd.glColor(1,1,1)

rd.glViewPort(200, 200, 100, 100)
rd.glVertex(0, 0)
rd.glVertex(0.5, 0.6)
rd.glVertex(0.2, 0.5)
rd.glVertex(0.1, 0.4)
rd.glVertex(0.7, 0.2)
# rd.glVertex(1, 1)



rd.glFinish('output.bmp')
