from structure import grid, robot, movement

class wall_follower(object):
	def __init__(self, wall):
		self.wall = wall

	def check_left(self, robot_obj, grid_obj):
		if robot_obj.orientation == 'n':
			try:
				if robot_obj.y_temp == 0:
					return True
				elif grid_obj.grid[robot_obj.x_temp][robot_obj.y_temp - 1] == 1:
					return True
				else:
					return False
			except IndexError:
				return True
		elif robot_obj.orientation == 's':
			try:
				if grid_obj.grid[robot_obj.x_temp][robot_obj.y_temp + 1] == 1:
					return True
				else:
					return False
			except IndexError:
				return True
		elif robot_obj.orientation == 'w':
			try:
				if grid_obj.grid[robot_obj.x_temp + 1][robot_obj.y_temp] == 1:
					return True
				else:
					return False
			except IndexError:
				return True
		elif robot_obj.orientation == 'e':
			try:
				if robot_obj.x_temp == 0:
					return True
				elif grid_obj.grid[robot_obj.x_temp - 1][robot_obj.y_temp] == 1:
					return True
				else:
					return False
			except IndexError:
				return True
		else:
			print "the orientation should be n,e,w,s only"

	def check_right(self, robot_obj, grid_obj):
		if robot_obj.orientation == 'n':
			try:
				if grid_obj.grid[robot_obj.x_temp][robot_obj.y_temp + 1] == 1:
					return True
				else:
					return False
			except IndexError:
				return True
		elif robot_obj.orientation == 's':
			try:
				if robot_obj.y_temp == 0:
					return True
				elif grid_obj.grid[robot_obj.x_temp][robot_obj.y_temp - 1] == 1:
					return True
				else:
					return False
			except IndexError:
				return True
		elif robot_obj.orientation == 'w':
			try:
				if robot_obj.x_temp == 0:
					return True
				elif grid_obj.grid[robot_obj.x_temp - 1][robot_obj.y_temp] == 1:
					return True
				else:
					return False
			except IndexError:
				return True
		elif robot_obj.orientation == 'e':
			try:
				if grid_obj.grid[robot_obj.x_temp + 1][robot_obj.y_temp] == 1:
					return True
				else:
					return False
			except IndexError:
				return True
		else:
			print "the orientation should be n,e,w,s only"

	def check_ahead(self, robot_obj, grid_obj):
		if robot_obj.orientation == 'n':
			try:
				if robot_obj.x_temp == 0:
					return False
				elif grid_obj.grid[robot_obj.x_temp - 1][robot_obj.y_temp] == 1:
					return False
				else:
					return True
			except IndexError:
				return False
		elif robot_obj.orientation == 's':
			try:
				if grid_obj.grid[robot_obj.x_temp + 1][robot_obj.y_temp] == 1:
					return False
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
				else:
					return True
			except IndexError:
				return False
		elif robot_obj.orientation == 'e':
			try:
				if grid_obj.grid[robot_obj.x_temp][robot_obj.y_temp + 1] == 1:
					return False
				else:
					return True
			except IndexError:
				return False
		else:
			print "the orientation should be n,e,w,s only"

	def follow(self, robot_obj, grid_obj):
		move = movement(robot_obj, grid_obj)

		if self.wall == 'left':
			if check_ahead and not(check_left):
				move.move()

		elif self.wall == 'right':
			if check_ahead and not(check_right):
				move.move()