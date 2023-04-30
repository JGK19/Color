import pygame
from help import (get_color_rgb)
from classes import (Mouse, Button)

pygame.init()
ALTURA, LARGURA = 800, 600
WIN = pygame.display.set_mode((ALTURA, LARGURA))

squarew = pygame.image.load('quadradobranco20x20.png').convert_alpha()
squareg = pygame.image.load('quadradocinza20x20.png').convert_alpha()

def main():
    run = True
    clock = pygame.time.Clock()

    back_color = (255, 0, 0)

    mouse = Mouse()
    button_rgb = Button(100, 300, (squarew, squareg), 3, 'H')

    while run:
        clock.tick(240)
        WIN.fill(back_color)
        mouse.data_mouse()
        button_rgb.do_all(mouse, WIN)

        new_rgb = get_color_rgb(button_rgb.position[0], button_rgb.bar['largura'], button_rgb.position0[0], back_color)

        back_color = new_rgb
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        pygame.display.update()

    pygame.quit()

main()