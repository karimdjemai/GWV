class Vertex:
    def __init__(self, x , y, parent):
        self.x = x
        self.y = y
        self.parent = parent

    @staticmethod
    def notIn(vertexA, list):
        # überprüft ob vertex A in der liste ist, unabhängig vom Parent

        for vertexB in list:
            if vertexA.x == vertexB.x and vertexA.y == vertexB.y:

                return False
        return True

    def printPath(self):
        currentVertex = self
        path = ""

        while currentVertex:
            path = "[x: " + str(currentVertex.x) + ", y: " + str(currentVertex.y) + "] " + path
            currentVertex = currentVertex.parent
        print("Path: " + path)