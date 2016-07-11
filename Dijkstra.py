"""
graph = ((0,1,0,0,0,0,),
        (1,0,1,0,1,0,),
        (0,1,0,0,0,1,),
        (0,0,0,0,1,0,),
        (0,1,0,1,0,0,),
        (0,0,1,0,0,0,),)"""

from utils.structure import grid
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
    c = 0
    for i in range(0, rows):
        for j in range(0, columns):
            index = int(str(i).zfill(2) + str(j).zfill(2))
            
            if grid[i][j] == 0:
            	print index
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

def dijkstra(Graph, source):
    '''
        +   +---+---+
        | 0   1   2 |
        +---+   +   +
        | 3   4 | 5  
        +---+---+---+
 
        >>> graph = (        # or ones on the diagonal
        ...     (0,1,0,0,0,0,),
        ...     (1,0,1,0,1,0,),
        ...     (0,1,0,0,0,1,),
        ...     (0,0,0,0,1,0,),
        ...     (0,1,0,1,0,0,),
        ...     (0,0,1,0,0,0,),
        ... )
        ...
        >>> Dijkstra(graph, 0)
        ([0, 1, 2, 3, 2, 3], [1e+140, 0, 1, 4, 1, 2])
        >>> display_solution([1e+140, 0, 1, 4, 1, 2])
        5<2<1<0
    '''
    # Graph[u][v] is the weight from u to v (however 0 means infinity)
    start_time = time.time()

    infinity = float('infinity')
    n = len(graph)
    dist = [infinity]*n   # Unknown distance function from source to v
    previous = [infinity]*n # Previous node in optimal path from source
    dist[source] = 0        # Distance from source to source
    Q = list(range(n)) # All nodes in the graph are unoptimized - thus are in Q
    while Q:           # The main loop
        u = min(Q, key = lambda n:dist[n])                 # vertex in Q with smallest dist[]
        Q.remove(u)
        if dist[u] == infinity:
            break # all remaining vertices are inaccessible from source
        for v in range(n):               # each neighbor v of u
            if Graph[u][v] and (v in Q): # where v has not yet been visited
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

def get_solution(predecessor):
    array = []
    cell = 9
    while cell:
        array.append(cell)
        cell = predecessor[cell]
    print array
    print(0)

grid = grid()
#grid.big_map()
grid.robolab()
grid.print_grid()
graph = create_graph(grid.grid)
#print graph
dist, previous = dijkstra(graph, 0)
#print len(dist)
#print len(previous)
print dist, previous
display_solution(previous)