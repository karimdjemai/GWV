from Vertex import Vertex
import re

# every vertex in range
frontier = []
# the vertices that have already been seen
already_visited = []
# the portals in the current labyrinth
portal_list = []
# the labyrinth in machine readable format
world = []


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
    global world
    return world[vertex.y][vertex.x] == 'g'


def append_neighbors(vertex):
    global world
    neighbors = [Vertex(vertex.x - 1, vertex.y, vertex),
                 Vertex(vertex.x + 1, vertex.y, vertex),
                 Vertex(vertex.x, vertex.y + 1, vertex),
                 Vertex(vertex.x, vertex.y - 1, vertex)]
    for neighbor in neighbors:
        if 'x' not in world[neighbor.y][neighbor.x] and Vertex.not_in(neighbor, frontier) and Vertex.not_in(neighbor, already_visited):
            frontier.append(neighbor)


# find s in the ascii chart to determine the start
def find_start():
    global world
    for line in range(len(world)):
        if 's' in world[line]:
            start_vertex = Vertex(world[line].index('s'), line, None)
            return start_vertex


def find_portals():
    global portal_list, world
    iterator = 0
    for line in world:
        if '1' in line:
            portal_list.append(Vertex(line.index('1'), iterator, None))
        if '2' in line:
            portal_list.append(Vertex(line.index('2'), iterator, None))
        iterator += 1


def breadth_first_search():
    global frontier
    while frontier:
        # print("x: " + str(frontier[0].x) + " y: " + str(frontier[0].y))
        vertex = frontier.pop(0)
        if goal_found(vertex):
            print("found")
            vertex.print_path()
            break
        elif Vertex(vertex.x, vertex.y, None) in portal_list:
            already_visited.append()
            # TODO add the recognition of portals and add the corresponding portal (out)
            # to the end of the frontier as well as its neighbours
            # elif Vertex(vertex.x, vertex.y, none) in portal_list
            #       add Vertex to frontier
            #       set portal in as parent
        else:
            append_neighbors(vertex)


def depth_first_search():
    global frontier, already_visited
    while frontier:
        vertex = frontier.pop(-1)
        already_visited.append(vertex)
        # print("x: " + str(vertex.x) + " y: " + str(vertex.y))
        if goal_found(vertex):
            print("found")
            vertex.print_path()
            break
        # same as above breadth_first_search but add the portal vertex at the beginning of the frontier
        else:
            append_neighbors(vertex)


def display_world():
    global world
    for line in world:
        print(line)


def startup(sheet, search_type):
    global world, already_visited, portal_list, frontier

    world = define_world(sheet)
    start_vertex = find_start()
    append_neighbors(start_vertex)
    already_visited = [start_vertex]
    # portal_list = find_portals()

    if search_type is "dfs":
        depth_first_search()
    elif search_type is "bfs":
        breadth_first_search()

    return world

# print("Breadth first search begins")
# breadth_first_search()
# frontier = [start_vertex]
# print("Depth first search begins")
# depth_first_search()


# TODO **DONE** Git zum Laufen kriegen ==> Git ignore
# TODO Wie Abgabe?  per zip? --> Warte auf Feedback von Twiefel
# TODO Portale hinkriegen

# TODO Aufgabe 1	Karim
# TODO Aufgabe 2	Christian
# TODO Aufgabe 3	Lisa
# TODO Aufgabe 4	Mav
# TODO Aufgabe 5	Josh
# TODO Aufgabe 6	Karim