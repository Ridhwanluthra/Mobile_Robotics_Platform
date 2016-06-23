class map(object):
	def __init__(self):
		self.map = [[0,0,0,0,1,0],[0,0,1,0,0,0],[1,1,1,0,0,0],[1,0,0,0,1,1],[0,0,0,0,0,0]]

	def set_map(self, map):
		self.map = map

	def set_goal(self, x, y):
		self.map[x][y] = 5

	def create_map(self):
		pass


class robot(object):
	def __init__(self):
		self.x = 0
		self.y = 0
		self.fx = 0
		self.fy = 0

	def set_start(self, x, y):
		self.x = x
		self.y = y

	def set_goal(self, map_obj, x, y):
		self.fx = x
		self.fy = y
		map_obj.set_goal(self.fx, self.fy)


def move():
	map = map()
	bot = robot()
	bot.set_start(0, 0)
	bot.set_goal(map, 10, 10)
	y_direction = bot.fy - bot.y
	x_direction = bot.fx - bot.x
