# Programa principal
from gl import Renderer, V2, color

width = 960
height = 540

rd = Renderer(width, height)

rd.glClearColor(1, 1, 1)
rd.glClear()



# rd.glViewPort(200, 200, 100, 100)



rd.glColor(1, 1, 1)

# for x in range(960):
#     for y in range(60):
#         rd.glPoint(x, y)

# rd.glLine(V2(2, 5), V2(900, 420), color=color(1, 0, 0))
# rd.glLine(V2(0, 0), V2(40, 500), color=color(0, 1, 0))
# rd.glLine(V2(900, 500), V2(600, 100), color=color(0, 0, 1))
# rd.glLine(V2(200, 400), V2(500, 400), color=color(0.2, 0.2, 1))

rd.glViewPort(20, 20, 200, 200)

rd.glColor(0, 0, 0)
rd.glVertex(0, 0)
rd.glVertex(-1, -1)
rd.glVertex(1, 1)
rd.glVertex(-1, 1)
rd.glVertex(1, -1)

rd.glLine(V2(200, 400), V2(200, 100), color=color(0.2, 0.2, 1))



rd.glFinish('output.bmp')
