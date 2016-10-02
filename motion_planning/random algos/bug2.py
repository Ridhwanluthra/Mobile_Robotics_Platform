from structure import movement
from structure import robot, grid

def check_ahead(robot_obj, grid_obj):
		if robot_obj.orientation == 'n':
			try:
				if robot_obj.x_temp == 0:
					return False
				elif grid_obj.grid[robot_obj.x_temp - 1][robot_obj.y_temp] == 1:
					return False
				elif grid_obj.grid[robot_obj.x_temp - 1][robot_obj.y_temp] == 5:
					return 'end'
				else:
					return True
			except IndexError:
				return False
		elif robot_obj.orientation == 's':
			try:
				if grid_obj.grid[robot_obj.x_temp + 1][robot_obj.y_temp] == 1:
					return False
				elif grid_obj.grid[robot_obj.x_temp + 1][robot_obj.y_temp] == 5:
					return 'end'
				else:
					return True
			except IndexError:
				return False
		elif robot_obj.orientation == 'w':
			try:
				if robot_obj.y_temp == 0:
					return False
				elif grid_obj.grid[robot_obj.x_temp][robot_obj.y_temp - 1] == 1:
					return False
				elif grid_obj.grid[robot_obj.x_temp][robot_obj.y_temp - 1] == 5:
					return 'end'
				else:
					return True
			except IndexError:
				return False
		elif robot_obj.orientation == 'e':
			try:
				if grid_obj.grid[robot_obj.x_temp][robot_obj.y_temp + 1] == 1:
					return False
				elif grid_obj.grid[robot_obj.x_temp][robot_obj.y_temp + 1] == 5:
					return 'end'
				else:
					return True
			except IndexError:
				return False
		else:
			print "the orientation should be n,e,w,s only"



def move_x(bot, grid):
		y_direction = bot.fy - bot.y_temp
		x_direction = bot.fx - bot.x_temp
		move = movement(bot, grid)
		if x_direction >= 0:
			bot.set_orientation = 'e'
			for i in range(bot.y_temp, bot.fy):
				if check_ahead(bot, grid) == 'end':
					print 'reached the goal'
				elif check_ahead(bot, grid):
					grid.grid[bot.x_temp][bot.y_temp + 1] = 3
					move.move()
					y_direction = bot.fy - bot.y_temp
					x_direction = bot.fx - bot.x_temp
				else:
					if y_direction >= 0:
						move.turn_right()
						if check_ahead(bot, grid) == 'end':
							print 'reached the goal'
						elif check_ahead(bot, grid):
							grid.grid[bot.x_temp + 1][bot.y_temp] = 3
							move.move()
							y_direction = bot.fy - bot.y_temp
							x_direction = bot.fx - bot.x_temp
					elif y_direction < 0:
						move.turn_left()
						if check_ahead(bot, grid) == 'end':
							print 'reached the goal'
						elif check_ahead(bot, grid):
							grid.grid[bot.x_temp - 1][bot.y_temp] = 3
							move.move()
							y_direction = bot.fy - bot.y_temp
							x_direction = bot.fx - bot.x_temp

		if x_direction < 0:
			bot.set_orientation = 'w'
			for i in range(bot.y_temp, bot.fy):
				if check_ahead(bot, grid) == 'end':
					print 'reached the goal'
				elif check_ahead(bot, grid):
					grid.grid[bot.x_temp][bot.y_temp - 1] = 3
					move.move()
					y_direction = bot.fy - bot.y_temp
					x_direction = bot.fx - bot.x_temp
				else:
					if y_direction >= 0:
						move.turn_left()
						if check_ahead(bot, grid) == 'end':
							print 'reached the goal'
						elif check_ahead(bot, grid):
							grid.grid[bot.x_temp + 1][bot.y_temp] = 3
							move.move()
							y_direction = bot.fy - bot.y_temp
							x_direction = bot.fx - bot.x_temp
					elif y_direction < 0:
						move.turn_right()
						if check_ahead(bot, grid) == 'end':
							print 'reached the goal'
						elif check_ahead(bot, grid):
							grid.grid[bot.x_temp - 1][bot.y_temp] = 3
							move.move()
							y_direction = bot.fy - bot.y_temp
							x_direction = bot.fx - bot.x_temp

grid = grid()
grid.robolab()

bot = robot()

bot.set_origin(0, 0)
bot.set_goal(grid,0,9)

move_x(bot,grid)

grid.print_grid()

print bot.x_temp, bot.y_temp