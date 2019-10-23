import pygame
from pygame.locals import *
import sys
import math

pygame.init()  # 初期化
screen = pygame.display.set_mode((1500, 900))
screensize = screen.get_size
background = pygame.Surface(screen.get_size())
background.fill((255, 255, 255))
screen.blit(background, (0, 0))
background = background.convert()
global player_surface
player_surface = pygame.Surface((25, 42))
player_surface.fill((255, 255, 255))
player_rect = pygame.draw.polygon(player_surface, pygame.Color("green"), ((0, 42), (12.5, 0), (25, 42)))
right = True

class Player(pygame.sprite.Sprite):
    speed = 5
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(playerpic.png).convert_alpha()
        width = self.image.get_width()
        height = self.image.get_height()
        self.rect = Rect(x, y, width, height)
    def update(self):
        keys = pygame.key.get_pressed()
        if keys[K_UP] or keys[K_w]:
            self.rect.x -= speed
        if keys[K_DOWN] or keys[K_s]:
            self.rect.y += speed
        if keys[K_RIGHT] or keys[K_d]:
            self.rect.x += speed
        if keys[K_LEFT] or keys[K_a]:
            self.rect.x -= speed
        self.rect.clamp_ip(screen)




class Enemy(pygame.sprite.Sprite):

    def __init__(self, x, y, health=100):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((10, 10))
        self.image.fill((255, 255, 0))
        width = self.image.get_width()
        height = self.image.get_height()
        self.rect = pygame.Rect(x, y, width, height)

    def draw(self):
        screen.blit(self.image, self.rect)


class Bullet(pygame.sprite.Sprite):

    def __init__(self, x, y):
        bullet_speed = 5
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((10, 10))
        self.image.fill((255, 0, 0))
        width = self.image.get_width()
        height = self.image.get_height()
        self.rect = pygame.Rect(x, y, width, height)

    def draw(self):  # デバッグ用
        screen.blit(self.image, self.rect)

    def shoot(self, x, y):
        mouse_pressed = pygame.mouse.get_pressed()
        if mouse_pressed[0]:
            mouse_pos = pygame.mouse.get_pos()
            sub_x = mouse_pos[0] - x
            sub_y = mouse_pos[1] - y
            angle = math.degrees(math.atan2(sub_x, sub_y))
            self.rect.x += math.sin(angle) * 5
            self.rect.y += math.cos(angle) * 5



def main():
    pygame.display.set_caption("ShootingGame")  # 初期設定
    loop = True

    Enemy1 = Enemy(100, 100, 10)
    px = 0
    py = 0
    while loop:
        screen.blit(background, (0, 0))
        Enemy1.draw()
        px, py = move(1, px, py)
        spin_surface = aim(px, py)
        screen.blit(spin_surface, (px, py))
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == QUIT:
                loop = False
                exit()
                sys.exit(0)
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    loop = False
                    exit()
                    sys.exit(0)


if __name__ == "__main__":
    main()
