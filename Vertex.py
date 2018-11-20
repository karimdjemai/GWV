class Vertex:
    def __init__(self, x , y, parent):
        self.x = x
        self.y = y
        self.parent = parent
        self.distance_from_start = 1
        self.value = 1

    @staticmethod
    def not_in(vertex_a, list):
        # überprüft ob vertex A in der liste ist, unabhängig vom Parent

        for vertex_b in list:
            if vertex_a.x == vertex_b.x and vertex_a.y == vertex_b.y:
                return False
        return True

    @staticmethod
    def vertex_out_of_list(vertex, list):
        for vertex_b in list:
            if vertex.x == vertex_b.x and vertex.y == vertex_b.y:
                return vertex_b

    def print_path(self):
        current_vertex = self
        path = ""

        while current_vertex:
            path = "[x: " + str(current_vertex.x) + ", y: " + str(current_vertex.y) + "] " + path
            current_vertex = current_vertex.parent
        print("Path: " + path)

    def return_path(self):
        current_vertex = self
        path = ""

        while current_vertex:
            path = "[x: " + str(current_vertex.x) + ", y: " + str(current_vertex.y) + "] " + path
            current_vertex = current_vertex.parent

        return path

    def set_parent(self, parent_vertex):
        return Vertex(self.x, self.y, parent_vertex)

    # Returns the Manhattan distance from one vertex to another
    def dist_man(self, other):
        return abs(self.x - other.x) + abs(self.y - other.y)