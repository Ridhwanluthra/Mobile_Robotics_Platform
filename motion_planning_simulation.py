from utils.structure import grid
import motion_planning.search as se
from modules.get_smooth_path import interpolate_path, plot_path, plot_interpolated_path, extract_xy

g = grid()
g.robolab()
grid = g.grid
#grid = [[1,0,0,0,1,0,1,0,0,0,1],[1,0,0,1,0,0,0,0,0,0,0],[0,1,0,0,0,0,0,1,0,0,0],[0,0,0,0,0,1,0,0,1,1,0],[1,0,1,0,0,0,0,0,1,0,1],[0,0,0,0,0,1,0,0,1,0,0],[1,0,0,1,1,0,0,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,0],[0,0,1,0,0,0,0,0,0,0,1],[1,0,0,0,1,0,1,0,1,0,0],[0,0,0,1,0,0,1,0,0,0,1]]
init = [0,0]
goal = [0, len(grid[0])-1]

def run_motion_planning(grid, init, goal):
	list_of_xy = se.search(grid, init, goal)
	print "search done!"
	interpolated_xy = interpolate_path(list_of_xy)
	#interpolated_xy = extract_xy(interpolated_xy)
	print "interpolation done!"
	plot_path(list_of_xy, interpolated_xy)

	plot_interpolated_path(interpolated_xy)
	input_array = 0
	print input_array

run_motion_planning(grid, init, goal)