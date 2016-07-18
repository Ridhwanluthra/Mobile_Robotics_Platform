from utils.structure import grid
from pi_arduino_interface import find_displacement
import search
from get_path import interpolate_path, plot_path

g = grid()
g.robolab()
grid = g.grid

init=[0,0]
goal = [0, len(grid[0])-1]

def run_motion_planning(grid, init, goal):
	list_of_xy = search.search(grid, init, goal)
	interpolated_xy = interpolate_path(list_of_xy)
	plot_path(list_of_xy, interpolated_xy)
	input_array = find_displacement(interpolated_xy)
	print input_array

run_motion_planning(grid, init, goal)