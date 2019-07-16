import pygame
from pygame.locals import *


white = [255, 255, 255]

def main():
    pygame.init()
    screen = pygame.display.set_mode((600, 500))

    screen.fill(white)
    start_button = pygame.draw.rect(screen,(0, 170, 0),(250, 350, 100, 50))
    pygame.display.flip()
    header = 'images/header.png'

    clock = pygame.time.Clock()
    winner = False
    play = False
    while not winner:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if not play:
                _header = pygame.image.load(header).convert_alpha()
                picture = pygame.transform.scale(_header, (600, 270))
                screen.blit(picture, (0, 20))
                pygame.display.update()
        clock.tick(15)

if __name__ == "__main__" :
    main()