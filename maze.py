from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from pythonds import Stack
import random

class Node:
	def __init__(self, x, y):
		self.x = x
		self.y = y
		self.dimention = [x, y, x + 1, y + 1]
		self.walls = [True, True, True, True]
		self.up = None
		self.down = None
		self.left = None
		self.right = None
		self.visited = False

	def draw_node(self):
		glBegin(GL_LINES)
		if self.walls[0]:
			glVertex2f(self.dimention[0], self.dimention[3])
			glVertex2f(self.dimention[2], self.dimention[3])
		if self.walls[1]:
			glVertex2f(self.dimention[0], self.dimention[1])
			glVertex2f(self.dimention[2], self.dimention[1])
		if self.walls[2]:
			glVertex2f(self.dimention[0], self.dimention[1])
			glVertex2f(self.dimention[0], self.dimention[3])
		if self.walls[3]:
			glVertex2f(self.dimention[2], self.dimention[1])
			glVertex2f(self.dimention[2], self.dimention[3])
		glEnd()

class Maze:
	def __init__(self, width, height):
		self.width = width
		self.height = height
		self.wall = self.generate_walls(width, height)
		self.generate_maze(width, height)

	def generate_walls(self, width, height):
		wall = []
		for i in range(width):
			s_wall = []
			for j in range(height):
				s_wall.append(Node(i, j))
			wall.append(s_wall)
		return wall

	def get_neighbours(self, node):
		neighbours = []
		if node.x > 0:
			if not self.wall[node.x - 1][node.y].visited:
				neighbours.append(self.wall[node.x - 1][node.y])
		if node.x < self.width - 1:
			if not self.wall[node.x + 1][node.y].visited:
				neighbours.append(self.wall[node.x + 1][node.y])
		if node.y > 0:
			if not self.wall[node.x][node.y - 1].visited:
				neighbours.append(self.wall[node.x][node.y - 1])
		if node.y < self.height - 1:
			if not self.wall[node.x][node.y + 1].visited:
				neighbours.append(self.wall[node.x][node.y + 1])
		return neighbours

	def remove_wall(self, current, next):
		if current.x == next.x:
			if current.y > next.y:
				current.walls[1] = False
				next.walls[0] = False
				current.down = next
				next.up = current
			else:
				current.walls[0] = False
				next.walls[1] = False
				current.up = next
				next.down = current
		if current.y == next.y:
			if current.x > next.x:
				current.walls[2] = False
				next.walls[3] = False
				current.left = next
				next.right = current
			else:
				current.walls[3] = False
				next.walls[2] = False
				current.right = next
				next.left = current

	def generate_maze(self, width, height):
		stack = Stack()
		current = self.wall[0][0]
		current.visited = True
		stack.push(current)
		while not stack.isEmpty():
			current = stack.peek()
			neighbours = self.get_neighbours(current)
			if neighbours:
				next = random.choice(neighbours)
				self.remove_wall(current, next)
				stack.push(next)
				current = next
				current.visited = True
			else:
				current = stack.pop()

	def wall_print(self):
		for smaze in self.wall:
			for node in smaze:
				node.draw_node()
def init():
	glClearColor(0.0, 0.0, 0.0, 0.0)
	glMatrixMode(GL_PROJECTION)
	glLoadIdentity()
	gluOrtho2D(-1, 31, -1, 31)
	glMatrixMode(GL_MODELVIEW)

def draw():
	glPointSize(3.0)
	glClear(GL_COLOR_BUFFER_BIT)
	glColor3f(1.0, 1.0, 1.0)
	maze.wall_print()
	for s in maze.wall:
		for node in s:
			glColor3f(1.0, 0.0, 0.0)
			glBegin(GL_LINES)
			if node.up:
				glVertex2f(node.x + 0.5, node.y + .5)
				glVertex2f(node.up.x + 0.5, node.up.y + .5)
			if node.down:
				glVertex2f(node.x + 0.5, node.y + .5)
				glVertex2f(node.down.x + 0.5, node.down.y + .5)
			if node.left:
				glVertex2f(node.x + 0.5, node.y + .5)
				glVertex2f(node.left.x + 0.5, node.left.y + .5)
			if node.right:
				glVertex2f(node.x + 0.5, node.y + .5)
				glVertex2f(node.right.x + 0.5, node.right.y + .5)
			glEnd()
	glFlush()


if __name__ == "__main__":
	glutInit()
	glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
	glutInitWindowSize(800, 800)
	glutInitWindowPosition(100, 100)
	glutCreateWindow("Maze")
	init()

	# Create the maze object here, outside the draw function
	maze = Maze(30, 30)

	glutDisplayFunc(draw)
	glutMainLoop()
