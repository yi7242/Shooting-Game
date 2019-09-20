import pygame
from pygame.locals import *
import sys
import math

pygame.init()  # 初期化
screen = pygame.display.set_mode((640, 480))
screensize = screen.get_size
background = pygame.Surface(screen.get_size())
background.fill((255, 255, 255))
screen.blit(background, (0, 0))
background = background.convert()

player_surface = pygame.Surface((25, 42))
player_surface.fill((255, 255, 255))
player_rect = pygame.draw.polygon(player_surface, pygame.Color("green"), ((0, 42), (12.5, 0), (25, 42)))

right = True


def move(speed):
    keys = pygame.key.get_pressed()
    x,y =
    if keys[K_UP] or keys[K_w]:
         -= speed
    if keys[K_DOWN] or keys[K_s]:
        player_rect.y += speed
    if keys[K_RIGHT] or keys[K_d]:
        player_rect.x += speed
    if keys[K_LEFT] or keys[K_a]:
        player_rect.x -= speed
    player_rect.clamp_ip(screen.get_rect())

def aim():
    mouse_pos = pygame.mouse.get_pos()
    sub_x = mouse_pos[0] - player_rect.x
    sub_y = mouse_pos[1] - player_rect.y
    angle = math.degrees(math.atan2(sub_x, sub_y))
    angle = angle + 180
    spin_surface = pygame.transform.rotate(player_surface, angle)
    return spin_surface


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

    def __init__(self, x, y, bullet_speed=10):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((1, 5))
        self.image.fill((255, 0, 0))
        width = self.image.get_width()
        height = self.image.get_height()
        self.rect = pygame.Rect(x, y, width, height)

    def draw(self):  # デバッグ用
        screen.blit(self.image, self.rect)

    def shoot(self):
        pygame.event.get()
        mousestatus = pygame.mouse.get_pressed()
        if mousestatus[0]:
            screen.blit(self.image, (20, 20))


def main():
    pygame.display.set_caption("ShootingGame")  # 初期設定
    loop = True

    Enemy1 = Enemy(100, 100, 10)
    Testbullet = Bullet(50, 50)
    while loop:
        screen.blit(background, (0, 0))
        player_surface = aim()
        print(player_surface)
        Enemy1.draw()
        move(1)
        Testbullet.shoot()
        screen.blit(player_surface, (0, 0))
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == QUIT:
                loop = False
                pygame.quit()
                sys.exit(0)
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    loop = False
                    pygame.quit()
                    sys.exit(0)

if __name__ == "__main__":
    main()
