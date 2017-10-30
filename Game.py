import pygame
import Snake
import sys
import random
import Menu
import AI
from collections import deque

class Pelet:
    color = (0, 0, 255)
    def __init__(self, _x, _y):
        self.x =_x*20 + 10
        self.y =_y*20 + 10

    def draw(self, board):
        pygame.draw.circle(board, Pelet.color, (self.x, self.y), 10)

class Board:
    def __init__(self, window, x, y):
        self.width = x
        self.height = y
        self.score = 0
        self.inputBuffer = deque([]);
        self.AI = AI.PathFinder();


        self.food = Pelet(random.randint(0, self.width/20), random.randint(0, self.height/20))
        self.screen = window
        self.snakePath = []
        self.snake = Snake.Snake()
        self.AI.setGameState(self)
        self.snakePath = self.AI.getMovments()

    def drawSegment(self, segment):
        pygame.draw.rect(self.screen, segment.color, (segment.x, segment.y, segment.width, segment.height))

    def checkFoodSnakeCollision(self):
        return (self.snake.head.x == self.food.x - 10) and (self.snake.head.y == self.food.y - 10)

    def removeFood(self):
        newX = 0
        newY = 0
        self.score += 100
        inSnake = True
        # we gotta make sure the pellet doesnt spawn inside of the snake
        while inSnake:
            newX = random.randint(1, self.width/20 - 2)
            newY = random.randint(1, self.height / 20 - 2)
            inSnake = False
            for segement in self.snake.body:
                if newX == segement.x and newY == segement.y:
                    inSnake = True

        self.food = Pelet(newX, newY)
        self.food.draw(self.screen)

    # exaimes possible lose conditions and calls the lose function in the case that we have lost
    def checkLose(self):
        # out of bounds?
        if self.snake.head.x < 0 or self.snake.head.x > self.width or self.snake.head.y < 0 or self.snake.head.y > self.height:
            Menu.lose(self.screen, self.score)
        # self collision?
        else:
            for i  in range(1, len(self.snake.body) - 1) :
                if self.snake.head.x == self.snake.body[i].x and self.snake.head.y == self.snake.body[i].y:
                    Menu.lose(self.screen, self.score)

    def mainLoop(self):
        while 1:
            # reset the screen
            self.screen.fill((0, 0, 0))
            self.food.draw(self.screen)

            # get the player input, may need to funcitonize this if it grows much larger
            #for event in pygame.event.get():
            #   if event.type == pygame.QUIT:
            #        sys.exit()
            #   elif event.type == pygame.KEYDOWN:
            #        if event.key == pygame.K_DOWN and len(self.inputBuffer) < 2:
            #            self.inputBuffer.append((0, 1))
            #        elif event.key == pygame.K_UP and len(self.inputBuffer) < 2:
            #            self.inputBuffer.append((0, -1))
            #        elif event.key == pygame.K_LEFT and len(self.inputBuffer) < 2:
            #            self.inputBuffer.append((-1, 0))
            #        elif event.key == pygame.K_RIGHT and len(self.inputBuffer) < 2:
            #            self.inputBuffer.append((1, 0))

            #if len(self.inputBuffer) > 0:
            #    dirVec = self.inputBuffer.popleft()
            #    self.snake.changeDir(dirVec[0], dirVec[1])


            if len(self.snakePath) == 0:
                self.AI.setGameState(self)
                self.snakePath = self.AI.getMovments()

            if len(self.snakePath) != 0:
                movVec = self.snakePath.pop()
                self.snake.changeDir(movVec[0], movVec[1])

            # move the snake and make sure we didnt lose,
            self.snake.move()
            self.checkLose()
            if self.checkFoodSnakeCollision():
                self.removeFood()
                self.snake.grow()
                self.AI.setGameState(self)
                self.snakePath = self.AI.getMovments()

            # draw the snake
            for segment in self.snake.body:
                self.drawSegment(segment)

            pygame.display.update()
            pygame.time.delay(50)
