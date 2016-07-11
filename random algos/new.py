
mapp = [[0,0,0,0,1,5],[0,0,1,0,0,0],[1,1,1,0,0,0],[1,0,0,0,1,1],[0,0,0,0,0,0]]
#mapp = [[0,1,0,0,0,1],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[1,0,0,0,0,1]]
"""
values represent:
0=free path
1=blocked path 
3=valid path
4=invalid path
5=goal
"""
ends = 0
def fill_dead_ends():
    global mapp
    rows = len(mapp)
    columns = len(mapp[0])
    global ends
    ends = 0
    for i in range(0,rows):
        for j in range(0,columns):
            counter = 0
            adj = [1,1,1,1]
            if mapp[i][j] == 1 or mapp[i][j] == 4:
                continue
            if i-1 >= 0:
                if mapp[i-1][j] == 1 or mapp[i-1][j] == 4:
                    counter = counter + 1
                else:
                    adj[0] = 0
            else:
                counter = counter + 1

            if i+1 < rows:
                if mapp[i+1][j] == 1 or mapp[i+1][j] == 4:
                    counter = counter + 1
                else:
                    adj[1] = 0
            else:
                counter = counter + 1

            if j-1 >= 0:
                if mapp[i][j-1] == 1 or mapp[i][j-1] == 4:
                    counter = counter + 1
                else:
                    adj[2] = 0
            else:
                counter = counter + 1        

            if j+1 < columns:
                if mapp[i][j+1] == 1 or mapp[i][j+1] == 4:
                    counter = counter + 1
                else:
                    adj[3] = 0
            else:
                counter = counter + 1

            if counter >= 3:
                mapp[i][j] = 4
                #print i,j
                ends = ends + 1
    print ends
    print_map()
    if ends != 0:
        fill_dead_ends()
    #return ends

def run():
    x = 1
    while x != 0:
        fill_dead_ends()

def find_path(cx, cy):
    global mapp
    rows = len(mapp)
    columns = len(mapp[0])
    if (not((cx < rows and cx >= 0) and (cy < columns and cy >= 0))):
    	return False
    if (mapp[cx][cy]==5):
    	return True
    if (mapp[cx][cy]!=0):
    	return False
    mapp[cx][cy] = 3
    if (find_path(cx-1,cy) == True):
        return True
    if (find_path(cx,cy+1) == True):
    	return True
    if (find_path(cx+1,cy) == True):
    	return True
    if (find_path(cx,cy-1) == True):
    	return True
    mapp[cx][cy] = 0
    return False

def print_map():
	global mapp
	rows = len(mapp)
	for i in range(0,rows):
		print mapp[i]

def find_all_paths(ex,ey):
    global mapp
    rows = len(mapp)
    columns = len(mapp[0])

    for i in range(0,rows):
        for j in range(0,columns):
            if mapp[i][j] != 1 or mapp[i][j] != 4:
                continue
            find_path(i,j)
