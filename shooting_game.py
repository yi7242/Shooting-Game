import pygame
from pygame.locals import *
import sys
import math
import random

pygame.init()  # 初期化
screen = pygame.display.set_mode((1200, 600))
screensize = screen.get_size
background = pygame.Surface(screen.get_size())
background.fill((255, 255, 255))
screen.blit(background, (0, 0))
background = background.convert()

score = 0


class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("playerpic.png").convert_alpha()
        width = self.image.get_width()
        height = self.image.get_height()
        self.rect = Rect(x, y, width, height)
        self.reload_timer = 0

    def update(self):
        speed = 1
        reload_time = 5
        keys = pygame.key.get_pressed()

        mouse_pos = pygame.mouse.get_pos()
        sub_x = mouse_pos[0] - self.rect.x
        sub_y = mouse_pos[1] - self.rect.y
        angle = math.atan2(sub_x, sub_y)

        self.surf = pygame.transform.rotate(self.image, math.degrees(angle) + float(180))
        if keys[K_s]:
            self.rect.y += speed
        if keys[K_d]:
            self.rect.x += speed
        if keys[K_a]:
            self.rect.x -= speed
        if keys[K_w]:
            self.rect.y -= speed

        mouse_pressed = pygame.mouse.get_pressed()
        if self.reload_timer > 0:
            self.reload_timer -= 1
        if mouse_pressed[0]:
            if self.reload_timer <= 0:
                Bullet(self.rect.center)
                self.reload_timer = reload_time
        self.rect.clamp_ip(screen.get_rect())

    def draw(self):
        screen.blit(self.surf, self.rect)

    def pos(self):
        return self.rect.x, self.rect.y


class Enemy(pygame.sprite.Sprite):

    def __init__(self, x, y, health=100):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.image = pygame.Surface((10, 10))
        self.image.fill((0, 0, 255))
        width = self.image.get_width()
        height = self.image.get_height()
        self.rect = pygame.Rect(x, y, width, height)
        self.rect.clamp_ip(screen.get_rect())

    def draw(self):
        screen.blit(self.image, self.rect)

    def update(self, x, y):
        speed = 1
        sub_x = self.rect.x - x
        sub_y = self.rect.y - y
        angle = math.atan2(sub_x, sub_y)
        print(angle)
        self.rect.x += math.sinmath.degees(angle) * speed
        self.rect.y += math.cos(angle) * speed
        self.rect.clamp_ip(screen.get_rect())



class Bullet(pygame.sprite.Sprite):

    def __init__(self, pos):
        bullet_speed = 5
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.image = pygame.Surface((4, 4))
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.center = pos
        self.mouse_pos = pygame.mouse.get_pos()

    def draw(self):  # デバッグ用
        screen.blit(self.image, self.rect)

    def update(self, x, y):
        speed = 10
        mouse_pos = pygame.mouse.get_pos()
        sub_x = self.mouse_pos[0] - x
        sub_y = self.mouse_pos[1] - y
        angle = math.atan2(sub_x, sub_y)
        self.rect.x += math.sin(angle) * speed
        self.rect.y += math.cos(angle) * speed
        if screen.get_rect().contains(self.rect):
            pass
        else:
            self.kill()


def collision_detection(bullet, enemy):
    collision = pygame.sprite.groupcollide(bullet, enemy, True, True)
    # score += 1


def main():
    pygame.display.set_caption("ShootingGame")  # 初期設定
    loop = True

    enemy = pygame.sprite.Group()
    bullets = pygame.sprite.Group()

    Bullet.containers = bullets
    Enemy.containers = enemy

    Player1 = Player(screen.get_rect().centerx, screen.get_rect().centery)

    timer = pygame.time.get_ticks()
    while loop:
        screen.blit(background, (0, 0))
        timer2 = pygame.time.get_ticks()
        yoko = screen.get_width()
        tate = screen.get_height()
        if timer2 - timer >= 3000:
            timer = timer2
            rand = random.randint(1, 4)
            if rand == 1:
                Enemy(random.randint(0, yoko), 0)
            elif rand == 2:
                Enemy(yoko, random.randint(0, tate))
            elif rand == 3:
                Enemy(random.randint(0, yoko), tate)
            elif rand == 4:
                Enemy(0, random.randint(0, tate))
        player_pos = Player1.pos()
        enemy.update(player_pos[0], player_pos[1])
        bullets.update(player_pos[0], player_pos[1])
        Player1.update()

        Player1.draw()
        enemy.draw(screen)
        bullets.draw(screen)

        collision_detection(bullets, enemy)
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
# TODO 敵がプレイヤーに近づくようにする
# TODO スコア等フォントで表示
# TODO 背景の変化
# TODO　スコアの表示の仕方を多少変える
# TODO　敵やプレイヤーの描写をかっこよく
# TODO 敵が自分に当たったらゲームオーバー
