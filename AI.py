import Game
import pygame


class PathFinder :

    def __init__(self):
        self.gameState = None
        self.end = None
        self.start = None
        self.path = []
        self.grid = []


    def setGameState(self, gameState):
        self.gameState = gameState;
        self.end = (int((gameState.food.x - 10) / 20), int((gameState.food.y - 10) / 20))
        self.start = (int(gameState.snake.head.x / 20), int(gameState.snake.head.y / 20))
        self.path = []
        self.grid = []

    def getMovments(self):
        self.gameStateToGrid()
        moveVec = []
        self.path = self.aStar()
        for i in range(0, len(self.path) - 1):
            if self.path[i].x < self.path[i +1].x:
                moveVec.append((-1, 0))
            elif self.path[i].x > self.path[i + 1].x:
                moveVec.append((1, 0))
            elif self.path[i].y < self.path[i + 1].y:
                moveVec.append((0, -1))
            else:
                moveVec.append((0, 1))
        return moveVec



    def aStar(self):
        closedSet = []
        openSet = [      self.grid[ self.start[0] ][ self.start[1] ]   ]
        #self.drawOpenSet();

        #while we have nodes to explore:
        while len(openSet) > 0 :
            current = openSet[0]
            #find the node least difficult to travel
            for node in openSet:
                if node.hScore < current.hScore :
                    current = node

            #we found it! return the path to take
            if current.x/20 == self.end[0] and current.y/20 == self.end[1] :
                return self.reconstructPath(current)

            #remove current from  the open set and add it to the closed set.
            openSet.remove(current)
            print("Open set length: " + str(len(openSet)))
            closedSet.append(current)
            print("Close set length: " + str(len(closedSet)))

            #check all the neighbours not yet explored
            x = int(current.x/20)
            y = int(current.y/20)

            if  (x != 0 and
                not self.grid[x-1][y].inSnake and
                not self.grid[x-1][y] in closedSet) :
                    self.evalNeighbour(self.grid[x-1][y], openSet, current)

            if  (x != len(self.grid) - 1 and
                not self.grid[x+1][y].inSnake and
                not self.grid[x+1][y] in closedSet):
                    self.evalNeighbour(self.grid[x+1][y], openSet, current)

            if  (y != 0 and
                not self.grid[x][y-1].inSnake and
                not self.grid[x][y-1] in closedSet) :
                    self.evalNeighbour(self.grid[x][y-1], openSet, current)

            if  (y != len(self.grid[x]) - 1 and
                not self.grid[x][y+1].inSnake and
                not self.grid[x][y+1] in closedSet) :
                    self.evalNeighbour(self.grid[x][y+1], openSet, current)

            #self.drawOpenSet()
            #self.drawClosedSet()
            #self.gameState.

        return []


    def evalNeighbour(self, evalNode, openSet, current):
        openSet.append(evalNode)
        if evalNode.hScore < current.hScore :
            evalNode.previous = current

    def reconstructPath(self, node):
        nodes = []
        while node.previous != None:
            nodes.append(node)
            node = node.previous
        nodes.append(node)
        return nodes

    def find(self, container, target):
        loc = 0
        for node in container :
            if node.x == target.x and node.y == target.y:
                return loc
            loc += 1
        return -1


    def gameStateToGrid(self):
        for i in range(0, int(self.gameState.width/20)) :
            x = i*20
            rowList = []
            for j in range (0, int(self.gameState.height/20)) :
                y = j*20
                if self.notInSnake(x,y) :
                    node = Node(x,y, False, self.dist(x, y, self.end[0]*20, self.end[1]*20))
                else :
                    node = Node(x, y, True, self.dist(x, y, self.end[0]*20, self.end[1]*20))
                rowList.append(node)
            self.grid.append(rowList)


    def notInSnake(self, x, y):
        for segment in self.gameState.snake.body :
            if x == segment.x and y == segment.y :
                return False
        return True


    def dist(self, x, y, targetX, targetY):
        return abs(x - targetX) + abs(y - targetY)


class Node:

    def __init__(self, x, y, inSnake, distFood):
        self.x = x
        self.y = y
        self.hScore = distFood
        self.inSnake = inSnake
        self.previous = None
