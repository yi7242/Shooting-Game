import pygame
from pygame.locals import *
import sys
import math
pygame.init() # 初期化
screen = pygame.display.set_mode((640,480))
screensize = screen.get_size
background = pygame.Surface(screen.get_size())
background.fill((255,255,255))
screen.blit(background,(0,0))
background = background.convert()

player_surface = pygame.Surface((25,42))
player_surface.fill((255,255,255))
player_rect = pygame.draw.polygon(player_surface, pygame.Color("green"),((0,42), (12.5,0), (25,0)))



right = True
class Player(pygame.sprite.Sprite):
	
	def __init__(self, x, y, health=500):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load("./playerpic.png")
		width = self.image.get_width()
		height = self.image.get_height()
		self.rect = pygame.Rect(x, y, width, height)
		print(width,height)
	def draw(self):
		screen.blit(self.image, self.rect)
	def aim(self, confusion = False):
		mouse_pos = pygame.mouse.get_pos()
		sub_x = mouse_pos[0]-self.rect.x
		sub_y = mouse_pos[1]-self.rect.y
		angle = math.degrees(math.atan2(sub_x, sub_y))
		angle = angle + 180
		self.image = pygame.transform.rotate(pygame.image.load("./playerpic.png"), angle)
	def move(self, speed = 1):
		keys = pygame.key.get_pressed()
		if keys[K_UP] or keys[K_w]:
			self.rect.y-= speed
		if keys[K_DOWN] or keys[K_s]:
			self.rect.y += speed
		if keys[K_RIGHT] or keys[K_d]:
			self.rect.x += speed
		if keys[K_LEFT] or keys[K_a]:
			self.rect.x -= speed
		self.rect.clamp_ip(screen.get_rect())
		
class Enemy(pygame.sprite.Sprite):

	def __init__(self, x, y, health = 100):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.surface.Surface((10,10))
		self.image.fill((255,255,0))
		width = self.image.get_width()
		height = self.image.get_height()
		self.rect = pygame.Rect(x, y, width, height)
	def draw(self):
		screen.blit(self.image, self.rect)

class Bullet(pygame.sprite.Sprite):

	def  __init__(self, x, y, bullet_speed = 10):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.Surface((1,5))
		self.image.fill((255,0,0))
		width = self.image.get_width()
		height = self.image.get_height()
		self.rect = pygame.Rect(x, y, width, height)
	def draw(self):  #デバッグ用
		screen.blit(self.image, self.rect)
	def shoot(self):
		pygame.event.get()
		mousestatus = pygame.mouse.get_pressed()
		if mousestatus[0]:
			screen.blit(self.image, (20,20))
def main():
	pygame.display.set_caption("ShootingGame") #初期設定
	loop = True

	Player1 = Player(0, 0)
	Enemy1 = Enemy(100,100,10)
	Testbullet = Bullet(50,50)
	while loop:
		screen.blit(background,(0,0))
		screen.blit(player_surface, (200,200))
		Player1.draw()
		Enemy1.draw()
		Player1.move()
		Player1.aim()
		Testbullet.shoot()
		pygame.display.flip()
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				loop = False
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE:
					pygame.quit()
					loop = False
if __name__ == "__main__":
	main()