import pygame
import help
from classes import (Mouse, Button)

pygame.init()
ALTURA, LARGURA = 800, 600
WIN = pygame.display.set_mode((ALTURA, LARGURA))

squarew = pygame.image.load('quadradobranco20x20.png').convert_alpha()
squareg = pygame.image.load('quadradocinza20x20.png').convert_alpha()

def main():
    run = True
    clock = pygame.time.Clock()

    back_color = (0, 0, 0)

    mouse = Mouse()
    button = Button(400, 300, (squarew, squareg), 3)

    while run:
        clock.tick(240)
        WIN.fill(back_color)
        mouse.data_mouse()
        button.do_all(mouse, WIN)

        back_color = (help.get_color(button.position[0]), 0, 0)
        print(help.get_color(button.position[0]))

        print(mouse.position)
        print(mouse.left, mouse.right, mouse.scroll)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        pygame.display.update()

    pygame.quit()

main()