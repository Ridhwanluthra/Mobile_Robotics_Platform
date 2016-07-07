from structure import grid

def check_collision_after_prelim(grid,x1,y1,x2,y2):
    for x in range(x1,x2+1):
        m = abs((y2-y1)/(x2-x1))
        c = y1 - m*x1
        y = m*x + c
        try:
            if grid[x][y] == 1:
                return False
        except IndexError:
            #print x, y
            return False
    return True

def convert_coords(x1, y1, x2, y2):
    cell_size = 35
    x1 = x1*cell_size + 35.000/2
    y1 = y1*cell_size + 35.000/2
    x2 = x2*cell_size + 35.000/2
    y2 = y2*cell_size + 35.000/2
    return x1, y1, x2, y2

def check_boundry(x, y):
    tr_x = x
    tl_x = x
    bl_x = x+1
    br_x = x+1
    tr_y = y+1
    tl_y = y
    bl_y = y
    br_y = y+1

    line_segment_top = 



def no_collision(grid, x1, y1, x2, y2):
    x1, y1, x2, y2 = convert_coords(x1,y1,x2,y2)