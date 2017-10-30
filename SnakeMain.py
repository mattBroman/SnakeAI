import Snake
import Game
import pygame

pygame.init()
window = pygame.display.set_mode((640, 480))
mainWindow = Game.Board(window, 640, 480)
mainWindow.mainLoop()
