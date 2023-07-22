from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *


class Node:
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
        #self.generate()

    def generate_walls(self, width, height):
        wall = []
        for i in range(width):
            s_wall = []
            for j in range(height):
                s_wall.append(Node(i, j))
            wall.append(s_wall)
        for smaze in wall:
            for node in smaze:
                if node.x == 0:
                    node.left = None
                else:
                    node.left = wall[node.x - 1][node.y]
                if node.x == self.width - 1:
                    node.right = None
                else:
                    node.right = wall[node.x + 1][node.y]
                if node.y == 0:
                    node.down = None
                else:
                    node.down = wall[node.x][node.y - 1]
                if node.y == self.height - 1:
                    node.up = None
                else:
                    node.up = wall[node.x][node.y + 1]
        return wall

    def maze_print(self):
        for smaze in self.wall:
            for node in smaze:
                glBegin(GL_LINES)
                glVertex2f(node.dimention[0], node.dimention[1])
                glVertex2f(node.dimention[2], node.dimention[1])
                glVertex2f(node.dimention[2], node.dimention[1])
                glVertex2f(node.dimention[2], node.dimention[3])
                glVertex2f(node.dimention[2], node.dimention[3])
                glVertex2f(node.dimention[0], node.dimention[3])
                glVertex2f(node.dimention[0], node.dimention[3])
                glVertex2f(node.dimention[0], node.dimention[1])
                glEnd()


def init():
    glClearColor(0.0, 0.0, 0.0, 0.0)
    glMatrixMode(GL_PROJECTION)
    gluOrtho2D(-1, 11, -1, 11)
    glMatrixMode(GL_MODELVIEW)


def draw():
    glLoadIdentity()
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0, 1.0, 1.0)
    maze.maze_print()
    glFlush()


if __name__ == "__main__":
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(500, 500)
    glutInitWindowPosition(100, 100)
    glutCreateWindow("Maze")
    init()

    # Create the maze object here, outside the draw function
    maze = Maze(10, 10)

    glutDisplayFunc(draw)
    glutMainLoop()
