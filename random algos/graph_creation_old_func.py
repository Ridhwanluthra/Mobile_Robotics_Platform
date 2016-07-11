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