"""
graph = ((0,1,0,0,0,0,),
        (1,0,1,0,1,0,),
        (0,1,0,0,0,1,),
        (0,0,0,0,1,0,),
        (0,1,0,1,0,0,),
        (0,0,1,0,0,0,),)
"""
from structure import grid
import time

"""
def no_collision(grid, x1, y1, x2, y2):
    if grid[x2][y2] == 1 or grid[x1][y1] == 1:
        return False

    for i in range(x1,x2):
        for j in range(y1,y2):
            if grid[i][j] == 1:
                return False
    return True
"""
def no_collision(grid, x1, y1, x2, y2):
    if y2-y1 == 0:
        for x in range(x1, x2):
            if grid[x][y1]:
                return False
        return True
    try:
        m = (y2-y1)/(x2-x1)
    except ZeroDivisionError:
        for y in range(y1, y2):
            if grid[x1][y] == 1:
                return False
        return True

    for x in range(x1,x2):
        m = abs((y2-y1)/(x2-x1))
        y = m*x
        try:
            if grid[x][y] == 1:
                return False
        except IndexError:
            print x, y
            return True
    return True

def create_graph(grid):
    graph = []

    rows = len(grid)
    columns = len(grid)

    start_time = time.time()

    for i in range(0, rows*columns):
        graph.append([])
        for j in range(0, rows*columns):
            graph[i].append(0)

    elapsed_time_empty = time.time() - start_time

    print "empty =" ,elapsed_time_empty

    start_time = time.time()

    for i in range(0, rows):
        for j in range(0, columns):
            if grid[i][j] == 0:
                index = int(str(i) + str(j))
                if i-3 >= 0:
                    low_i = i-3
                else:
                    low_i = 0

                if j-3 >= 0:
                    low_j = j-3
                else:
                    low_j = 0

                if i+3 < rows:
                    high_i = i+3
                else:
                    high_i = rows-1

                if j+3 < columns:
                    high_j = j+3
                else:
                    high_j = columns-1
                for x in range(low_i, high_i):
                    for y in range(low_j, high_j):
                        if no_collision(grid,i,j,x,y):
                            graph[index][int(str(x) + str(y))] = 1

    elapsed_time_convert = time.time() - start_time
    print "convert =" ,elapsed_time_convert
    return graph
"""
def create_graph(grid):
    graph = []

    rows = len(grid)
    columns = len(grid[])

    start_time = time.time()

    for i in range(0, rows*columns):
        graph.append([])
        for j in range(0, rows*columns):
            graph[i].append(0)

    elapsed_time_empty = time.time() - start_time

    print "empty =" ,elapsed_time_empty

    start_time = time.time()

    for i in range(0, rows):
        for j in range(0, columns):
            index = int(str(i) + str(j))
            if grid[i][j] == 0:
                try:
                    r = 1
                    if i == 0:
                        pass
                    elif grid[i-r][j] == 0:
                        graph[index][int(str(i-r) + str(j))] = 1

                    if grid[i+r][j] == 0:
                        graph[index][int(str(i+r) + str(j))] = 1

                    if j == 0:
                        pass
                    elif grid[i][j-r] == 0:
                        graph[index][int(str(i) + str(j-r))] = 1

                    if grid[i][j+r] == 0:
                        graph[index][int(str(i) + str(j+r))] = 1
                    
                    #diagonal elements
                    if i == 0:
                        pass
                    elif grid[i-r][j+r] == 0:
                        graph[index][int(str(i-r) + str(j+r))] = 1

                    if i == 0 or j == 0:
                        pass
                    elif grid[i-r][j-r] == 0:
                        graph[index][int(str(i-r) + str(j-r))] = 1

                    if grid[i+r][j+r] == 0:
                        graph[index][int(str(i+r) + str(j+r))] = 1

                    if j == 0:
                        pass
                    elif grid[i+r][j-r] == 0:
                        graph[index][int(str(i+r) + str(j-r))] = 1
                    
                except ValueError:
                    pass
                except IndexError:
                    pass
    elapsed_time_convert = time.time() - start_time
    print "convert =" ,elapsed_time_convert
    return graph
"""
def prm(Graph, source):
    start_time = time.time()

    infinity = float('infinity')
    n = len(graph)
    #empty list for distances from source
    dist = [infinity]*n
    #empty list for the previous node in the path
    previous = [infinity]*n
    dist[source] = 0
    unoptimized_vertices = list(range(n))
    count = 0
    while unoptimized_vertices:
        # vertex in Q with smallest dist[]
        u = min(unoptimized_vertices, key = lambda n: dist[n])
        unoptimized_vertices.remove(u)
        count += 1
        if dist[u] == infinity:
            #print "not possible after: ", count
            break # all remaining vertices are inaccessible from source
        for v in range(n):               # each neighbor v of u
            if Graph[u][v] and (v in unoptimized_vertices): # where v has not yet been visited
                alt = dist[u] + Graph[u][v]
                if alt < dist[v]:       # Relax (u,v,a)
                    dist[v] = alt
                    previous[v] = u
    elapsed_time_dijkstras = time.time() - start_time
    print "algo =" ,elapsed_time_dijkstras
    return dist, previous

def display_solution(predecessor):
    cell = 9
    while cell:
        print cell
        cell = predecessor[cell]
    print(0)

grid = grid()
#grid.big_map()
grid.robolab()
#grid.example_grid()
grid.print_grid()
graph = create_graph(grid.grid)
dist, previous = prm(graph, 0)
#print graph
#print len(dist)
#print len(previous)
#print dist, previous
display_solution(previous)