from utils.structure import grid, robot

class scan_grid(object):
	def scan(self):
		pass

	def scan_x(self):
		bot = robot()
		grid = grid()
		grid.robolab()

		bot.set_goal(grid, 0, 9)

		rows = len(grid.grid)
		columns = len(grid.grid[0])

		for i in range(0, rows):
			counter = 0
			for j in range(bot.y, bot.fy):
				if grid.grid[i][j] == 1:
					break
				elif grid.grid[i][j] == 0:
					counter += 1
			dmap = [[]]

	def create_dict_x(self, grid):
		dict_map_x = {}

		rows = len(grid.grid)
		columns = len(grid.grid)

		for i in range(0, rows):
			dict_map_x[i] = []
			for j in range(0, columns):
				if grid.grid[i][j] == 0:
					dict_map_x[i].append(j)

	def find_path(self):
		for i in range(bot.y_temp, bot.fy):
			if i in dict_map_x[bot.x_temp]:
				that means go here
				