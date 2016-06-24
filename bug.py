from structure import robot, grid, movement
class bug(object):
	def move_x(self, bot, grid):
		y_direction = bot.fy - bot.y_temp
		x_direction = bot.fx - bot.x_temp
		if x_direction >= 0:
			for i in range(bot.y_temp, bot.fy):
				if grid.grid[bot.x_temp][bot.y_temp] != 1 or grid.grid[bot.x_temp][bot.y_temp] != 5:
					grid.grid[bot.x_temp][bot.y_temp] = 3
					bot.y_temp += 1
					y_direction = bot.fy - bot.y_temp
					x_direction = bot.fx - bot.x_temp
				elif grid.grid[bot.x_temp][bot.y_temp] == 5:
					print "goal reached"
				else:
					if y_direction >= 0:
						for j in range(bot.x_temp, bot.fx):
							if grid.grid[bot.x_temp][bot.y_temp] != 1 or grid.grid[bot.x_temp][bot.y_temp] != 5:
								grid.grid[bot.x_temp][bot.y_temp] = 4
								bot.x_temp += 1
								y_direction = bot.fy - bot.y_temp
								x_direction = bot.fx - bot.x_temp
							elif grid.grid[bot.x_temp][bot.y_temp] == 5:
								return "goal reached"
							else:
								pass
					elif y_direction < 0:
						for j in range(bot.x_temp, bot.fy):
							if grid.grid[bot.x_temp][bot.y_temp] != 1 or grid.grid[bot.x_temp][bot.y_temp] != 5:
								grid.grid[bot.x_temp][bot.y_temp] = 3
								bot.x_temp -= 1
								y_direction = bot.fy - bot.y_temp
								x_direction = bot.fx - bot.x_temp
							elif grid.grid[bot.x_temp][bot.y_temp] == 5:
								return "goal reached"
							else:
								pass
		elif x_direction < 0:
			for i in range(bot.y_temp, bot.fy):
				if grid.grid[bot.x_temp][bot.y_temp] != 1 or grid.grid[bot.x_temp][bot.y_temp] != 5:
					grid.grid[bot.x_temp][bot.y_temp] = 3
					bot.y_temp -= 1
					y_direction = bot.fy - bot.y_temp
					x_direction = bot.fx - bot.x_temp
				elif grid.grid[bot.x_temp][bot.y_temp] == 5:
					return "goal reached"
				else:
					if y_direction >= 0:
						for j in range(bot.x_temp, bot.fx):
							if grid.grid[bot.x_temp][bot.y_temp] != 1 or grid.grid[bot.x_temp][bot.y_temp] != 5:
								grid.grid[bot.x_temp][bot.y_temp] = 3
								bot.x_temp += 1
								y_direction = bot.fy - bot.y_temp
								x_direction = bot.fx - bot.x_temp
							elif grid.grid[bot.x_temp][bot.y_temp] == 5:
								return "goal reached"
							else:
								pass
					elif y_direction < 0:
						for j in range(bot.x_temp, bot.fy):
							if grid.grid[bot.x_temp][bot.y_temp] != 1 or grid.grid[bot.x_temp][bot.y_temp] != 5:
								grid.grid[bot.x_temp][bot.y_temp] = 3
								bot.x_temp -= 1
								y_direction = bot.fy - bot.y_temp
								x_direction = bot.fx - bot.x_temp
							elif grid.grid[bot.x_temp][bot.y_temp] == 5:
								return "goal reached"
							else:
								pass



	def find_path(self):
		lab_grid = grid()
		bot = robot()
		bot.set_origin(0, 0)
		bot.set_goal(lab_grid,0,9)
		y_direction = bot.fy - bot.y
		x_direction = bot.fx - bot.x
		if x_direction > y_direction:
			move_x()