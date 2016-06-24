class grid(object):
	def __init__(self):
		self.grid = []

	def example_grid(self):
		self.set_grid([[0,0,0,0,1,0],[0,0,1,0,0,0],[1,1,1,0,0,0],[1,0,0,0,1,1],[0,0,0,0,0,0]])

	def set_grid(self, grid):
		self.grid = grid

	def set_goal(self, x, y):
		self.grid[x][y] = 5

	#taking in height and width to create an oject with grid of said h and w
	def create_grid(self, height, width):
		for i in range(0, height):
			#creating a row
			self.grid.append([])
			for j in range(0, width):
				#seting all coloums in that row to 0 to denote free space
				self.grid[i].append(0)

	def add_obstacle(self, xinitial, xfinal, yinitial, yfinal):
		#checking to see if x or y start and end are same
		if xinitial == xfinal:
			xfinal += 1
		if yinitial == yfinal:
			yfinal += 1		
		#setting the range taken as input to 1 to denote obstacles
		for i in range(xinitial, xfinal):
			for j in range(yinitial, yfinal):
				self.grid[i][j] = 1
	def add_single_obstacle(self, x, y):
		self.grid[x][y] = 1

	def robolab(self):
		self.create_grid(10,10)
		self.add_obstacle(5,5,0,4)
		self.add_obstacle(5,5,5,8)
		self.add_obstacle(0,6,5,5)
		self.add_obstacle(0,4,7,7)
		self.add_single_obstacle(5,7)
		#self.print_grid()

	#prints the grid in a more human readable form
	def print_grid(self):
		rows = len(self.grid)
		for i in range(0,rows):
			print self.grid[i]


class robot(object):
	x_temp = 0
	y_temp = 0
	orientation = 'n'
	def __init__(self):
		self.x = 0
		self.y = 0
		self.fx = 0
		self.fy = 0

	def set_origin(self, x, y):
		self.x = x
		self.y = y

	def set_goal(self, grid_obj, x, y):
		self.fx = x
		self.fy = y
		grid_obj.set_goal(self.fx, self.fy)

	def set_orientation(self, orientation):
		self.orientation = orientation

class movement(object):
	def __init__(self, robot_obj, grid_obj):
		self.bot = robot_obj
		self.grid = grid_obj

	def check_orientation(self):
		pass

	def up(self):
		robot_obj.x_temp -= 1
		robot_obj.set_orientation('n')
	def left(self):
		robot_obj.y_temp -= 1
		robot_obj.set_orientation('w')
	def right(self):
		robot_obj.y_temp += 1
		robot_obj.set_orientation('e')
	def down(self):
		robot_obj.x_temp += 1
		robot_obj.set_orientation('s')
	def move(self):
		if self.bot.orientation == 'n':
			self.bot.x_temp -= 1
		elif self.bot.orientation == 's':
			self.bot.x_temp += 1
		elif self.bot.orientation == 'w':
			self.bot.y_temp -= 1 
		elif self.bot.orientation == 'e':
			self.bot.y_temp += 1
		self.grid.print_grid()
		print 'next'
	def turn_left(self):
		if self.bot.orientation == 'n':
			self.bot.orientation = 'w'
		elif self.bot.orientation == 's':
			self.bot.orientation = 'e'
		elif self.bot.orientation == 'w':
			self.bot.orientation = 's'
		elif self.bot.orientation == 'e':
			self.bot.orientation = 'n'
	def turn_right(self):
		if self.bot.orientation == 'n':
			self.bot.orientation = 'e'
		elif self.bot.orientation == 's':
			self.bot.orientation = 'w'
		elif self.bot.orientation == 'w':
			self.bot.orientation = 'n'
		elif self.bot.orientation == 'e':
			self.bot.orientation = 's'