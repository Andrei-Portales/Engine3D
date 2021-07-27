from gl import Renderer, V2, color


width = 960
height = 800

rd = Renderer(width, height)

rd.glColor(1, 1, 1)

def draw(points, color=color(1,1,1)):
    lines = []

    for p in range(len(points)):
        p1 = points[p]
        p2 = points[(p + 1) if p < len(points) - 1 else 0]

        lines.append(rd.glLine(V2(p1[0], p1[1]), V2(p2[0], p2[1]), returnPoints=True))
    rd.glfillPolygon(lines, color)


draw([(165, 380), (185, 360), (180, 330), (207, 345), (233, 330), (230, 360), (250, 380), (220, 385), (205, 410), (193, 383)], color(1,0,0)) # estrella
draw([(321, 335), (288, 286), (339, 251), (374, 302)], color(0,1,0)) # cuadrado
draw([(377, 249), (411, 197), (436, 249)], color(0,0,1)) # triangulo
draw([(413, 177), (448, 159), (502, 88), (553, 53), (535, 36), (676, 37), (660, 52),(750, 145), (761, 179), (672, 192), (659, 214), (615, 214), (632, 230), (580, 230),(597, 215), (552, 214), (517, 144), (466, 180)], color(1,1,0)) # tetera
draw([(682, 175), (708, 120), (735, 148), (739, 170)], color(0,0,0)) # hoyo en tetera


rd.glFinish('lab_outputs/Lab1_FillingAnyPolygon.bmp')
