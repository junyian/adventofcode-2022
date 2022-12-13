from pprint import pprint

lines = open("input2.txt").readlines()

def normalize(c):
    if ord(c) >= ord('a') and ord(c) <= ord('z'):
        return ord(c) - ord('a') + 1
    elif c=='S':
        return 1
    elif c=='E':
        return ord('z') - ord('a') + 1

def printmap(map):
    for rows in map:
        print(rows)

startpos, endpos = [0,0], [0,0]

map = []
for i,l in enumerate(lines):
    for j,c in enumerate(l.strip()):
        if c=='S':
            startpos = [i, j]
        elif c=='E':
            endpos = [i, j]
    map.append(list(normalize(c) for c in l.strip()))
maxrow, maxcol = len(map), len(map[0])
# print(maxrow, maxcol)
# printmap(map)

# Build the graph
graph = {}
# pprint(graph)

queue = []
queue.append(startpos)

while len(queue) > 0:
    # print("----------")
    x, y = list(queue.pop(0))
    if str([x,y]) not in graph.keys():
        graph[str([x,y])] = []

        v = map[x][y]
        # print([x,y], v)
        
        if [x,y] != endpos:
            # Left
            nx, ny = x, y-1
            if ny >= 0 and map[nx][ny] <= v+1:
                graph[str([x,y])].append([nx, ny])
                if str([nx,ny]) not in graph.keys() and [nx, ny] not in queue:
                    queue.append([nx, ny])
            # Right
            nx, ny = x, y+1
            if ny < maxcol and map[nx][ny] <= v+1:
                graph[str([x,y])].append([nx, ny])
                if str([nx,ny]) not in graph.keys() and [nx, ny] not in queue:
                    queue.append([nx, ny])
            # Up
            nx, ny = x-1, y
            if nx >= 0 and map[nx][ny] <= v+1:
                graph[str([x,y])].append([nx, ny])
                if str([nx,ny]) not in graph.keys() and [nx, ny] not in queue:
                    queue.append([nx, ny])
            # Down
            nx, ny = x+1, y
            if nx < maxrow and map[nx][ny] <= v+1:
                graph[str([x,y])].append([nx, ny])
                if str([nx,ny]) not in graph.keys() and [nx, ny] not in queue:
                    queue.append([nx, ny])

    # pprint(graph)
    # print(queue)

    # input()

# pprint(graph)

def shortest_path(graph, startpos, endpos):
    # Find shortest path
    path_list = [[startpos]]
    path_index = 0
    previous_nodes = { str(startpos) }

    while path_index < len(path_list):
        current_path = path_list[path_index]
        last_node = current_path[-1]
        next_nodes = graph[str(last_node)]
        if endpos in next_nodes:
            current_path.append(endpos)
            return current_path
        for next_node in next_nodes:
            # print(next_node)
            if str(next_node) not in previous_nodes:
                new_path = current_path[:]
                new_path.append(next_node)
                path_list.append(new_path)
                previous_nodes.add(str(next_node))
        path_index += 1

part1 = shortest_path(graph, startpos, endpos)
# print(part1)
print(len(part1)-1)

startpositions = []
for x in range(maxrow):
    for y in range(maxcol):
        if map[x][y] == 1:
            startpositions.append([x,y])
# print(startpositions)

steps = []
for sp in startpositions:
    step = shortest_path(graph, sp, endpos)
    if step is not None:
        steps.append(len(step)-1)
print(min(steps))