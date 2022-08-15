#Jessica Ortiz 20192

from poligonos import Render
w = 1000
h = 1000
rend = Render()
rend.glCreateWindow(w, h)

rend.glViewport(int(0),
                int(0), 
                int(w/1), 
                int(h/1))

def glInit():
    return rend


if __name__ == '__main__':

    rend = glInit()
    rend.glClear()

    #poligono1: estrella
    #color
    rend.glColor(1, 0.93, 0.25)
    polygon1 = ((165, 380), (185, 360), (180, 330), (207, 345), (233, 330), (230, 360), (250, 380), (220, 385), (205, 410), (193, 383))
    rend.glFillPolygon(polygon1)

    #poligono3: cuadrado
    #color
    rend.glColor(0.5, 0.2, 0.87)
    polygon2 = ((321, 335), (288, 286), (339, 251), (374, 302))
    rend.glFillPolygon(polygon2)

    #poligono3: triangulo
    #color
    rend.glColor(0.3, 0.1, 0.26)
    polygon3 = ((377, 249), (411, 197), (436, 249))
    rend.glFillPolygon(polygon3)


    #poligono4: tetera
    #color
    rend.glColor(0.2,0.7,1)
    polygon4 = ((413, 177), (448, 159), (502, 88), (553, 53), (535, 36), (676, 37), (660, 52), (750, 145), (761, 179), (672, 192), (659, 214), (615, 214), (632, 230), (580, 230), (597, 215), (552, 214), (517, 144), (466, 180))
    rend.glFillPolygon(polygon4)

    #poligono4: hoyo tetera
    #color
    rend.glColor(0, 0, 0)
    polygon5 = ((682, 175), (708, 120), (735, 148), (739, 170))
    rend.glFillPolygon(polygon5)

    #Output rend
    rend.glFinish("imagen.bmp")