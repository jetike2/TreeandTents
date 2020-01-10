import pygame
import sys

WIDTH = 800
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH,HEIGHT))

def Tile_generator(array):
    x = 0
    y = 0
    for i in range(len(array)):
        for n in range(len(array)):
            if array[i][n] == "#":
                pygame.draw.rect(screen,(0, 255, 0),((x, y),(160, 120)))
            if array[i][n] == "F":
                pygame.draw.rect(screen,(255, 0, 0),((x, y),(160, 120)))

            if array[i][n] == "T":
                pygame.draw.rect(screen,(0, 0, 255),((x, y),(160, 120)))
            x += 160

        x = 0
        y += 120
class GameApp:
    def __init__(self):
        pygame.init()
        
        self.test_array = [  ['#','#','#','#','#'],
                             ['F','T','#','F','#'],
                             ['#','#','#','#','#'],
                             ['#','F','#','F','#'],
                             ['#','#','#','#','#'] ]

    def Execute(self):

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()


            screen.fill((0, 0, 0))
            Tile_generator(self.test_array)

            pygame.display.flip()


if __name__=='__main__':
    game = GameApp()
    
    game.Execute()
