from queue import Queue

def land_counter(map):
    mem = {};
    count = 0
    directs = [[1, 0], [0, 1], [-1, 0], [0, -1]]
    m = len(map)
    n = len(map[0])
    for i in range(len(map)):
        for j in range(len(map[i])):
            if map[i][j] == 1 and not mem.get("{}{}".format(i,j)):
                q = Queue();
                q.put([i, j])
                mem["{}{}".format(i, j)] = True
                count += 1
                while not q.empty():
                    x, y = q.get()
                    for direct in directs:
                        nx =  x + direct[0]
                        ny =  y + direct[1]
                        if nx < 0 or nx >= m or ny < 0 or ny >= n: continue
                        if mem.get("{}{}".format(nx,ny)): continue
                        mem["{}{}".format(nx, ny)] = True
                        if map[nx][ny] == 1: q.put([nx, ny])
    return count

map = [
    [1, 0, 0, 0, 0],
    [1, 0, 0, 1, 0],
    [1, 1, 0, 0, 0],
    [1, 1, 0, 1, 0],
    [1, 0, 0, 1, 1],
]

land_num = land_counter(map)
print(land_num)