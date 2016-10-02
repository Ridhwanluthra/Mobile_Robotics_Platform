
#mapp = [[0,0,0,0,1,5],[0,0,1,0,0,0],[0,1,1,0,0,0],[0,0,0,0,1,1],[0,0,0,0,0,0]]
mapp = [[0,0,0,0,1,5],[0,0,1,0,1,0],[0,0,0,0,1,0],[1,0,0,0,1,0],[0,0,0,0,0,0]]
"""
values represent:
0=free path
1=blocked path 
3=valid path
4=invalid path
5=goal
"""
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

print_map()
find_path(4,0)
print_map()