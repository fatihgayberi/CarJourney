from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import sys

CAR_X = 0  # arabanin x positionunu tutar
BIRD_X = -5  # kusun x positionunu tutar
TRANSATOR = 0  # kusun x positionunun degisimini saglar

def InitGL():
    glClearColor(1.0, 1.0, 1.0, 0.0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(-15.0, 15.0, -15.0, 15.0)
    glMatrixMode(GL_MODELVIEW)

# kusu cizer
def Bird():
    global BIRD_X
    global TRANSATOR

    SphereDraw(1.8, 0.5, 0, -5, 11, -1)

    # kusun surekli hareketini saglar
    if BIRD_X >= 11:
        TRANSATOR -= 0.003
    if BIRD_X <= -5:
        TRANSATOR += 0.003

    BIRD_X += TRANSATOR

# agaci cizer
def Tree():
    # agacin ustunu cizer
    glColor3f(0, 0.2, 0.05)
    glPushMatrix()
    glBegin(GL_TRIANGLES)
    glVertex2f(9.5, 4.0)
    glVertex2f(14.5, 4.0)
    glVertex2f(12.0, 13.0)
    glEnd()
    glPopMatrix()

    # agacin govdesini cizer
    QuadDraw(0.6, 0.2, 0, 11, -7, 11, 4, 13, 4, 13, -7)

# arabayi cizer
def Car():

    # ust kisim
    QuadDraw(0, 0, 1, -12.0, -1.0, -12.0, 2.0, -6.0, 2.0, -6.0, -1.0)

    # orta kisim
    QuadDraw(0.5, 0, 1, -14.0, -5.0, -14.0, -1.0, -4.0, -1.0, -4.0, -5.0)

    # on teker
    SphereDraw(0.0, 0.0, 0.0, -6, -6, -1)

    # arka teker
    SphereDraw(0.0, 0.0, 0.0, -12, -6, -1)

# Projedeki butun daireleri cizer
def SphereDraw(R, G, B, posX, posY, posZ):
    glColor3f(R, G, B)
    glPushMatrix()
    glTranslate(posX, posY, posZ)
    glutSolidSphere(1, 20, 20)
    glPopMatrix()

# Projedeki butun dortgenleri cizer
def QuadDraw(R, G, B, x1, y1, x2, y2, x3, y3, x4, y4):
    glColor3f(R, G, B)
    glPushMatrix()
    glBegin(GL_QUADS)
    glVertex2f(x1, y1)
    glVertex2f(x2, y2)
    glVertex2f(x3, y3)
    glVertex2f(x4, y4)
    glEnd()
    glPopMatrix()

def DrawGLScene():
    global CAR_X

    glClear(GL_COLOR_BUFFER_BIT)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

    Tree()  # agaci cizer
    QuadDraw(0, 1, 0, -15.0, -15.0, -15.0, -7.0, 15.0, -7.0, 15.0, -15.0)  # zemini cizdirir

    glPushMatrix()
    glTranslate(BIRD_X, 0, 0)  # kusun hareket etmesini saglar
    Bird()  # kusu cizer
    glPopMatrix()


    glPushMatrix()
    glTranslate(CAR_X, 0, 0)  # arabanin hareket etmesini saglar
    Car()  # arabayi cizer
    glPopMatrix()
    glutSwapBuffers()


def keyPressed(*args):
    global CAR_X

    # sol ok tusuna basilirsa ve ekrandan cikmiyorsa hareket etmesini saglar
    if args[0] == GLUT_KEY_LEFT and CAR_X >= 0:
        CAR_X += -0.4

    # sag ok tusuna basilirsa ve agaca carpmiyorsa hareket etmesini saglar
    elif args[0] == GLUT_KEY_RIGHT and CAR_X <= 14.5:
        CAR_X += 0.4

    glutPostRedisplay()


def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE)
    glutInitWindowSize(720, 540)
    glutInitWindowPosition(0, 0)
    glutCreateWindow("Car journey")
    glutDisplayFunc(DrawGLScene)
    glutIdleFunc(DrawGLScene)
    glutSpecialFunc(keyPressed)
    InitGL()
    glutMainLoop()


main()
