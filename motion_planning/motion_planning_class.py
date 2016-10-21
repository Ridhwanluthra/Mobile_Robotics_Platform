class motion_planning(object):
	def __init__(self, grid_map):
		self.grid = grid_map

	def set_init(self, x, y):
		self.init[0] = x
		self.init[1] = y

	def set_goal(self, x, y):
		self.goal[0] = x
		self.goal[1] = y

	def check_possible_next(self, grid, current_location):
		self.i = current_location[0]
		self.j = current_location[1]
		h_count = current_location[2] + 1

		to_return = []

		if i == 0:
			pass
		elif grid[i-1][j] == -1:
			grid[i-1][j] = h_count
			to_return.append([i-1, j, h_count])

		if i == len(grid) - 1:
			pass
		elif grid[i+1][j] == -1:
			grid[i+1][j] = h_count
			to_return.append([i+1, j, h_count])

		if j == 0:
			pass
		elif grid[i][j-1] == -1:
			grid[i][j-1] = h_count
			to_return.append([i, j-1, h_count])

		if j == len(grid[0]) - 1:
			pass
		elif grid[i][j+1] == -1:
			grid[i][j+1] = h_count
			to_return.append([i, j+1, h_count])

		#diagonal elements
		
		if i == 0 or j == len(grid[0]) - 1:
			pass
		elif grid[i-1][j+1] == -1:
			grid[i-1][j+1] = h_count
			to_return.append([i-1, j+1, h_count])

		if i == 0 or j == 0:
			pass
		elif grid[i-1][j-1] == -1:
			grid[i-1][j-1] = h_count
			to_return.append([i-1, j-1, h_count])

		if i == len(grid) - 1 or j == len(grid[0]) - 1:
			pass
		elif grid[i+1][j+1] == -1:
			grid[i+1][j+1] = h_count
			to_return.append([i+1, j+1, h_count])

		if j == 0 or i == len(grid) - 1:
			pass
		elif grid[i+1][j-1] == -1:
			grid[i+1][j-1] = h_count
			to_return.append([i+1, j-1, h_count])

		return grid, to_return