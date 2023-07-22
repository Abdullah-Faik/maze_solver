from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

class node:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.up = None
        self.down = None
        self.left = None
        self.right = None
        self.visited = False

class Maze:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.wall = self.generate_walls(width, height)
        self.generate()

    def generate_walls(self, width, height):
        maze = []
        for i in range(width):
            for j in range(height):
                maze.append(node(i, j))
        return maze


def init():
    glClearColor(0.0, 0.0, 0.0, 0.0)
    glMatrixMode(GL_PROJECTION)
    gluOrtho2D(-1.0, 1.0, -1.0, 1.0)
    glMatrixMode(GL_MODELVIEW)

def draw():
    glLoadIdentity()




def main():
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(500, 500)
    glutInitWindowPosition(100, 100)
    glutCreateWindow("Maze")
    glutDisplayFunc(draw)
    init()
    glutMainLoop()

main()

