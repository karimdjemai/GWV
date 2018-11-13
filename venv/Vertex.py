class Vertex:
    def __init__(self, x , y, parent):
        self.x = x
        self.y = y
        self.parent = parent

    @staticmethod
    def not_in(vertex_a, list):
        # überprüft ob vertex A in der liste ist, unabhängig vom Parent

        for vertex_b in list:
            if vertex_a.x == vertex_b.x and vertex_a.y == vertex_b.y:
                return False
        return True

    def print_path(self):
        current_vertex = self
        path = ""

        while current_vertex:
            path = "[x: " + str(current_vertex.x) + ", y: " + str(current_vertex.y) + "] " + path
            current_vertex = current_vertex.parent
        print("Path: " + path)

    def set_parent(self, parent_vertex):
        self.parent = parent_vertex