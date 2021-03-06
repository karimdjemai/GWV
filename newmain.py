from Vertex import Vertex
from sys import getsizeof
import timeit

# every vertex in range
frontier = []
# the vertices that have already been seen
already_visited = []
# the portals in the current labyrinth
portal_list = []
# the labyrinth in machine readable format
world = []
# the goal vertex
goal_vertex = None


def define_world(sheet):
    global world
    print("Reading " + sheet)
    text_file = open(sheet, "r")
    lines = text_file.readlines()
    h, w = len(lines), len(lines[0]) - 1

    world = [[7 for x in range(w)] for y in range(h)]

    for line in range(len(lines)):
        for char in range(len(lines[line]) - 1):
            world[line][char] = lines[line][char]
    return world


def goal_found(vertex):
    return goal_vertex.x == vertex.x and goal_vertex.y == vertex.y


def append_neighbors(vertex):
    global world
    neighbors = [Vertex(vertex.x - 1, vertex.y, vertex),
                 Vertex(vertex.x + 1, vertex.y, vertex),
                 Vertex(vertex.x, vertex.y + 1, vertex),
                 Vertex(vertex.x, vertex.y - 1, vertex)]

    for neighbor in neighbors:
        if not Vertex.not_in(neighbor,portal_list):  # Wenn der Vertex in der Portalliste ist
            neighbor = Vertex.vertex_out_of_list(neighbor, portal_list).parent.set_parent(vertex)  # Setze den nachbarn auf den Ausgang des Portals
        if 'x' not in world[neighbor.y][neighbor.x] and Vertex.not_in(neighbor, frontier) and Vertex.not_in(neighbor, already_visited):
            frontier.append(neighbor)


# find s in the ascii chart to determine the start
def find_start():
    global world
    for line in range(len(world)):
        if 's' in world[line]:
            start_vertex = Vertex(world[line].index('s'), line, None)
            return start_vertex


# find g in the ascii chart to determine the start
def find_goal():
    global world
    for line in range(len(world)):
        if 'g' in world[line]:
            global goal_vertex
            goal_vertex = Vertex(world[line].index('g'), line, None)
            return goal_vertex


def find_portals():
    global world
    pl = []
    for pn in range(1, 6):  # search for portalnumber 1-5
        vertex1 = None
        vertex2 = None
        for li in range(len(world)):  # li = lineIndex
            if str(pn) in world[li]:
                if not vertex1:
                    vertex1 = Vertex(world[li].index(str(pn)), li, None)
                else:
                    vertex2 = Vertex(world[li].index(str(pn)), li, None)
        if vertex1:
            pl.append(vertex1.set_parent(vertex2))
            pl.append(vertex2.set_parent(vertex1))
    return pl


def heuristic_with_portals(start):
    global goal_vertex
    distances = [start.dist_man(goal_vertex)]  # Generate list of distances, direct and through all of the portals
    for portal_vertex in portal_list:
        dist = start.dist_man(portal_vertex) + portal_vertex.parent.dist_man(goal_vertex)  # Distance from start to portal_entrance + distance from portal_exit to goal
        distances.append(dist)
    return min(distances)  # return the minimum


def heuristic(vertex):
    return vertex.dist_man(goal_vertex)
                

def breadth_first_search():
    global frontier
    b_start = timeit.timeit()
    b_iterations = 0

    while frontier:
        vertex = frontier.pop(0)
        if goal_found(vertex):
            print("Found!")
            vertex.print_path()
            b_end = timeit.timeit()
            print(str(b_end - b_start) + " seconds")
            print(str(b_iterations) + " iterations needed")
            print(str(getsizeof(already_visited)) + " bytes")
            break
        else:
            append_neighbors(vertex)
            b_iterations += 1


def depth_first_search():
    global frontier, already_visited
    d_start = timeit.timeit()
    d_iterations = 0

    while frontier:
        vertex = frontier.pop(-1)
        already_visited.append(vertex)
        if goal_found(vertex):
            print("Found!")
            vertex.print_path()
            d_end = timeit.timeit()
            print(str(d_end - d_start) + " seconds")
            print(str(d_iterations) + " iterations needed")
            print(str(getsizeof(already_visited)) + " bytes")
            break
        else:
            append_neighbors(vertex)
            d_iterations += 1


def get_min_value(l):
    values = []

    for v in l:
        value = v.value
        values.append(value)

    min_value = min(values)
    index_min_value = values.index(min_value)

    return l[index_min_value]


def a_star_search():
    global frontier, already_visited
    a_start = timeit.timeit()
    a_iterations = 0

    while frontier:
        vertex = get_min_value(frontier)
        already_visited.append(vertex)
        vertex.distance_from_start += 1
        vertex.value = vertex.distance_from_start + heuristic_with_portals(vertex)

        if goal_found(vertex):
            print("Found!")
            vertex.print_path()
            a_end = timeit.timeit()
            print(str(a_end - a_start) + " seconds")
            print(str(a_iterations) + " iterations needed")
            print(str(getsizeof(already_visited)) + " bytes")
            break
        else:
            append_neighbors(vertex)
            a_iterations += 1


def display_world(path):
    global world
    for line in world:
        for vertex in path:
            if vertex[0][0] in world:
                print(vertex)
            else:
                print(line)


def startup(sheet, search_type):
    global world, already_visited, portal_list, frontier, goal_vertex
    s_start = timeit.timeit()

    world = define_world(sheet)
    start_vertex = find_start()
    goal_vertex = find_goal()
    portal_list = find_portals()
    append_neighbors(start_vertex)
    already_visited = [start_vertex]

    s_end = timeit.timeit()
    print("Startup needed: " + str(s_end - s_start) + " seconds \n")

    if search_type is "dfs":
        depth_first_search()
    elif search_type is "bfs":
        breadth_first_search()
    elif search_type is "a_star":
        a_star_search()
    else:
        return search_type + " not found"

    return world


print("\n A Stern")
startup("blatt4_environment_b.txt", "a_star")
print("\n Breitensuche")
startup("blatt4_environment_b.txt", "bfs")
print("\n Teiefensuche")
startup("blatt4_environment_b.txt", "dfs")
