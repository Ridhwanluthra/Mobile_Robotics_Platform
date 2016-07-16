from utils.structure import grid

def create_dict(grid):
	dict_map = {}

	rows = len(grid)
	columns = len(grid)

	for i in range(0, rows):
		for j in range(0, columns):
			index = int(str(i) + str(j))
			if grid[i][j] == 0:
				dict_map[index] = set([])
				try:
					if i == 0:
						pass
					elif grid[i-1][j] == 0:
						dict_map[index].add(int(str(i-1) + str(j)))
					if grid[i+1][j] == 0:
						dict_map[index].add(int(str(i+1) + str(j)))
					if j == 0:
						pass
					elif grid[i][j-1] == 0:
						dict_map[index].add(int(str(i) + str(j-1)))
					if grid[i][j+1] == 0:
						dict_map[index].add(int(str(i) + str(j+1)))
				except ValueError:
					pass
				except IndexError:
					pass
	return dict_map

"""graph = {1: set([2, 3]),
         2: set([1, 4, 5]),
         3: set([1, 6]),
         4: set([2]),
         5: set([2, 6]),
         6: set([3, 5])}
"""
grid = grid()
grid.robolab()
graph = create_dict(grid.grid)
print graph

def bfs_paths(graph, start, goal):
	counter = 0
	queue = [(start, [start])]
	while queue:
		counter += 1
		print counter
		(vertex, path) = queue.pop(0)
		for next in graph[vertex] - set(path):
			if next == goal:
				yield path + [next]
			else:
				queue.append((next, path + [next]))


# [['A', 'C', 'F'], ['A', 'B', 'E', 'F']]
#for i in bfs_paths(graph, 0, 9):
#	print i
"""
def shortest_path(graph, start, goal):
    try:
        return next(bfs_paths(graph, start, goal))
    except StopIteration:
        return None

print shortest_path(graph, 1, 6)
"""