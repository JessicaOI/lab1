#Jessica Ortiz 20192

import struct

def char(c):
    # 1 byte
    return struct.pack('=c'. c.encode('ascii'))


def word(w):
    # 2 bytes
    return struct.pack('=h', w)

def dword(d):
    # 4 bytes
    return struct.pack('=l',d)


def color(r,g,b):
    # Creacion de Color (255 deja usar todos los colores)
    return bytes([int(b*255),
                int(g*255),
                int(r*255)])


class Render(object):
    # Constructor
    def __init__(self):
        self.viewPortX = 0
        self.viewPortY = 0
        self.height = 0
        self.width = 0
        #los colores van de 0 a 1 
        self.clearColor = color(0, 0, 0)

        #aqui especificamos el color de los puntitos
        self.current_color = color(1, 1, 1)
        self.framebuffer = []
       
        self.glViewport(0,0,self.width, self.height)
        self.glClear() 

    def glCreateWindow(self, width, height):
        self.width = width
        self.height = height
        self.glClear()

    def glViewport(self, x, y, width, height):
        self.vpX = x
        self.vpY = y
        self.vpWidth = width
        self.vpHeight = height
    
    def glClear(self):
        self.framebuffer = [[self.clearColor for x in range(self.width+1)]
                            for y in range(self.height+1)]

    #el color del fondo o pantalla
    def glClearColor(self, r, g, b):
        self.clearColor = color(r, b, g)
        self.glClear()

    def glColor(self, r, g, b):
        self.current_color = color(r, g, b)

    def glPoint(self, x, y, color):
        x = int(round((x+1) * self.width / 2))
        y = int(round((y+1) * self.height / 2))
        try:
                self.framebuffer[x][y] = color
        except IndexError:
                print("\nFuera de los límites de la imagen\n")

    #color del area donde trabajaremos
    def glClearViewport(self, Acolor = None):
        #le sumamos uno porque el range no toma el ultimo elemento recorrido
        for x in range(self.vpX, self.vpX + self.vpWidth + 1):
            for y in range(self.vpY, self.vpY + self.vpHeight + 1):
                self.glVertex(x,y,Acolor)


    def glVertex(self, x, y, Acolor=None):
        if (0 <= x < self.width) and (0 < + y < self.height):
            self.framebuffer[x][y] = Acolor or self.current_color
    
    def glVertex_vp(self, ndcX, ndcY, Acolor=None):
        if ndcX < -1 or ndcX > 1 or ndcY < -1 or ndcY > 1 :
            return 

        x = (ndcX + 1) * (self.vpWidth / 2) + self.vpX
        y = (ndcY + 1) * (self.vpHeight / 2) + self.vpY

        x = int(x)
        y = int(y)
        self.glVertex(x,y,Acolor)

    #Rellena la figura indicada
    def glFillPolygon(self, polygon):
            #Point-in-Polygon (PIP) Algorithm
            for y in range(self.height):
                for x in range(self.width):
                    i = 0
                    j = len(polygon) - 1
                    draw_point = False
                    #Verifica si el punto está entre los límites
                    for i in range(len(polygon)):
                        if (polygon[i][1] < y and polygon[j][1] >= y) or (polygon[j][1] < y and polygon[i][1] >= y):
                            if polygon[i][0] + (y - polygon[i][1]) / (polygon[j][1] - polygon[i][1]) * (polygon[j][0] - polygon[i][0]) < x:
                                draw_point = not draw_point
                        j = i
                    if draw_point:
                        self.glPoint((float(x)/(float(self.width)/2))-1,(float(y)/(float(self.height)/2))-1,self.current_color)

    # Función para crear la imagen
    def glFinish(self, filename):
        with open(filename, 'bw') as file:
            # Header
            file.write(bytes('B'.encode('ascii')))
            file.write(bytes('M'.encode('ascii')))

            # file size
            file.write(dword(14 + 40 + self.height * self.width * 3))
            file.write(dword(0))
            file.write(dword(14 + 40))

            # Info Header
            file.write(dword(40))
            file.write(dword(self.width))
            file.write(dword(self.height))
            file.write(word(1))
            file.write(word(24))
            file.write(dword(0))
            file.write(dword(self.width * self.height * 3))
            file.write(dword(0))
            file.write(dword(0))
            file.write(dword(0))
            file.write(dword(0))

            # Color table
            for y in range(self.height):
                for x in range(self.width):
                    file.write(self.framebuffer[x][y])
            file.close()

    