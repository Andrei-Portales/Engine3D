# Programa principal

from gl import Renderer

width = 960
height = 540

rd = Renderer(width, height)

rd.glClearColor(0, 0.3, 0)
rd.glClear()

rd.glColor(0.2, 1, 1)


rd.glViewPort(200, 200, 100, 100)

rd.glVertex(0, 0)
rd.glVertex(-1, -1)
rd.glVertex(1, 1)
rd.glVertex(-1, 1)
rd.glVertex(1, -1)


# for x in range(50, 200):
#     rd.glPoint(x, x)

rd.glFinish('output.bmp')
