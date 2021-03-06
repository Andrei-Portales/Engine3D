from gl import Renderer, V2, color


width = 960
height = 800

rd = Renderer(width, height)

rd.glColor(1, 1, 1)

rd.glLoadModel('models/face.obj', scale=V2(30, 30), translate=V2(width/2, height/4 - 145))

rd.glFinish('lab_outputs/SR3ObjModels.bmp')
