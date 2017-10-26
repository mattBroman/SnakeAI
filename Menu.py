import Game
import pygame
import sys

def lose(screen, score):
    window = LoseScreen(screen, score)
    window.loseLoop()

def start(screen):
    window = StartScreen(screen)
    window.startLoop()

class LoseScreen :

    width = 640
    height = 480
    playAgainCoord = (width*(1/8), height*(3/4), width*(5/16), height/8)
    quitCoord = (width * (9 / 16), height * (3 / 4), width * (5 / 16), height / 8)
    scoreCoord = (width *(1/16), height * (1/8), width *(7/8), height * (9/16))
    def __init__(self, window, score):
        self.screen = window
        self.font = pygame.font.SysFont("comicsansms", 40)
        self.playAgainText = self.font.render("Play Again", True, (255, 255, 255))
        self.quitText = self.font.render("Quit", True, (255, 255, 255))
        self.scoreText = self.font.render(str(score), True, (255,255,255))

    def loseLoop(self):
        self.screen = pygame.display.set_mode((LoseScreen.width, LoseScreen.height))
        #draw both buttons and display text.
        pygame.draw.rect(self.screen, (255, 0, 0), LoseScreen.playAgainCoord)
        pygame.draw.rect(self.screen, (255, 0, 0), LoseScreen.quitCoord)
        pygame.draw.rect(self.screen, (255, 0, 0), LoseScreen.scoreCoord)
        self.screen.blit(self.playAgainText, (LoseScreen.width*(1/8) + 5, LoseScreen.height*(3/4)))
        self.screen.blit(self.quitText, (LoseScreen.width*(9/16) + 60, LoseScreen.height*(3/4)))
        self.screen.blit(self.scoreText, (LoseScreen.scoreCoord[0] + 5, LoseScreen.scoreCoord[1] + 10))
        pygame.display.update();

        while 1 :
            for event in pygame.event.get():
                if event.type == pygame.QUIT :
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    coord = pygame.mouse.get_pos();
                    #if they clicked in play again launch the game again
                    if (LoseScreen.playAgainCoord[0] < coord[0] < LoseScreen.playAgainCoord[0] + LoseScreen.playAgainCoord[2] and
                       LoseScreen.playAgainCoord[1] < coord[1] < LoseScreen.playAgainCoord[1] + LoseScreen.playAgainCoord[3]):
                        mainWindow = Game.Board(self.screen, 640, 480)
                        mainWindow.mainLoop()
                    #else if they clicked quit exit.
                    if (LoseScreen.quitCoord[0] < coord[0] < LoseScreen.quitCoord[0] + LoseScreen.quitCoord[2] and
                       LoseScreen.quitCoord[1] < coord[1] < LoseScreen.quitCoord[1] + LoseScreen.quitCoord[3]):
                        sys.exit()
