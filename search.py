"""
from utils.structure import grid

g = grid()
g.big_map()
g.add_obstacle(25,25,0,90)
g.add_obstacle(50,50,10,100)
g.add_obstacle(75,57,0,90)
grid = g.grid
#for i in range(len(grid)):
#	print grid[i]
"""
"""
grid = [[0,1,0,0,0,0],
		[0,1,0,0,0,0],
		[0,1,0,0,1,0],
		[0,1,0,0,1,0],
		[0,0,0,0,1,0]]

heuristic = [[9,8,7,6,5,4],
			 [8,7,6,5,4,3],
			 [7,6,5,4,3,2],
			 [6,5,4,3,2,1],
			 [5,4,3,2,1,0]]
"""
"""
heuristic = [[5,4,4,4,4,4],
			 [5,4,3,3,3,3],
			 [5,4,3,2,2,2],
			 [5,4,3,2,1,1],
			 [5,4,3,2,1,0]]
"""
init=[0,0]

goal = [0, len(grid[0])-1]


delta = [[-1,0],
		 [0,-1],
		 [1,0],
		 [0,1],
		 [-1,-1],
		 [-1,1],
		 [1,-1],
		 [1,1]]

#delta_name = ['^','<','v','>']

cost = 1


def check_all(grid, xy):
	i = xy[0]
	j = xy[1]
	h_count = xy[2] + 1

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


def build_heuristic(grid, goal):
	heuristic = [[-1 for row in range(len(grid[0]))] for col in range(len(grid))]
	#for i in range(len(heuristic)):
	#	print heuristic[i]
	x = goal[0]
	y = goal[1]
	heuristic[x][y] = 0
	dist = 0
	h_count = 0

	to_check = [[x, y, dist]]
	while to_check:
		current_xy = to_check.pop(0)
		#print 'xy: ', current_xy
		changes = check_all(heuristic, current_xy)
		#print 'changes: ', changes
		heuristic = changes[0]
		for i in range(len(changes[1])):
			to_check.append(changes[1][i])
	#for i in range(len(heuristic)):
	#	print heuristic[i]
	return heuristic

def search(grid, goal):
	heuristic = build_heuristic(grid, goal)
	closed = [[0 for row in range(len(grid[0]))] for col in range(len(grid))]
	
	closed[init[0]][init[1]] = 1
	
	expand = [[-1 for row in range(len(grid[0]))] for col in range(len(grid))]
	action = [[-1 for row in range(len(grid[0]))] for col in range(len(grid))]
	
	x = init[0]
	y = init[1]
	g = 0
	h = heuristic[x][y]
	f = g + h
	
	open = [[f,g,h,x,y]]
	
	found = False#flag that is set when search is complete
	resign = False#flag set if we can't find expand
	count = 0
	
	while not found and not resign:
		if len(open) == 0:
			resign = True
		else:
			open.sort()
			open.reverse()
			next = open.pop()
			x = next[3]
			y = next[4]
			g = next[1]
			expand[x][y] = count
			count += 1
			if x == goal[0] and y == goal[1]:
				found = True
			else:
				for i in range(len(delta)):
					x2 = x + delta[i][0]
					y2 = y + delta[i][1]
					if x2 >= 0 and x2 < len(grid) and y2 >=0 and y2<len(grid[0]):
						if closed[x2][y2] == 0 and grid[x2][y2] == 0:
							if i < 4:
								cost = 3.5
							else:
								cost = 5
							g2 = g + cost
							h2 = heuristic[x2][y2]
							f2 = g2 + h2
							open.append([f2, g2, h2, x2,y2])
							closed[x2][y2] = 1
							action[x2][y2] = i
	path = [[''] * len(grid[0]) for i in grid]
	x = goal[0]
	y = goal[1]
	path[x][y] = '*'
	x_cords = [x]
	y_cords = [y]

	while x != init[0] or y != init[1]:
		x2 = x - delta[action[x][y]][0]
		y2 = y - delta[action[x][y]][1]
		x_cords.append(x2)
		y_cords.append(y2)
		path[x2][y2] = 3
		x = x2
		y = y2
	x_cords.reverse()
	y_cords.reverse()
	#for row in path:
	#	print row
	print x_cords
	print y_cords
	return x_cords, y_cords