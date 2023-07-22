from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *


class node:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.dimention = [x, y, x + 1, y + 1]
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
        for node in maze:
            if node.x == 0:
                node.left = None
            else:
                node.left = maze[(node.x - 1) * height + node.y]

            if node.x == width - 1:
                node.right = None
            else:
                node.right = maze[(node.x + 1) * height + node.y]

            if node.y == 0:
                node.down = None
            else:
                node.down = maze[node.x * height + node.y - 1]

            if node.y == height - 1:
                node.up = None
            else:
                node.up = maze[node.x * height + node.y + 1]

        return maze


def init():
    glClearColor(0.0, 0.0, 0.0, 0.0)
    glMatrixMode(GL_PROJECTION)
    gluOrtho2D(-1, 11, -1, 11)
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
