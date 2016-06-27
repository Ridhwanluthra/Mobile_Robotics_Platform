
graph = ((0,1,0,0,0,0,),
        (1,0,1,0,1,0,),
        (0,1,0,0,0,1,),
        (0,0,0,0,1,0,),
        (0,1,0,1,0,0,),
        (0,0,1,0,0,0,),)

from structure import grid
import time

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
            index = int(str(i).zfill(2) + str(j).zfill(2))
            if grid[i][j] == 0:
                try:
                    if i == 0:
                        pass
                    elif grid[i-1][j] == 0:
                        graph[index][int(str(i-1).zfill(2) + str(j).zfill(2))] = 1

                    if grid[i+1][j] == 0:
                        graph[index][int(str(i+1).zfill(2) + str(j).zfill(2))] = 1

                    if j == 0:
                        pass
                    elif grid[i][j-1] == 0:
                        graph[index][int(str(i).zfill(2) + str(j-1).zfill(2))] = 1

                    if grid[i][j+1] == 0:
                        graph[index][int(str(i).zfill(2) + str(j+1).zfill(2))] = 1

                except ValueError:
                    pass
                except IndexError:
                    pass
    elapsed_time_convert = time.time() - start_time
    print "convert =" ,elapsed_time_convert
    return graph

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

    while unoptimized_vertices:
        # vertex in Q with smallest dist[]
        u = min(unoptimized_vertices, key = lambda n:dist[n])
        print u
        unoptimized_vertices.remove(u)
        if dist[u] == infinity:
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
    cell = 5
    while cell:
        print cell
        cell = predecessor[cell]
    print(0)

#grid = grid()
#grid.big_map()
#grid.print_grid()
#graph = create_graph(grid.grid)
#print graph
dist, previous = prm(graph, 0)
#print len(dist)
#print len(previous)
#print dist, previous
display_solution(previous)