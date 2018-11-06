from Vertex import Vertex

text_file = open("blatt3_environment.txt", "r")
lines = text_file.readlines()

h, w = len(lines), len(lines[0]) - 1

world = [[7 for x in range(w)] for y in range(h)]

for line in range(len(lines)):
    for char in range(len(lines[line])-1):
        world[line][char] = lines[line][char]
print(world)

# find s to determine startpos
for line in range(len(world)):
    if 's' in world[line]:
        startVertex = Vertex(world[line].index('s'), line, None)
        break


frontier = [startVertex]

def goalFound(vertex):
    return world[vertex.y][vertex.x] == 'g'

def appendNeighbors(vertex):
    neighbors = [Vertex(vertex.x - 1, vertex.y, vertex),
                 Vertex(vertex.x + 1, vertex.y, vertex),
                 Vertex(vertex.x, vertex.y + 1, vertex),
                 Vertex(vertex.x, vertex.y - 1, vertex)]

    for neighbor in neighbors:
        if world[neighbor.y][neighbor.x] != 'x' and Vertex.notIn(neighbor, frontier):
            frontier.append(neighbor)

def breadthFirstSearch():
    while frontier:
        #print("x: " + str(frontier[0].x) + " y: " + str(frontier[0].y))
        vertex = frontier.pop(0)
        if goalFound(vertex):
            print("found")
            vertex.printPath()
            break
        else:
            appendNeighbors(vertex)

def depthFirstSearch():
    while frontier:
        vertex = frontier.pop(-1)
        if goalFound(vertex):
            print("found")
            vertex.printPath()
            break
        else:
            appendNeighbors(vertex)


breadthFirstSearch()
frontier = [startVertex]
depthFirstSearch()