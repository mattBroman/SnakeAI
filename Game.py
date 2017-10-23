import pygame
import Snake
import sys
import random


class Pelet:
    color = (255, 0, 0)
    def __init__(self, _x, _y):
        self.x =_x*20 + 10
        self.y =_y*20 + 10

    def draw(self, board):
        pygame.draw.circle(board, Pelet.color, (self.x, self.y), 10)
        #pygame.display.update()

class Board:
    def __init__(self, x, y):
        self.width = x
        self.height = y

        pygame.init()
        self.food = Pelet(random.randint(0, self.width/20), random.randint(0, self.height/20))
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.snake = Snake.Snake()

    def drawSegment(self, segment):
        pygame.draw.rect(self.screen, segment.color, (segment.x, segment.y, segment.width, segment.height))
        #pygame.display.update()

    def checkFoodSnakeCollision(self):
        return (self.snake.head.x == self.food.x - 10) and (self.snake.head.y == self.food.y - 10)

    def removeFood(self):
        newX = 0
        newY = 0
        inSnake = True
        while inSnake:
            newX = random.randint(1, self.width/20 - 1)
            newY = random.randint(1, self.height / 20 - 1)
            inSnake = False
            for segement in self.snake.body:
                if newX == segement.x and newY == segement.y:
                    inSnake = True

        self.food = Pelet(newX, newY)
        self.food.draw(self.screen)

    def checkLoose(self):
        if self.snake.head.x < 0 or self.snake.head.x > self.width or self.snake.head.y < 0 or self.snake.head.y > self.height:
            self.loose()
        else:
            i = 1
            while i < len(self.snake.body) - 1:
                if self.snake.head.x == self.snake.body[i].x and self.snake.head.y == self.snake.body[i].y:
                    self.loose()
                i += 1

    def loose(self):
        print("lose")

    def mainLoop(self):
        while 1:
            self.screen.fill((0, 0, 0))
            self.food.draw(self.screen)

            self.snake.move()
            self.checkLoose()
            if self.checkFoodSnakeCollision():
                self.removeFood()
                self.snake.grow()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:
                        self.snake.changeDir(0, 1)
                    elif event.key == pygame.K_UP:
                        self.snake.changeDir(0, -1)
                    elif event.key == pygame.K_LEFT:
                        self.snake.changeDir(-1, 0)
                    elif event.key == pygame.K_RIGHT:
                        self.snake.changeDir(1, 0)

            for segment in self.snake.body:
                self.drawSegment(segment)

            pygame.display.update()
            pygame.time.delay(50)
