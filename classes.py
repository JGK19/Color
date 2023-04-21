import pygame

class Mouse:
    def __init__(self):
        self.position = None
        self.left_mouse = None
        self.scroll_mouse = None
        self.right_mouse = None
    
    def data_mouse(self):
        self.position = pygame.mouse.get_pos()
        self.left = pygame.mouse.get_pressed()[0] == 1
        self.scroll = pygame.mouse.get_pressed()[1] == 1
        self.right = pygame.mouse.get_pressed()[2] == 1


class Button:
    def __init__(self, x, y, images, scale):
        largura = images[0].get_size()[0]
        altura = images[0].get_size()[1]
        print(largura, altura)
        self.position = (x, y)
        self.image = pygame.transform.scale(images[0], (int(largura * scale), int(altura * scale)))
        self.image_click = pygame.transform.scale(images[1], (int(largura * scale), int(altura * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (self.position[0], self.position[1])
        self.pressed = False
        self.pressing = False

    def do_all(self, mouse, win):
        pygame.draw.rect(win, (0,0,0), (100,300,600,60))
        self.rect.topleft = (self.position[0], self.position[1])
        self.draw(win)
        self.is_click(mouse, win)
        self.movel_button(mouse)

    def draw(self, win):
        if not self.pressing:
            win.blit(self.image, (self.rect.x, self.rect.y))
            #pygame.draw.circle(win, (255,255,255), (self.rect.x, self.rect.y), 60)
        else:
            win.blit(self.image_click, (self.rect.x, self.rect.y))
            #pygame.draw.circle(win, (127,127,127), (self.rect.x, self.rect.y), 60)

    def is_click(self, mouse, win):
        if self.rect.collidepoint(mouse.position):
            if mouse.left and ( not self.pressing):
                self.pressing = True
                self.pressed = False
            elif not mouse.left and (not self.pressed and self.pressing):
                self.pressed = True
                self.pressing = False
    def movel_button(self, mouse):
        if self.pressing:
            position = ((mouse.position[0], self.position[1]))
            if mouse.position[0] < 100:
                position = ((100, self.position[1]))
            elif mouse.position[0] > 640:
                position = ((640, self.position[1]))
            self.position = position
