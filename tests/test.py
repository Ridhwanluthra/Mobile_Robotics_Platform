#from wall_follow import wall_follower
from structure import robot, grid
from bug import bug

grid = grid()
grid.robolab()

bot = robot()

bot.set_origin(0, 0)
bot.set_goal(grid,0,9)

bug = bug()
bug.move_x(bot,grid)

grid.print_grid()

print bot.x_temp, bot.y_temp



#test = wall_follower('left')
#print test.check_left(bot, grid)


