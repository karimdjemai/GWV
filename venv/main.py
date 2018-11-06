text_file = open("blatt3_environment.txt", "r")
lines = text_file.readlines()

h, w = len(lines), len(lines[0]) - 1

world = [[7 for x in range(w)] for y in range(h)]

for line in range(len(lines)):
  for char in range(len(lines[line])-1):
    world[line][char] = lines[line][char]
print(world)


class Vertex:
  def __init__(self, x, y, parent):
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
    print(path)

position = {'x': 4, 'y': 4}
#print(position['x'])

goalPath = []
alreadyRead = []
frontier = [position]
goalFound = False

def isGoal (x, y):
  return world[x][y] == 'g'

def bFS (x, y):
  if isGoal(x, y):
   print('\nYay')
   global goalFound
   goalFound = True
   return
  print('x: ' + str(x), 'y: ' + str(y))

  # neighbors = direkte nachbarn von position, wenn kein x und nicht in alreadyread
  neighborLeft = {'x': x - 1, 'y': y}
  neighborRight = {'x': x + 1, 'y': y}
  neighborBottom = {'x': x, 'y': y - 1}
  neighborTop = {'x': x, 'y': y + 1}

  pushNeighborToList(neighborLeft)
  pushNeighborToList(neighborRight)
  pushNeighborToList(neighborBottom)
  pushNeighborToList(neighborTop)

  frontier.pop(0)
  alreadyRead.append({'x': x, 'y': y})
  #print(alreadyRead)

  for neighbor in frontier:
    if not goalFound:
      bFS(neighbor['x'], neighbor['y'])



def pushNeighborToList(neighbor):
  # an der position is kein x und die position ist nicht in already read enthalten
  if world[neighbor['x']][neighbor['y']] != 'x' and neighbor not in alreadyRead and neighbor not in frontier:
    frontier.append(neighbor)

bFS(position['x'], position['y'])
