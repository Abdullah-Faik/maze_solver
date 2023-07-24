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
		self.walls = [True, True, True, True]     # top , bottom, left, right
		self.up = None
		self.down = None
		self.left = None
		self.right = None
		self.visited = False
		if x == 0 and y == 0:
			self.walls[2] = False
		if x == 39 and y == 39:
			self.walls[3] = False

	def get_nighbours(self):
		n = []
		if self.up:
			n.append(self.up)
		if self.down:
			n.append(self.down)
		if self.left:
			n.append(self.left)
		if self.right:
			n.append(self.right)
		return n

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
		self.set_unvisited()

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

	def print_paths(self):
		for s in self.wall:
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

	def set_unvisited(self):
		for s_wall in self.wall:
			for node in s_wall:
				node.visited = False


class Player:
	def __init__(self, n: Node):
		self.node = n
		self.neighbours = n.get_nighbours()
		self.dimention = [n.x, n.y, n.x + 1, n.y + 1]
		self.node.visited = True

	def draw_player(self):
		glBegin(GL_QUADS)
		glVertex2f(self.dimention[0], self.dimention[1])
		glVertex2f(self.dimention[0], self.dimention[3])
		glVertex2f(self.dimention[2], self.dimention[3])
		glVertex2f(self.dimention[2], self.dimention[1])
		glEnd()

	def move(self):
		n = self.neighbours
		for node in n:
			if node.visited:
				n.remove(node)
		if n != []:
			self.node = random.choice(n)
			self.node.visited = True
			self.neighbours = self.node.get_nighbours()
			self.dimention = [self.node.x, self.node.y,
							  self.node.x + 1, self.node.y + 1]
			self.draw_player()


def init():
	glClearColor(0.0, 0.0, 0.0, 0.0)
	glMatrixMode(GL_PROJECTION)
	glLoadIdentity()
	gluOrtho2D(-1, 21, -1, 21)
	glMatrixMode(GL_MODELVIEW)


x = 0


def draw():
	global x
	glPointSize(3.0)
	glClear(GL_COLOR_BUFFER_BIT)
	glColor3f(1.0, 1.0, 1.0)
	maze.wall_print()
	# maze.print_paths()

	glColor3f(0.0, 1.0, 0.0)
	player.move()
	glutSwapBuffers()


def timer(value):
	draw()
	glutTimerFunc(1000, timer, 0)


if __name__ == "__main__":
	glutInit()
	glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
	glutInitWindowSize(800, 800)
	glutInitWindowPosition(0, 0)
	glutCreateWindow("Maze")
	init()

	# Create the maze object here, outside the draw function
	maze = Maze(20, 20)
	player = Player(maze.wall[0][0])

	glutDisplayFunc(draw)
	glutTimerFunc(1000, timer, 0)
	glutMainLoop()
